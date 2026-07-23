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

- **Quick Facts & Callout Boxes**: Use standard Material admonition syntax for key highlights, historical quotes, warnings, or tips:

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

### 4. GLightbox Asset Path Normalization

- **Relative Image Paths Rule**: Always use relative paths for Markdown images (`assets/images/filename.jpg` or `../assets/images/filename.jpg`). **NEVER use root-leading slashes** (`/assets/images/filename.jpg`).
- **Why**: `zensical.extensions.glightbox` constructs `<a class="glightbox" href="...">` anchors directly from `img.src`. A leading slash causes `href` to remain absolute (`/assets/images/...`), bypassing MkDocs' relative URL rewriter and breaking lightbox image modal previews on subpages.

### 5. Verification & Validation

- **Markdown Linting**: Run `pymarkdown --config .pymarkdownlnt.json scan <path/to/file.md>` to verify compliance (checking `MD009` trailing spaces, `MD022` heading blanks, and `MD032` list blanks).
- **Site Build**: Execute `mkdocs build` to verify that all Markdown extensions (admonitions, tables, superfences, glightbox) render correctly without build errors.
- **HTML Anchor Verification**: Inspect generated HTML in `site/<page>/index.html` to confirm that `<a class="glightbox">` `href` paths resolved to correct relative URLs (`../assets/images/...`).

## Common Pitfalls

- **Boundary Collisions & Duplicate Walls**: When editing full pages with multiple sections, replace large contiguous blocks carefully or perform a single coherent rewrite of the file content to prevent duplicating legacy text walls below the edited section.
- **Indentation in Admonitions**: All content inside an admonition box (lists, text, blockquotes) must be indented by exactly 4 spaces.
- **Preserving Details**: Ensure no original numbers, dates, place names, species, or technical terms are lost during reorganization.
- **Broken Markdown Link Syntax**: Watch for multi-line link targets or squished `[Link 1](a.md) [Link 2](b.md)` entries and format them into clean, separate list items or table rows.
