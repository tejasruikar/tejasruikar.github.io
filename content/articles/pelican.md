Title: How this site is built?
Date: 2025-12-20
Category: General
Tags: pelican, static-site, github-pages, deployment
Slug: how-this-site-is-built
Status: published
Summary: A detailed look at how this personal website is built using Pelican and automatically deployed to GitHub Pages.

# How This Site is Built and Deployed

This website is a static site built with [Pelican](https://getpelican.com/), a Python-based static site generator. In this post, I'll walk you through the technology stack, build process, and automated deployment pipeline.

## Technology Stack

### Pelican Static Site Generator

I chose Pelican for several reasons:

- **Python-based**: Since I work with Python regularly, it's a natural fit
- **Markdown support**: All content is written in Markdown, making it easy to write and maintain
- **Flexible theming**: Custom themes allow for complete design control
- **Fast and secure**: Static sites are incredibly fast and have no server-side vulnerabilities
- **Version control friendly**: All content lives in Git, making it easy to track changes

### Project Structure

The site follows a standard Pelican structure:

```
tejasruikar/
├── content/
│   ├── articles/      # Blog posts (Markdown files)
│   ├── pages/         # Static pages (Home, About, etc.)
│   ├── images/        # Image assets
│   └── files/         # Static files (like resume.pdf)
├── themes/
│   └── minimal/       # Custom minimal theme
├── output/            # Generated HTML (gitignored)
├── pelicanconf.py     # Development configuration
├── publishconf.py     # Production configuration
└── requirements.txt   # Python dependencies
```

## Configuration

The site uses two configuration files:

### Development Configuration (`pelicanconf.py`)

The development config includes:

- **Site metadata**: Author name, site name, timezone
- **Content paths**: Where to find articles, pages, and static files
- **URL structure**: Custom URLs for articles (`/blog/{slug}.html`) and pages
- **Theme**: Uses a custom minimal theme
- **Relative URLs**: Enabled for local development
- **Social links**: GitHub, LinkedIn, and email

### Production Configuration (`publishconf.py`)

The production config extends the development config and adds:

- **Absolute URLs**: Sets `SITEURL` to `https://tejasruikar.github.io`
- **Feed generation**: Enables Atom feeds for RSS readers
- **Output cleanup**: Deletes the output directory before each build

## Build Process

### Local Development

For local development, I use:

```powershell
# Build the site
pelican content

# Serve with auto-reload
pelican --listen --autoreload
```

This generates the static site in the `output/` directory and serves it at `http://localhost:8000` with automatic reloading when files change.

### Production Build

For production builds, I use:

```powershell
pelican content -s publishconf.py
```

This uses the production configuration file, which sets the correct site URL and enables feeds.

## Automated Deployment

The site is automatically deployed to GitHub Pages using GitHub Actions. Here's how it works:

### GitHub Actions Workflow

The deployment workflow (`.github/workflows/deploy.yml`) consists of two jobs:

#### 1. Build Job

```yaml
- Checks out the repository
- Sets up Python 3.12
- Installs Pelican with Markdown support
- Builds the site using `publishconf.py`
- Uploads the output directory as an artifact
```

#### 2. Deploy Job

```yaml
- Deploys the artifact to GitHub Pages
- Runs only after the build job completes
- Uses GitHub's official Pages deployment action
```

### Deployment Triggers

The workflow runs automatically when:

- Code is pushed to the `master` branch
- The workflow is manually triggered via GitHub Actions UI

### Deployment Process

1. **Push to repository**: When I push changes to the `master` branch
2. **GitHub Actions triggers**: The workflow automatically starts
3. **Site builds**: Pelican generates the static HTML files
4. **Deployment**: The built site is deployed to GitHub Pages
5. **Site goes live**: Changes are visible at `https://tejasruikar.github.io` within minutes

## Content Management

### Writing Blog Posts

Blog posts are simple Markdown files in `content/articles/` with metadata at the top:

```markdown
Title: How this site is built?
Date: 2024-12-15
Category: General
Tags: pelican, static-site, github-pages
Slug: how-this-site-is-built
Status: published
Summary: A brief description...

# Content here in Markdown
```

### Static Pages

Pages like the home page are in `content/pages/` with similar metadata structure.

## Benefits of This Setup

1. **Fast deployment**: Changes go live within minutes of pushing to Git
2. **No server management**: GitHub Pages handles hosting
3. **Free hosting**: GitHub Pages is free for public repositories
4. **Version control**: All content and code changes are tracked in Git
5. **Easy content updates**: Just edit Markdown files and push
6. **Fast site**: Static sites load incredibly quickly
7. **Secure**: No server-side code means fewer attack vectors

## Future Improvements

Some potential enhancements I'm considering:

- Add a comment system (possibly using GitHub Discussions or Giscus)
- Implement a search functionality
- Add syntax highlighting for code blocks
- Create more custom theme features
- Add analytics (privacy-friendly options)

## Conclusion

This setup provides a simple, fast, and maintainable way to run a personal website and blog. The combination of Pelican, Markdown, and GitHub Pages creates a workflow that's both powerful and easy to use.

If you're interested in building a similar site, I'd recommend checking out the [Pelican documentation](https://docs.getpelican.com/) and the [GitHub Pages documentation](https://docs.github.com/en/pages).

---

*Questions or suggestions about this setup? Feel free to reach out!*
