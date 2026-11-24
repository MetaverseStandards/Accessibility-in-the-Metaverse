# CLAUDE.md

Guidance for Claude (and any contributor using Claude) when working in this repository.

## What this repo is

The public repository of the **Accessibility in the Metaverse** group of the
[Metaverse Standards Forum](https://metaverse-standards.org/) (MSF). The group is now a **subgroup of the MSF
3D Assets Working Group**.
- Group page: <https://metaverse-standards.org/domain-groups/accessibility-in-the-metaverse/>
- GitHub: `MetaverseStandards/Accessibility-in-the-Metaverse`

The group finds risks, gathers insights, and recommends strategies and best practices so that immersive
experiences are accessible to everyone. Its main deliverable is the **MSF XR Accessibility Guidelines**: testable
success criteria for XR, comparable to [WCAG 2.2](https://www.w3.org/TR/WCAG22/). Version 1.0 went out for
review in July 2026, and v2.0 is now in progress.

Work here means preparing and sharing material about XR accessibility, chiefly:
- the guidelines website on **GitHub Pages**;
- guidance documents, summaries, explainers, and presentations.

## People and contributors

- **Chairs:** Dylan Fox (Yahoo), Michael Cooper (Aihal Accessibility), and James Maki (Inclusive Reality).
  - In the README, the chairs are a list, not a table, and each LinkedIn link names its person. Keep that
    format when editing.
  - Yahoo stays plain text, with no link.
- The user is usually Dylan, but **other group members also contribute**. In the long run, anyone will be able
  to suggest changes. So:
  - write for contributors who are new to the repo;
  - keep instructions in the repo, not in anyone's personal setup;
  - don't assume the person you're working with is a chair.
- Chair contact list: `accessibility-chair@lists.metaverse-standards.org`.
- Meetings: every other Tuesday, 8am PT / 11am ET / 3pm UTC, on Zoom.

## Source of truth

1. **The guidelines working document is the source of truth** for criteria, examples, tags, glossary, and
   acknowledgements. The chairs keep it as "MSF XR Accessibility Guidelines – Working Document", which is a
   [public Google Doc](https://docs.google.com/document/d/1wRHflVnJhRqZh6IvVAbWZGm0qXrkcJ2RxdRNaQjsMdY/edit?usp=sharing)
   that anyone can comment on. When the site or any summary disagrees with it, the working document wins. Don't silently
   "fix" criterion wording. Raise the difference instead.
   - An archived v1.0 snapshot exists (released early July 2026). The working document is the active v2.0 draft.
   - **Pending suggestions are not accepted text.** The working document holds many undecided suggested edits. A
     .docx export stores them as tracked changes, so simple text extraction mixes them in. Leave out insertions
     (`w:ins`) and keep deletions (`w:delText`) to get the accepted text. If you use a pending suggestion, say so.
2. **`xr-accessibility-guidelines-collection.md`** in this repo is an earlier upstream source, not the guidelines
   themselves. It is co-chair James Maki's compilation of other guidelines (Game Accessibility Guidelines, Meta
   VRCs, Xbox, Schell Games, and others). Copyright © 2024 James Maki.
3. **XR Access resources** may be used as supporting reference, but they don't override the working document:
   - [xraccessibility.github.io](https://github.com/XRAccessibility/xraccessibility.github.io), a curated
     resource index, licensed CC BY-SA 4.0;
   - [XR-Access-Initiative](https://github.com/XR-Access-Initiative) Unity toolkits, e.g. Chirp captions (MIT),
     the Vision Accessibility Toolkit (MIT), and the Locomotion Accessibility Toolkit (no license stated). Check
     each license before reusing code or text.
4. **External standards** are cited, never paraphrased into new requirements: WCAG 2.2/3.0, W3C XAUR, EN 301 549,
   the XRA Developer Guide (Ch. 3), and Game Accessibility Guidelines.

## Structure of the guidelines (from the working document)

- **Front matter:** Overview (Criteria, Examples, Glossary), Scope, Use of AI, Acknowledgements.
- **Accessibility Criteria**, grouped in topic › subtopic › criterion order:
  - **General:** System & Interface (Menus, Notifications, Error Prevention, …).
  - **Avatar.**
  - **Understanding:** Multimodal Feedback (Captions, Audio Descriptions, Sign Language, …) and Cognitive
    Accessibility.
  - **Navigation:** Virtual Motion, Points of Interest, Major Transitions.
  - **Interaction:** Physical Limitations, Input Methods, Focus, Timing & Difficulty.
  - **Comfort & Safety:** Physical and Mental.
- **Each criterion section** has these parts:
  - one or more ✅ statements;
  - a `Tags:` line;
  - `References:`.
  - ⭐ marks *experimental* statements: needs that are essential for full access but not yet widely
    implemented.
- **Tag dimensions:**
  - Practicality (Basic / Intermediate / Advanced);
  - Impact (Best Practice / Important / Critical);
  - Access Need (Vision, Hearing, Mobility/Physical, Cognitive, plus Speech, which appears in use);
  - Platform (VR / AR / MR);
  - Responsibility (Designer / Developer / Platform Owner);
  - conformance (**Requirement** / **Best Practice**).
  - Tag spelling and capitalization in the document are inconsistent.
  - Don't invent new tags.
  - How to normalize the tags is still to be decided.
- **Accessibility Examples:** real applications (e.g. Cosmonious High, Walkabout Mini Golf, The Last of Us
  Part II). Each example lists the criteria it meets. Grouped as Extended Reality / Other 3D Media.
- **Glossary:** still sparse. Match the [MSF Glossary](https://glossary.metaverse-standards.org/) and W3C
  definitions where possible.
- **Highlighted text, bracketed notes, and "[To add]"** in the working document are open questions. Carry them
  over as flagged drafts, not finished content.

## GitHub Pages site ("coming soon" page only)

- The guidelines will be published as a website on **GitHub Pages**, built from this repo.
- For now, Pages shows a "coming soon" page: `index.html` in the top folder. It links to the working document, the
  feedback form, the group page, and the draft demos and glossary. When you add or remove a demo, update it and its
  "last updated" date.
- Pages publishes from the `gh-pages` branch, which holds the same files as `main`. Pushing to `main` doesn't change the
  live site. To publish, push `main` to `gh-pages` with `git push origin main:gh-pages`. Never edit `gh-pages` directly.
- Ask before changing `gh-pages` or the Pages settings.
- `.nojekyll` makes Pages serve the files as they are, without building them.
- Don't copy planning documents into this repo, commits, PRs, issues, or any public material until Dylan
  authorizes it.
- **Don't build anything big yet.** That includes:
  - site scaffolding;
  - schemas and front matter field names;
  - criterion IDs;
  - migrating content.
  - The chairs are still reviewing comments on the working document, and design decisions such as field names
    need a group discussion first.
  - Small, reversible prototypes are fine when asked for.
- When the time comes, keep the content model independent of the site generator, and generate every output
  from a single source.

## Demos

- `demos/` holds small interactive demos of accessibility criteria. `demos/README.md` covers their status, ideas for
  more, and how to build and test them. It is a proposal that the working group has not approved.
- List the MSF criteria a demo covers first, from accepted text, and then WCAG.
- A demo shows one possible technique. It is never evidence of conformance.
- Say what has not been tested. Only a person can do the screen reader check.

## Parity with the Metaverse Standards Forum

Follow MSF conventions wherever MSF has published them.

- **Naming:**
  - Use "Metaverse Standards Forum" in full on first use, then "MSF".
  - In body text, call us the "Accessibility in the Metaverse Working Group". Titles can use "Accessibility in the
    Metaverse" alone. "Domain group" is only MSF's navigation and URL term.
- **Brand:**
  - Use the MSF logo only as supplied (horizontal, unaltered, approved colors) from the official logo pack.
  - Logo files are in `assets/msf/`: black text for light backgrounds, and white text for dark ones. Keep other text away
    from the logo.
  - MSF has published no color palette or fonts. Don't invent "official" brand values. Ask Dylan for the logo
    pack and user guide if they're needed.
- **Glossary:** reuse terms from the MSF Glossary
  ([site](https://glossary.metaverse-standards.org/),
  repo `MetaverseStandards/metaversestandards-glossary`) before defining new ones.
- **Contributions:** the MSF org states that non-members' pull requests are reviewed by Forum membership before
  being accepted. Contributing docs should say so.
- **Legal:**
  - MSF has published no license for documents. Its site terms are "© Metaverse Standards Forum, all rights
    reserved".
  - Don't add a LICENSE, copyright line, IPR statement, or disclaimer without Dylan's sign-off.
- **Group status:** the group is a subgroup of the 3D Assets Working Group.
  - Use this status even if another page describes the group differently.
  - Check with Dylan before writing new public descriptions of where the group sits in MSF.

## Content principles

Everything this group publishes must model the accessibility it argues for.

- **The site and other HTML** meet WCAG 2.2 AA at minimum. That means:
  - semantic landmarks and logical heading order;
  - meaningful alt text, or `alt=""` for decorative images;
  - sufficient contrast and visible focus;
  - full keyboard operation;
  - accessible search and filters, with results announced to screen readers;
  - support for `prefers-reduced-motion`;
  - no information carried by color alone;
  - captions or transcripts for media;
  - descriptive link text;
  - reflow at 320px and zoom to 200%.
  - Keep pages light: minimal client-side dependencies, and no unnecessary tracking or personal data.
- **Markdown:**
  - use real headings, not bold text;
  - give every image alt text;
  - use tables only for tabular data, with header rows;
  - use descriptive link text.
- **Documents and slides:**
  - use real heading and list structure;
  - give images alt text;
  - set a reading order;
  - don't put text inside images.
- **Writing:** plain language and short sentences. Define jargon and acronyms on first use. The audience is
  designers, developers, platform owners, auditors, product managers, policymakers, researchers, and disabled
  users.
- **Disability language:** follow the community's lead. Both person-first and identity-first language are fine
  (e.g. "Deaf", "disabled people"). Avoid "suffers from", "confined to a wheelchair", and "special needs".
- **Accuracy:**
  - Cite sources.
  - Never invent citations, statistics, examples, or standards language.
  - If unsure, say so and flag it for a chair to check.

## Public vs. member-only material

- This repo and the site are **public**.
- These stay out of public files unless a chair confirms they're cleared:
  - MSF Portal content and meeting notes;
  - member lists;
  - internal plans and drafts;
  - commenter names;
  - anything marked member-only.
  - Acknowledgements in the working document count as cleared once they appear in a released version.
- Don't publish personal contact details beyond the chair mailing list.

## Working with the files

- `xr-accessibility-guidelines-collection.md` is about 3,400 lines.
  - Use Grep and ranged reads.
  - Keep its numbering, `####` guideline headings, hand-kept TOC and GitHub anchors in step.
  - Keep every source citation.
  - Check with a chair before making substantive changes, since it's James's authored work.
- `README.md` is the GitHub landing page. Keep it consistent with the MSF group page, except for the group status,
  which follows "Group status" above.
  - Keep the charter link as it is for now.
  - The "Our main project" paragraph links to the public working document for now. Swap in the official site or
    the v1.0 archive once either one has a public URL.

## Workflow

- `main` must always be publishable. Use branches for unfinished work.
- For now, maintainers can push finished work straight to `main` without a PR. Everyone else uses a PR. Return to PRs
  for everyone once other people contribute regularly, or once the guidelines site publishes from `main`.
- Ask before pushing, opening PRs, publishing anything externally, or changing repo settings. This is a shared
  MSF organization repo.
- Every content change should be traceable to an issue, a PR, or a commit message that explains it. User-facing
  changes go in the changelog once one exists.
- Before any site or demo change reaches `main`, with or without a PR:
  - run the validation and build;
  - check accessibility (structure, contrast, keyboard, screen-reader names, zoom/reflow);
  - report the results.
