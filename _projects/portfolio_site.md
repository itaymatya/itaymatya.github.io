---
layout: page
title: Personal Portfolio Website
description: Building my personal academic portfolio using Jekyll and al-folio theme
img: assets/img/portfolio/portfolio screen shot.png
importance: 1
category: work
---

# Creating My Academic Portfolio Website

### Biggest lesson (highlight)

THE BIGGEST LESSON FROM THIS PROJECT IS: ALWAYS CONSULT THE DOCUMENTATION — check Jekyll, al-folio, and GitHub Pages docs when you hit problems. Documentation will often point to exact config options, required plugins, and breaking changes in deployment.

## Project Overview

This project documents the creation of my personal academic portfolio website using Jekyll and the al-folio theme. The site serves as a platform to showcase my academic work, projects, publications, and professional experience.

## Technologies Used

- Jekyll static site generator
- al-folio theme
- GitHub Pages for hosting
- Ruby and Bundler for development
- YAML for configuration
- Markdown for content
- Liquid templating

## Key Implementation Steps

### 1. Initial Setup

```bash
# Clone the al-folio template
git clone https://github.com/alshedivat/al-folio.git
cd al-folio
```

### 2. Configuration Customization

One of the first tasks was customizing the site's configuration in `_config.yml`:

```yaml
title: blank
first_name: Itay
middle_name:
last_name: Matya
email: # your email
description: >
  A personal academic portfolio showcasing my work and research.
```

### 3. Social Media Integration

Modified `_data/socials.yml` to integrate my professional social media profiles:

```yaml
- platform: github
  user_url: "https://github.com/itaymatya"
  icon: fab fa-github
```

### 4. Content Organization

The site's content is organized into several key sections:

- About page (`_pages/about.md`)
- Projects (`_projects/`)
- Blog posts (`_posts/`)
- Publications (`_pages/publications.md`)

### 5. Custom Styling

Added custom styling adjustments to enhance the theme's appearance while maintaining its professional look.

## Challenges and Solutions

### Challenge 1: YAML Syntax

Initially encountered issues with YAML syntax in configuration files. Resolved by ensuring proper indentation and learning YAML's block scalar styles.

Before:

```yaml
# Incorrect
contact_note: >
You can even add a little note about which of these is the best way to reach you.
```

After:

```yaml
# Correct
contact_note: >
  You can even add a little note about which of these is the best way to reach you.
```

### Challenge 2: Image Management

Implemented an organized structure for managing project images and assets:

```
assets/
  ├── img/
  │   ├── portfolio/
  │   └── projects/
  └── pdf/
```

## Key Features

1. Responsive design that works on all devices
2. Blog functionality for sharing updates and articles
3. Project portfolio with categorization
4. Publication listing with BibTeX integration
5. Easy-to-maintain architecture

## Future Enhancements

- Implement dark mode toggle
- Add more interactive elements
- Integrate with additional academic services
- Enhance SEO optimization

## Technical Documentation

### Local Development

To run the site locally:

```bash
bundle install
bundle exec jekyll serve
```

### Deployment

The site is automatically deployed to GitHub Pages when changes are pushed to the main branch.

## Learning Outcomes

- Deep understanding of Jekyll and static site generators
- Experience with GitHub Pages deployment
- YAML and Markdown proficiency
- Git workflow improvements
- Web development best practices

## Difficulties & Lessons (what I had to learn)

### Deployment changes and GitHub updates

Over time GitHub has changed how Pages build and deploy sites. The important differences I ran into while setting this site up were:

- GitHub Actions vs. built-in Pages: older guides assume Pages will build with `jekyll` automatically, while today many projects use a GitHub Actions workflow to run `bundle install` and `bundle exec jekyll build` in a controlled environment. That means you may need to add a `.github/workflows/` workflow file and ensure the correct Ruby version and system packages (for example `imagemagick`) are installed in the runner.
- System dependencies: image processing (responsive WebP generation) requires ImageMagick to be installed in the build environment. On GitHub Actions you usually add an `apt-get` step, for example:

```yaml
- name: Install system deps
  run: sudo apt-get update && sudo apt-get install -y imagemagick
```

- File paths and case-sensitivity: GitHub Pages build runners (Linux) are case-sensitive. Make sure your image filenames and references match exactly (including spaces, dashes, and extensions).

### Required languages, file types and syntaxes you should be familiar with

Given you have only an intro course in Python, here's a short list of the additional languages and file types you'll encounter and what they are used for in this project:

- YAML (`.yml`, `.yaml`) — configuration for Jekyll and data files in `_data/`. Learn indentation and block scalars (`|` and `>`).
- Markdown (`.md`) — writing pages and posts. Learn front matter (the top `---` block) and basic Markdown syntax.
- Liquid templates (`.liquid`) — Jekyll's templating language used in `_layouts/` and `_includes/`. You'll see tags like {% raw %}{% for %}{% endraw %} and {% raw %}{{ variable }}{% endraw %}. It's similar to basic Python templating but with its own filters and logic.
- HTML/CSS — small edits for layout or style changes, typically in `_includes/`, `_layouts/` and `_sass/`.
- Ruby / Bundler (`Gemfile`, `bundle`) — you don't need to write Ruby for the site, but you will run `bundle install` to get Jekyll and plugins. Reading the `Gemfile` helps understand plugin versions.
- JavaScript (`.js`) — used for interactive features. Usually you won't need deep JS knowledge but basic debugging in the browser devtools helps.
- JSON (`.json`) — resume data is loaded via `jekyll_get_json` (see `assets/json/resume.json`). Knowing JSON structure helps when editing resume contents.
- Images and binary files (`.jpg`, `.png`, `.webp`, `.pdf`) — know where to place them (e.g., `assets/img/`, `assets/pdf/`) and how the build will transform them.

### Practical tips for someone with a Python intro-course background

- Use Python strengths (file editing, small scripts) to automate repetitive tasks (for example, generating JSON resume entries or batch-renaming images). A tiny Python script can help validate YAML/JSON before committing.
- Learn to run local builds: `bundle exec jekyll serve` and check `_site/` output. This is faster for debugging than relying on GitHub Actions alone.
- Use browser DevTools to inspect the generated nav bar and confirm whether a page link exists but is hidden by CSS.
- If an image or file is missing during a CI build, check the action logs for `No such file or directory` and verify case and path.

## Resources and References

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [al-folio Theme Documentation](https://github.com/alshedivat/al-folio)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
