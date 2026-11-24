# Glossary prototype

A small prototype to discuss how a glossary could work. Nothing here is approved: the terms, wording, field names,
and IDs are all open. It can be deleted without affecting anything else in the repo.

## What it shows

- One data file (`terms.json`) that everything is built from.
- A permanent link for every term, such as `index.html#captions`. An old ID can be kept in `formerIds`, so links to it
  still work after a rename.
- Where each term stands against WCAG and the MSF Glossary: adopted, adopted with an XR note, differs, or ours.
- Criteria that link to terms by ID, and terms that list the criteria using them.
- A build that stops if a criterion links to a term that doesn't exist.

## What it leaves out

- **Source definitions.** Entries link to WCAG and MSF instead of copying their text, because licensing isn't settled.
  One short MSF quote ("immersive") shows how a quoted definition would look.
- **Most terms.** Only 18 are included.

## Try it

Open `index.html`. To change the content, edit `terms.json` or `sample-criteria.json`, then run:

```
python build.py
```

Add `--check-sources` to also check that the WCAG and MSF links still work.
