"""Build the prototype glossary from terms.json and sample-criteria.json.

    python build.py                  build the pages; stop if any glossary link is broken
    python build.py --check-sources  also check that every WCAG and MSF link still works

Uses only the Python standard library.
"""
import html
import json
import re
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
LINK = re.compile(r"\[([^\]]+)\]\(glossary:([^)]+)\)")
RELATIONSHIPS = {
    "adopted": ("Adopted", "Uses the source's definition as it is."),
    "adopted-note": ("Adopted with an XR note", "Uses the source's definition, plus a note on how it applies in XR."),
    "differs": ("Differs", "Our own draft definition, because the sources' do not fit."),
    "ours": ("Ours", "Our own draft definition, with no equivalent in the sources."),
}
esc = html.escape


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def source_url(data, ref):
    return data["sources"][ref["source"]]["base"] + ref["ref"]


def source_refs(term):
    return ([term["definitionFrom"]] if "definitionFrom" in term else []) + term.get("related", [])


def source_link(data, ref):
    name = data["sources"][ref["source"]]["name"]
    return f'<a href="{esc(source_url(data, ref))}">{esc(name)}: {esc(ref["label"])}</a>'


def check(data, criteria):
    """Return (errors, warnings) for the term data and every glossary link."""
    errors, warnings, ids, names = [], [], {}, {}
    for t in data["terms"]:
        for i in [t["id"], *t.get("formerIds", [])]:
            if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", i):
                errors.append(f'ID "{i}" must be lowercase words joined by hyphens')
            if i in ids:
                errors.append(f'ID "{i}" is used by both "{ids[i]}" and "{t["term"]}"')
            ids[i] = t["term"]
        for n in [t["term"], *t.get("aliases", [])]:
            if n.lower() in names:
                errors.append(f'the name "{n}" belongs to both "{names[n.lower()]}" and "{t["term"]}"')
            names[n.lower()] = t["term"]
        if t["relationship"] not in RELATIONSHIPS:
            errors.append(f'"{t["term"]}" has an unknown relationship "{t["relationship"]}"')
        elif t["relationship"].startswith("adopted"):
            if "definitionFrom" not in t or "definition" in t:
                errors.append(f'"{t["term"]}" is adopted, so it needs definitionFrom and no definition of its own')
        elif "definition" not in t:
            errors.append(f'"{t["term"]}" needs a definition')
        if t["relationship"] == "adopted-note" and not t.get("notes"):
            errors.append(f'"{t["term"]}" is adopted with an XR note, but has no note')
        for r in source_refs(t):
            if r["source"] not in data["sources"]:
                errors.append(f'"{t["term"]}" cites an unknown source "{r["source"]}"')

    current = {t["id"] for t in data["terms"]}
    for c in criteria:
        seen = set()
        for words, target in LINK.findall(c["text"]):
            if target not in ids:
                errors.append(f'criterion "{c["title"]}" links "{words}" to "{target}", which is not in the glossary')
            elif target not in current:
                warnings.append(f'criterion "{c["title"]}" uses the old ID "{target}"')
            if target in seen:
                warnings.append(f'criterion "{c["title"]}" links "{target}" more than once')
            seen.add(target)
        for words, target in LINK.findall(c.get("flag", "")):
            if target not in ids:
                errors.append(f'the note on "{c["title"]}" links "{words}" to "{target}", which is not in the glossary')
    return errors, warnings


def check_sources(data):
    """Return problems with links to WCAG, WCAG2ICT and the MSF Glossary."""
    errors, pages = [], {}
    for t in data["terms"]:
        for r in source_refs(t):
            url, _, anchor = source_url(data, r).partition("#")
            if url not in pages:
                try:
                    req = urllib.request.Request(url, headers={"User-Agent": "glossary-link-check"})
                    pages[url] = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
                except OSError as e:
                    pages[url] = None
                    errors.append(f"{url} could not be opened ({e})")
            text = pages[url]
            if text is None:
                continue
            if anchor and not re.search(rf"""id=["']?{re.escape(anchor)}["'\s>]""", text):
                errors.append(f'"{t["term"]}": {url} has no "#{anchor}"')
            # MSF numbers are not unique, so confirm that the page is about the expected term.
            word = r["label"].split(" (")[0]
            if r["source"] == "msf" and not re.search(rf">\s*{re.escape(word)}\s*<", text, re.I):
                errors.append(f'"{t["term"]}": {url} is not the page for "{word}"')
            quote = t.get("quote")
            if quote and r is t.get("definitionFrom"):
                plain = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", text)))
                if quote not in plain:
                    errors.append(f'"{t["term"]}": the quoted definition no longer matches {url}')
    return errors, len(pages)


