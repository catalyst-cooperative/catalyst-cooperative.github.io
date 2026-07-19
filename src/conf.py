# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import datetime

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Catalyst Cooperative"
copyright = (  # noqa: A001
    f"2016-{datetime.date.today().year}, Catalyst Cooperative, CC-BY-4.0"
)
author = "Catalyst Cooperative"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_logo = "_static/catalyst_logo-200x200.png"
html_icon = "_static/favicon.ico"
html_static_path = ["_static"]
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/catalyst-cooperative",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        },
        {
            "name": "Mastodon",
            "url": "https://mastodon.energy/@catalystcoop",
            "icon": "fa-brands fa-mastodon",
            "type": "fontawesome",
        },
        {
            "name": "Bluesky",
            "url": "https://bsky.app/profile/catalyst.coop",
            "icon": "fa-brands fa-bluesky",
            "type": "fontawesome",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/company/catalyst-cooperative/",
            "icon": "fa-brands fa-linkedin",
            "type": "fontawesome",
        },
        {
            "name": "Support Catalyst Cooperative",
            "url": "https://opencollective.com/pudl",
            "icon": "fa-solid fa-donate",
            "type": "fontawesome",
        },
    ],
}
