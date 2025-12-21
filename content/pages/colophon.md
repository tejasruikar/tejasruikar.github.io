Title: Colophon
Slug: colophon
Status: published

# Colophon

This website is built using modern static site generation tools and technologies. Here's how it all comes together:

## Static Site Generator

**Pelican** — A Python-based static site generator that transforms Markdown files into a beautiful static website. This site uses Pelican 4.11.0.

## Content

- **Markdown** — All content is written in Markdown, making it easy to write and maintain
- **Python** — The site is built using Python 3.12

## Theme

**Minimal Theme** — A custom minimal theme inspired by clean, content-first design principles. The theme emphasizes readability and simplicity.

## Development Tools

- **Invoke** — Task automation for building and deploying the site
- **ghp-import** — Tool for deploying to GitHub Pages

## Hosting

**GitHub Pages** — The site is automatically deployed to GitHub Pages using GitHub Actions. Every push to the repository triggers a rebuild and deployment.

## Build Process

1. Content is written in Markdown files in the `content/` directory
2. Pelican processes the Markdown and generates static HTML files
3. GitHub Actions automatically builds and deploys the site on every push
4. The site is served via GitHub Pages at `https://tejasruikar.github.io`

## Source Code

The source code for this website is available on [GitHub](https://github.com/tejasruikar/tejasruikar.github.io).

---

*Last updated: Built with Pelican 4.11.0*
