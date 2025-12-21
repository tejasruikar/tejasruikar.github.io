"""Pelican configuration file for development."""

AUTHOR = 'Tejas Ruikar'
SITENAME = 'Tejas Ruikar'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'
DEFAULT_LANG = 'en'

# Content paths
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images', 'files']

# URL settings
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Blog index at /blog/
INDEX_SAVE_AS = 'blog/index.html'

# Feed generation (disabled during development)
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Navigation menu (pipe-separated in theme, like adamj.eu)
MENUITEMS = [
    ('Home', '/'),
    ('Blog', '/blog/'),
    ('Resume', '/files/resume.pdf'),
]

# Display pages in menu
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Pagination
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Theme - Minimal (inspired by adamj.eu)
THEME = 'themes/minimal'

# Social links
SOCIAL = [
    ('GitHub', 'https://github.com/tejasruikar'),
    ('LinkedIn', 'https://linkedin.com/in/tejasruikar'),
    ('Email', 'mailto:tejasruikar@live.com'),
]

# Markdown configuration
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# Extra metadata
DEFAULT_METADATA = {
    'status': 'draft',
}

