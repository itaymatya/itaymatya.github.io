---
layout: page
title: Personal Portfolio Website
description: Building my personal academic portfolio using Jekyll and al-folio theme
img: ""
importance: 1
category: work
---

# Creating My Academic Portfolio Website

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

## Resources and References
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [al-folio Theme Documentation](https://github.com/alshedivat/al-folio)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)