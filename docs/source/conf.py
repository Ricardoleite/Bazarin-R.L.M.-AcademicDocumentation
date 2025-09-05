# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import sphinx_rtd_theme
import sphinx_pdj_theme
import json
import re
import sphinx

sys.path.insert(0, os.path.abspath(".."))
sys.path.append(os.path.abspath('exts'))

project = 'Academic-Live-Documentation'
copyright = '2025, Ricardo LMB'
author = 'Ricardo LMB'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
comments_config = {'hypothesis': False, 'utterances': False}
bibtex_bibfiles = ['references.bib']
bibtex_encoding = 'latin'
bibtex_default_style = 'unsrt'
extensions = [    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    "sphinxemoji.sphinxemoji",
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_rtd_size',
    "nbsphinx",
    'nbsphinx_link',
    'sphinx_togglebutton',
    'sphinx_copybutton',
    'jupyter_book',
    'sphinx_thebe',
    'sphinx_comments',
    'sphinx.ext.intersphinx',
    'sphinx_design',
    'sphinx_jupyterbook_latex',
    "myst_nb",
    'sphinx.ext.graphviz',
    'sphinxcontrib.bibtex', 
    'sphinxcontrib.tikz']

myst_enable_extensions = [
    "html_admonition",
    "html_image",
    'dollarmath',
    'colon_fence',
    'linkify',
    'substitution',
    "deflist",
    'tasklist'
]

sphinx_rtd_size_width = "100%"
templates_path = ['_templates']
exclude_patterns = ['/source/Note-Cris/Gota-Plana','**.ipynb_checkpoints', '.DS_Store', 'Thumbs.db', '_build']
myst_url_schemes = ['mailto', 'http', 'https']
# nb_execution_allow_errors = False
# nb_execution_cache_path = ''
# nb_execution_excludepatterns = []
# nb_execution_in_temp = False
# nb_execution_mode = 'force'
# nb_execution_timeout = 30
# nb_output_stderr = 'show'
# suppress_warnings = ['myst.domains']
# use_jupyterbook_latex = True
# use_multitoc_numbering = True



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_css_files = [
    'css/eqno.css',
    'custom.css'
]

numfig_format = {'figure': 'Fig. %s', 'table': 'Table %s', 'code-block': 'Listing %s'}

# Show current build date in desired format
today_fmt = '%d/%B/%Y'   # e.g. 05/September/2025
