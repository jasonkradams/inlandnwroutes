---
name: zensical-page-reorganizer
description: >
  Reorganizes, restructures, and enhances run-on Markdown documentation pages
  or sections in Zensical / Material for MkDocs projects with structured
  headings (h2/h3/h4), Material callouts (admonitions), summary tables,
  GLightbox asset path normalization, and strict pymarkdown lint verification.
---

# Zensical Page & Section Reorganizer

## Overview

This skill provides a systematic workflow for refactoring unorganized, run-on, or wall-of-text pages and sections in MkDocs / Zensical documentation projects. It transforms legacy or squished text into clean, accessible, visually rich documentation using structured heading hierarchies, Material admonitions, summary tables, GLightbox image path normalization, and strict lint validation.

## Workflow

### 1. Content Audit & Full Page Parsing

- **Complete Page Reading**: Read the entire target file using `view_file` before making any edits to understand the overall page structure, heading hierarchy, and section boundaries.
- **Unsquish Concatenated Text**: Scan for inline headings or text blocks that were accidentally concatenated into paragraph text (e.g., `...natural beauty. Access The Washington portion...` or `...you wish to visit. Geology The Priest Lake...`).
- **Clean Invisible Characters**: Check for and strip hidden Unicode artifacts like zero-width spaces (`\u200b`), non-breaking spaces, or broken line breaks inside Markdown links (e.g., `trail #\n59]`).
- **Frontmatter & Notes Consolidation**: Audit YAML frontmatter. Legacy pages often split a single note entry into two separate array items (e.g., `- Forest Service Alerts` followed by `- <https://...>` or `h[ttps://...`). Combine these split items into a single, clean Markdown link item (e.g., `- "[Forest Service Alerts](https://...)"`).
- **Thematic Grouping**: Categorize content into logical sections and sub-topics (e.g., Geography & Topography, Land Management, Access, Geology, Cultural History, Climate & Vegetation, Wildlife, Alpine Lakes & Camping, Route Index).

### 2. Structural Hierarchy (`h1`, `h2`, `h3`, `h4`)

- Maintain a single top-level page title (`# Page Title`).
- Use level 2 headings (`## Main Section Title`) for primary thematic divisions.
- Use level 3 headings (`### Sub-topic`) for secondary divisions.
- Use level 4 headings (`#### Detailed Topic`) for nested sub-topics within major divisions.
- **Blank Line Rule**: Ensure every heading is separated by a blank line above and below to pass Markdown linting (`MD022`). Never duplicate heading lines consecutively.

### 3. Visual & Rich Enhancements (Material for MkDocs / Zensical)

- **Automatic Frontmatter Rendering vs. In-Body Duplication**:
  `overrides/main.html` automatically extracts and renders `stats:`, `notes:`, and `tags:` from YAML frontmatter into top-of-page callout boxes ("Quick Facts & Trip Stats", "Forest Alerts & Important Notes"). **DO NOT hand-write redundant `!!! info "Quick Facts..."` boxes in the Markdown body if `stats:` is already defined in frontmatter**, as this causes the Quick Facts box to render twice.

- **Admonition Box Indentation & Blank Lines**:
  All content inside an admonition box (`!!! info ...`, `!!! warning ...`, `!!! quote ...`) MUST be indented by 4 spaces (`    `) on every line, and preceded by a blank line inside the callout block if it starts a list (to satisfy `MD032` linting).

  ```markdown
  !!! info "Quick Facts: [Subject]"

      - **Fact 1:** Details
      - **Fact 2:** Details

  !!! quote "Historical Quote"
      Quote content indented by 4 spaces.

  !!! warning "Wildfire History"
      Warning content indented by 4 spaces.
  ```

- **Summary & Route Tables**: Convert lists of route links, mountain peaks, elevation zones, or jurisdiction managers into structured Markdown tables:

  ```markdown
  | Destination / Peak | Elevation / Trail Details | Route Guide Link |
  | :--- | :--- | :--- |
  | **Beehive Lake** | 6,457' (Trail #279) | [Beehive Lake Guide](beehive-lake-6457.md) |
  ```

- **Bulleted Lists**: Group key statistics or boundary descriptions into bulleted lists. Ensure lists have preceding and succeeding blank lines (`MD032`).

### 4. Image Formatting & GLightbox Asset Normalization

- **Accessibility & Caption Synchronization**:
  - Format images using standard Markdown image syntax with an italicized caption paragraph directly beneath:

    ```markdown
    ![Hikers navigating the boulder route toward Hunt Lake](assets/images/p620.png)
    _Hikers navigating the boulder route toward Hunt Lake._
    ```

  - **Identical Alt & Caption Text Rule**: Ensure the image `alt` text (`![Alt text]`) matches the italicized caption (`_Caption text_`) below the image. This guarantees:
    1. **a11y Compliance**: Assistive screen readers receive full descriptive alt text on the `<img>` tag.
    2. **Lightbox Title**: `zensical.extensions.glightbox` (`auto_caption: true`) extracts the `alt` text to populate `data-title` in the GLightbox modal viewer.
    3. **Page Display**: The exact caption text renders on the web page in italics directly below the image.

