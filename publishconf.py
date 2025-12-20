"""Pelican configuration file for production/publishing."""

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# Production URL - GitHub Pages user site
SITEURL = 'https://tejasruikar.github.io'
RELATIVE_URLS = False

# Enable feeds in production
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True