def inline(text):
    out, last = [], 0
    for m in LINK.finditer(text):
        out.append(esc(text[last:m.start()]))
        out.append(f'<a class="term" href="index.html#{esc(m[2])}">{esc(m[1])}</a>')
        last = m.end()
    return "".join(out) + esc(text[last:])


def page(title, body):
    template = (HERE / "template.html").read_text(encoding="utf-8")
    return template.replace("{{title}}", esc(title)).replace("{{body}}", body)


def glossary_page(data, criteria):
    terms = sorted(data["terms"], key=lambda t: t["term"].lower())
    used = {t["id"]: [] for t in terms}
    for c in criteria:
        for target in dict.fromkeys(m[1] for m in LINK.findall(c["text"])):
            if target in used:
                used[target].append(c)
    out = [
        "<h1>Glossary prototype</h1>",
        "<p>Each term has its own permanent link, and points to the WCAG or MSF definition it uses or differs from. "
        'See the terms in use on the <a href="sample-criteria.html">sample criteria page</a>.</p>',
        '<h2>How each term relates to its sources</h2>\n<dl class="key">',
    ]
    for label, meaning in RELATIONSHIPS.values():
        out.append(f"<div><dt>{label}</dt><dd>{meaning}</dd></div>")
    out.append('</dl>\n<nav aria-labelledby="all-terms">\n<h2 id="all-terms">All terms</h2>\n<ul class="index">')
    out += [f'<li><a href="#{t["id"]}">{esc(t["term"])}</a></li>' for t in terms]
    out.append("</ul>\n</nav>\n<h2>Definitions</h2>")
    for t in terms:
        former = "".join(f'<span id="{esc(i)}"></span>' for i in t.get("formerIds", []))
        out.append(f'<article id="{t["id"]}" tabindex="-1" aria-labelledby="h-{t["id"]}">{former}')
        out.append(f'<h3 id="h-{t["id"]}">{esc(t["term"])}</h3>')
        if t.get("aliases"):
            out.append(f'<p class="meta">Also: {esc(", ".join(t["aliases"]))}</p>')
        out.append(f'<p class="meta">Relationship: <strong>{RELATIONSHIPS[t["relationship"]][0]}</strong></p>')
        if "definition" in t:
            out.append(f'<p><strong>Draft definition:</strong> {esc(t["definition"])}</p>')
        else:
            src = source_link(data, t["definitionFrom"])
            body = f'<q>{esc(t["quote"])}</q> ({src})' if t.get("quote") else src
            out.append(f"<p><strong>Definition:</strong> {body}</p>")
        for n in t.get("notes", []):
            out.append(f'<p class="note"><strong>Draft note:</strong> {esc(n)}</p>')
        if t.get("related"):
            out.append("<p>Related: " + "; ".join(source_link(data, r) for r in t["related"]) + "</p>")
        if used[t["id"]]:
            links = ", ".join(f'<a href="sample-criteria.html#{c["id"]}">{esc(c["title"])}</a>' for c in used[t["id"]])
            out.append(f"<p>Used in: {links}</p>")
        out.append(f'<p><a href="#{t["id"]}">Link to “{esc(t["term"])}”</a></p>\n</article>')
    return page("Glossary prototype", "\n".join(out))


def criteria_page(criteria):
    out = [
        "<h1>Sample criteria with glossary links</h1>",
        "<p>Wording is from the public working document of 20 November 2026, with links added. "
        "Each term is linked the first time it appears in a criterion. "
        'Back to the <a href="index.html">glossary</a>.</p>',
    ]
    for c in criteria:
        out.append(f'<article id="{c["id"]}" tabindex="-1">\n<h2>{esc(c["title"])}</h2>\n<p>{inline(c["text"])}</p>')
        if c.get("flag"):
            out.append(f'<p class="note">{inline(c["flag"])}</p>')
        out.append("</article>")
    return page("Sample criteria with glossary links", "\n".join(out))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    data, criteria = load("terms.json"), load("sample-criteria.json")["criteria"]
    errors, warnings = check(data, criteria)
    if not errors and "--check-sources" in sys.argv:
        errors, count = check_sources(data)
        print(f"Checked sources on {count} pages")
    for w in warnings:
        print("Warning:", w)
    for e in errors:
        print("Error:", e)
    if errors:
        sys.exit(1)
    (HERE / "index.html").write_text(glossary_page(data, criteria), encoding="utf-8", newline="\n")
    (HERE / "sample-criteria.html").write_text(criteria_page(criteria), encoding="utf-8", newline="\n")
    print(f'Built {len(data["terms"])} terms and {len(criteria)} sample criteria')


if __name__ == "__main__":
    main()
