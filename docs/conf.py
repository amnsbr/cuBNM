# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'cuBNM'
copyright = '2024, Amin Saberi'
author = 'Amin Saberi'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'autoapi.extension',
    'sphinx_rtd_theme'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for autoapi -----------------------------------------------------
autoapi_dirs = ['../src/cubnm']
autoapi_type = "python"
autoapi_python_class_content = "both"
autoapi_ignore = ["*_core*", "*_setup_flags*"]
autoapi_template_dir = '_autoapi_templates'
autoapi_options = [
    'members', 'undoc-members', 'show-inheritance', 
    'show-module-summary', 'special-members',
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {
    'logo_only': True,
    'display_version': True,
    'style_nav_header_background': 'black',
}
html_logo = '_static/logo_text_white.png'
html_css_files = [
    'css/custom.css',
]