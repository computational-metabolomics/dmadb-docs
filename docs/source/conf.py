# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'DMAdb documentation'
copyright = '2024, University of Birmingham'
author = 'University of Birmingham'

release = '0.1'
version = '0.1.0'

import django
import os
import sys

sys.path.insert(0, os.path.abspath('../src'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'mogi.test_settings'
django.setup()

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
