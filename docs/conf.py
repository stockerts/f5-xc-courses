# Configuration file for the Sphinx documentation builder.
# -- Project information

project = 'F5 Distributed Cloud'
copyright = '2025'
author = 'F5'

#release = '0.1'
#version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    "sphinx_copybutton"
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

#templates_path = ['_templates']

# JS Path
html_static_path = ['_static']

def setup(app):
    app.add_js_file('custom.js')


# -- Options for HTML output
#
html_theme = 'piccolo_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

#html_css_files = ['theme_overrides.css']

# If true, "Created using Sphinx" is shown in the HTML footer. The default is True.
#
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#
html_show_copyright = False

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
#html_logo = "docs/images/f5-logo-solid-rgb_small.png"

# A shorter title for the navigation bar.  Default is the same as html_title.
#
#html_short_title = "Home"

# -- Options for EPUB output
epub_show_urls = 'footnote'