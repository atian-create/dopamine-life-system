<div align="center">

# Dopamine Life System

### Turn your personal life system and creator account plan into a page worth sharing.

**Bright colors · Bold outlines · Sticker cards · Life and creative planning**

[中文](README.md) · [English](README_EN.md) · [Customize](docs/CUSTOMIZE.md) · [Prompts](prompts/README.md)

![Template home](docs/screenshots/01-home.png)

Two reusable templates developed from A Tian's life-system and seven-account planning pages.

Colorful cards, illustrated characters and clear sections, with public example content you can replace.

</div>

## Two templates

| Life system | Account planner |
| --- | --- |
| ![Life system desktop view](docs/screenshots/02-life-desktop.png) | ![Account planner desktop view](docs/screenshots/03-accounts-desktop.png) |
| Traits, energy, strengths, voice, boundaries, projects, obstacles and rhythm | Roles, audiences, purpose, series, shared themes, weekly scheduling and boundaries |
| [Chinese page](templates/life-system.html) · [English page](templates/life-system.en.html) | [Chinese page](templates/account-planner.html) · [English page](templates/account-planner.en.html) |

These links show source files on GitHub. Download the repository and open `index_en.html` to browse the pages, or enable GitHub Pages for an online version.

## Highlights

- **Make planning enjoyable.** A cream dot-grid background, saturated colors, bold outlines and hard shadows turn long documents into a visual map.
- **Keep your own character.** Reflect on real experiences, energy and boundaries without forcing yourself into a fixed persona.
- **Give accounts distinct roles.** Four content lanes and seven example accounts, each with an audience, recurring series, production approach and exclusions.
- **Fully bilingual pages.** Both templates and READMEs have Chinese and English versions, with direct language links.
- **Open, edit and share.** No runtime dependencies, login or backend. Ready-made HTML opens locally and works on static hosting.
- **Reusable AI prompts included.** Combine your own records with the structure and visual brief to create a new version.

## Details

![Life-system making loop and energy map](docs/screenshots/06-life-detail.png)

![Account role map](docs/screenshots/07-account-map.png)

<details>
<summary>Account detail, English page and mobile views</summary>

![Account series and production notes](docs/screenshots/08-account-detail.png)

![English life system](docs/screenshots/04-life-english.png)

<img src="docs/screenshots/09-life-mobile.png" alt="Life system mobile view" width="300">
<img src="docs/screenshots/10-accounts-mobile.png" alt="Account planner mobile view" width="300">

</details>

## Get started

1. Download and extract the repository ZIP.
2. Open `index_en.html` and choose a template. The Chinese entry is `index.html`.
3. Edit the HTML directly, or give the [prompts](prompts/README.md) and sample page to AI and replace the content with your own records.
4. For structured maintenance, edit the JSON files in `data/`, then run:

```sh
python3 scripts/build.py
```

Optional local preview:

```sh
python3 -m http.server 8000
```

Visit `http://localhost:8000`. Each template also offers a Print / PDF button.

## What to prepare

| Life system | Account planner |
| --- | --- |
| Introduction, actual experiences, language habits, energy sources, boundaries, projects and routines | Account names, audiences, purposes, recurring series, sample topics, formats, frequency and roles |

Leave unavailable information blank. Do not invent achievements, revenue, followers or psychological traits to fill the layout. Lin, projects, series and schedules are fictional examples. The original pages' pricing, exclusive partnership details and unpublished product plans are not included.

## Visual style

A useful description is **dopamine colors + Neo-brutalist outlines and hard shadows + illustrated sticker-style editorial layouts**.

These are combined visual traits, not a strict movement you need to follow. See [design notes](docs/DESIGN.md) for the palette and layout.

## Structure

```text
├── index.html / index_en.html          # Bilingual entry points
├── templates/                         # Two templates, in both languages
├── data/                              # Editable bilingual sample content
├── assets/                            # Styles and illustrations
├── prompts/                           # Life, account and visual prompts
├── scripts/build.py                   # Standard-library static generator
└── docs/                              # Customization, design and screenshots
```

The optional ZCOOL KuaiLe font loads through Google Fonts. Offline pages fall back to system fonts; images and styles are included locally. The pages collect no personal data, call no AI API and do not automatically analyze your records.

## Hosting and contributions

For GitHub Pages, select **Settings → Pages → Deploy from a branch → main → / (root)**. Other static hosts work too.

Contributions to responsive layouts, print styles, translations, template structure and accessibility are welcome. Regenerate pages after editing sample data to keep `data/` and `templates/` aligned.

Code, templates and included example resources use the [MIT License](LICENSE). Replace the example illustrations and names when creating your own personal introduction.
