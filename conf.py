import random

# -- Project information
project = "ArviZ project"
author = "ArviZ contributors"
copyright = f"2022, {author}"

version = ""
release = version


# -- General configuration

extensions = [
    "sphinx.ext.intersphinx",
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_togglebutton",
]

exclude_patterns = ["Thumbs.db", ".DS_Store", ".ipynb_checkpoints", "README.md", "cards/*", ".github/**"]
templates_path = ["sphinx/_templates"]

# The reST default role (used for this markup: `text`) to use for all documents.
default_role = "code"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
locale_dirs = ["locale"]
gettext_uuid = True
gettext_compact = False
nb_render_priority = {"gettext": ()}

# -- Options for extensions

myst_enable_extensions = ["colon_fence", "deflist", "dollarmath", "amsmath", "attrs_block", "linkify"]
myst_linkify_fuzzy_links = False


# -- Options for HTML output

html_theme = "furo"
html_title = project
html_static_path = ["sphinx", "arviz_logos"]
html_css_files = [
    "custom.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css",
]
html_js_files = ["https://code.iconify.design/2/2.1.1/iconify.min.js"]
logo = "ArviZ.png"
html_favicon = "arviz_logos/favicon.ico"
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#0f718e",
        "color-brand-content": "#069fac",
    },
    "dark_css_variables": {
        "color-brand-primary": "#069fac",
        "color-brand-content": "#00c0bf",
    },
    "sidebar_hide_name": True,
    "light_logo": logo,
    "dark_logo": "ArviZ_white.png",
}
html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "ext_links.html",
        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",
        "sidebar/variant-selector.html",
    ]
}

intersphinx_mapping = {"arviz": ("https://python.arviz.org/en/latest/", None)}
