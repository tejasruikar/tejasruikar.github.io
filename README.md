# Tejas Ruikar - Personal Website

A static personal website built with [Pelican](https://getpelican.com/), featuring a blog, portfolio, and about page.

## Quick Start

### Prerequisites
- Python 3.10+

### Local Development

1. **Create and activate virtual environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Build the site:**
   ```powershell
   pelican content
   ```

4. **Serve locally:**
   ```powershell
   pelican --listen
   ```

5. Open http://localhost:8000 in your browser.

### Development with Auto-Reload

```powershell
pelican --listen --autoreload
```

## Project Structure

```
tejasruikar/
├── content/
│   ├── articles/      # Blog posts (Markdown)
│   ├── pages/         # Static pages (About, Portfolio)
│   └── images/        # Images and assets
├── themes/flavor/     # Custom theme
├── output/            # Generated site (gitignored)
├── pelicanconf.py     # Development config
├── publishconf.py     # Production config
└── requirements.txt   # Python dependencies
```

## Writing Content

### Blog Posts
Create a new `.md` file in `content/articles/`:

```markdown
Title: My New Post
Date: 2024-12-15
Category: Technology
Tags: python, web
Slug: my-new-post
Status: published
Summary: A brief description of the post.

Your content here...
```

### Pages
Create a new `.md` file in `content/pages/`:

```markdown
Title: Page Title
Slug: page-url
Status: published

Your page content here...
```

## Deployment

This site automatically deploys to GitHub Pages when you push to the `main` branch.

### Manual Deployment

```powershell
pelican content -s publishconf.py
```

## Configuration

- **pelicanconf.py**: Development settings
- **publishconf.py**: Production settings (extends pelicanconf.py)

## License

MIT License




