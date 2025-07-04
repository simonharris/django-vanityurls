# Configuration file for the Sphinx documentation builder.

# N. https://github.com/zostera/django-bootstrap5/blob/main/docs/conf.py

# -- Project information

project = 'Django VanityURLs'
copyright = '2025, Simon Harding'
author = 'Simon Harding <github@pointbeing.net>'

release = '2.0'
version = '2.0.0'

# -- General configuration

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
