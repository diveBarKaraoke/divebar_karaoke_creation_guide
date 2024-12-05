# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'diveBar Karaoke Creation Guide'
html_title = project
copyright = '2024, diveBar Karaoke Community'
author = 'diveBar Karaoke Community'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

#root_doc = 'contents'

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx_design',
    'sphinxcontrib.youtube',
    'sphinxext.opengraph',
    'sphinx_favicon'
]
autosectionlabel_prefix_document = True

ogp_site_url='https://docs.divebar.me/'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']

html_logo = 'images/logo.png'
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'style_nav_header_background': '#000000'
}
html_css_files = [
    'css/custom.css'
]
html_context = {
    'github_repo': 'diveBarKaraoke/divebar_karaoke_creation_guide',
    'github_version': 'main',
    'conf_py_path': '/docs/',
    'display_github': True
}
favicons = [
    {"href": "favicon.ico"},
    {"href": "favicon-160x160.png"},
    {"href": "favicon-android-192x192.png"},
    {"href": "favicon-ios-180x180.png", "rel": "apple-touch-icon"}
]