- **Relative Image Paths Rule**: Always use relative paths for Markdown images (`assets/images/filename.jpg` or `../assets/images/filename.jpg`). **NEVER use root-leading slashes** (`/assets/images/filename.jpg`).
- **Why**: `zensical.extensions.glightbox` constructs `<a class="glightbox" href="...">` anchors directly from `img.src`. A leading slash causes `href` to remain absolute (`/assets/images/...`), bypassing MkDocs' relative URL rewriter and breaking lightbox image modal previews on subpages.

### 5. Blog Post Detection & Specialized Formatting

When reorganizing a page identified as a blog post (located in `docs/blog/`, `docs/blog/posts/`, or containing blog frontmatter / title `Blog #...`):

- **Blog Detection**:
  - File path is inside `docs/blog/` or `docs/blog/posts/`.
  - Page contains YAML frontmatter (`date:`, `authors:`, `categories:`).
  - Title begins with `Blog #...` or `BLOG #...`.

- **Plugin-Driven YAML Frontmatter (No Inline HTML)**:
  Metadata (`title`, `date`, `authors`, `categories`) must reside exclusively in standard YAML frontmatter at the top of the post file. **DO NOT add custom inline HTML banners** (`<div class="blog-meta">`) or manual metadata markup to the post body. All frontmatter elements (author avatars, author profile links, categories badges, dates, estimated read time) are rendered site-wide through the `blog:` plugin configuration in `mkdocs.yml`:
  ```yaml
  plugins:
    - blog:
        blog_dir: blog
        authors: true
        authors_file: blog/.authors.yml
        authors_profiles: true
        categories: true
        archive: true
        post_date_format: MMMM d, yyyy
        post_readtime: true
        post_excerpt: optional
        post_excerpt_max_authors: 2
  ```

  Example YAML Frontmatter:
  ```yaml
  ---
  title: "Blog #12: Geology, Geography, and History"
  date: 2023-07-06
  authors:
    - chic
    - david
  categories:
    - Geology & History
  ---
  ```

- **Preserve Original Authors' Prose**:
  Do **NOT** rewrite, paraphrase, or alter the authors' original body prose. The wording, tone, and voice must remain strictly faithful to the original content.

- **Excerpt Separator (`<!-- more -->`)**:
  Insert `<!-- more -->` directly after the initial introductory paragraph so blog indexers and card feeds extract clean summaries.

- **Author Signature & Scraped Artifact Cleanup**:
  - Fix duplicated author footers (e.g., change `Chic Burge    Chic Burge` to a single clean citation line `Chic Burge    David Crafton`).
  - Strip raw website footers (`InlandNWRoutes.com`), scraped comment markers (`[0 Comments]`), and reply forms (`### Leave a Reply.`).

### 6. Verification & Validation

- **Non-Destructive File-Level & Project Markdown Linting**: Run `just lint` (or `./scripts/lint.sh <file.md>`) against every single file touched during reorganization to verify strict compliance (`MD009` trailing spaces, `MD013` line length <= 120, `MD022` heading blanks, `MD032` list blanks, `MD041` first line heading, `MD047` single trailing newline).
- **Read-Only Scanner Guarantee**: Linting commands MUST run as pure, read-only scanners (`pymarkdown scan`). Never execute mutating regex pre-processors or destructive legacy scripts (`cleanup_markdown.py`) during lint runs.
- **Site Build**: Execute `just build` or `mkdocs build` to verify that all Markdown extensions (admonitions, tables, superfences, glightbox) render correctly without build errors.
- **HTML Anchor Verification**: Inspect generated HTML in `site/<page>/index.html` to confirm that `<a class="glightbox">` `href` paths resolved to correct relative URLs (`../assets/images/...`).

## Common Pitfalls

- **Duplicate Quick Facts Boxes**: Do not duplicate `stats:` frontmatter inside the Markdown body as a `!!! info "Quick Facts..."` box, since `overrides/main.html` renders `stats:` automatically.
- **Indentation & Line Formatting in Admonitions**: All content inside an admonition box (lists, text, blockquotes) must be indented by exactly 4 spaces (`    `) on every line, and preceded by a blank line inside the callout block if it starts a list.
- **Markdown Link Protection**: Line-wrapping tools must protect Markdown link tags (`[Anchor](URL)`) using exact-length dummy tokens so link anchors or URLs are never split across line breaks.
- **Destructive Pre-processors**: Avoid invoking file-rewriting scripts during lint checks. Use `scripts/reorganize_all_docs.py` for structured formatting and keep linting strictly read-only.
- **Boundary Collisions & Duplicate Walls**: When editing full pages with multiple sections, replace large contiguous blocks carefully or perform a single coherent rewrite of the file content to prevent duplicating legacy text walls below the edited section.
- **Preserving Details**: Ensure no original numbers, dates, place names, species, or technical terms are lost during reorganization.
