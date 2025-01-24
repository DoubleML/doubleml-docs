# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'DoubleML'
copyright = '2023, Bach, P., Chernozhukov, V., Klaassen, S., Kurz, M. S., and Spindler, M.'
author = 'Bach, P., Chernozhukov, V., Klaassen, S., Kurz, M. S., and Spindler, M.'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.graphviz',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
    'matplotlib.sphinxext.plot_directive',
    'nbsphinx',
    'sphinx_gallery.load_style',
    'sphinx_copybutton',
    'sphinx_design',
    'jupyter_sphinx',
]

# sphinx-panels shouldn't add bootstrap css since the pydata-sphinx-theme
# already loads it
panels_add_bootstrap_css = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'shared/*']

master_doc = 'index'

autoclass_content = 'class'
autosummary_generate = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    "navigation_with_keys": False,
    "header_links_before_dropdown": 6,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/DoubleML/doubleml-for-py",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/DoubleML/",
            "icon": "fa-solid fa-cube",
            "type": "fontawesome",
        },
    ],
}

# html_logo = '../img/logo.png'
html_extra_path = ['../img/logo.png', '../img/logo_dark.png']
html_favicon = '../img/favicon.ico'

html_sidebars = {'**': ['logo.html',
                        'search-field.html',
                        'sidebar-nav-bs.html'],
                 'workflow/workflow': ['logo.html',
                                       'search-field.html',
                                       'sidebar-nav-bs.html',
                                       'sidebar-doubleml-workflow.html'],
                 'guide/guide': ['logo.html',
                                 'search-field.html',
                                 'sidebar-nav-bs.html']}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['css/custom.css']

# -- Extension configuration -------------------------------------------------

nbsphinx_thumbnails = {
    'examples/py_double_ml_sensitivity': '_static/sensitivity_example_nb.png',
    'examples/py_double_ml_gate_sensitivity': '_static/sensitivity_example_nb.png',
    'examples/py_double_ml_firststage': '_static/firststage_example_nb.png',
    'examples/py_double_ml_basic_iv': '_static/basic_iv_example_nb.png',
    'examples/R_double_ml_basic_iv': '_static/basic_iv_example_nb.png',
    'examples/py_double_ml_ssm': '_static/ssm_example_nb.svg',
    'examples/py_double_ml_sensitivity_booking': '_static/dag_usecase_revised.png',
}

copybutton_prompt_text = r'>>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: | {2,5}\.\.\.\.:'
copybutton_prompt_is_regexp = True

# config of sphinx gallery for examples
nbsphinx_prolog = r"""
.. raw:: html
    {% raw %}
        <div class="admonition note">
        <p class="admonition-title">Note</p>
        <ul class="simple">
    {% endraw %}
    Download Jupyter notebook:
    {{ '<' }}a class={{ '"' }}reference external{{ '"' }} href={{ '"' }}https://docs.doubleml.org/stable/{{ env.doc2path(env.docname, base=None) }}{{ '"' }}{{ '>' }}https://docs.doubleml.org/stable/{{ env.doc2path(env.docname, base=None) }}{{ '</a>' }}.
    {% raw %}
        </ul>
        </div>
    {% endraw %}
"""

# intersphinx configuration
intersphinx_mapping = {
    'python': ('https://docs.python.org/{.major}'.format(sys.version_info), None),
    'sklearn': ('https://scikit-learn.org/stable/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    'statsmodels': ('https://www.statsmodels.org/stable/', None),
}

linkcheck_ignore = [
    # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.1093/ectj/utaa001',
    # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.1111/ectj.12097',
    # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.2307/2171802',
    # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.2307/1912705',
    # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.1093/ectj/utaa027',
    # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.1111/rssb.12026',
    # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.1111/rssa.12623',
    # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.1146/annurev-economics-012315-015826',
    # Valid DOI, Causes 418 Client Error: unknown for url:...
    'https://doi.org/10.1109/TIT.2014.2343629',
    # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.1093/ectj/utaa001',
    # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.1111/0034-6527.00321',
    # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.1016/j.jeconom.2020.06.003',
    # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.1080/07350015.2021.1895815',
    # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.1198/jbes.2010.07136',
    # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.1111/rssb.12348',
    # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.1145/3460231.3474231',
    # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://dl.acm.org/doi/10.1145/3447545.3451181',
    # Pipelines notebook has to be reworked
    'https://mlr3book.mlr-org.com/pipelines.html',
    # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.1080/07350015.2023.2271071',
    # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.1093/restud/rdt044',
    # Valid DOI; 'Connection aborted.', RemoteDisconnected ...
    'https://CRAN.R-project.org/package=mlr3learners',
    # Valid DOI (error not replicable), Causes 404 Client Error: Not Found for url:...
    'https://doi.org/10.1214/14-AOS1204',
    # Valid DOI (error not replicable), Causes 404 Client Error: Not Found for url:...
    'https://doi.org/10.1214/14-AOS1221',
    # Valid DOI (error not replicable), Causes 404 Client Error: Not Found for url:...
    'https://doi.org/10.1214/17-AOS1671',
    # Valid DOI (error not replicable), Causes 404 Client Error: Not Found for url:...
    'https://dx.doi.org/10.1214/13-AOS1161',
    # Valid DOI (error not replicable), Causes 404 Client Error: Not Found for url:...
    'https://dx.doi.org/10.1214/14-AOS1230',
    # Valid URL Failed to establish a new connection: [Errno 111] Connection refused' ...
    'https://glmnet.stanford.edu/',
    # Valid URL Failed to establish a new connection: [Errno 111] Connection refused' ...
    'https://glmnet.stanford.edu/index.html',
    # Valid URL Failed to establish a new connection: [Errno 111] Connection refused' ...
    'https://glmnet.stanford.edu/reference/cv.glmnet.html',
    # Valid URL (error not replicable), Causes 409 Client Error: Too Many Requests for url
    'http://dx.doi.org/10.2139/ssrn.3619201',
    # Valid URL, Causes ConnectTimeoutError
    'https://folia.unifr.ch/global/documents/306524',
    # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.1146/annurev-economics-051520-021409',
    # Valdi DOI; Causes 504 Server Error: Gateway Time-out for ...
    'https://doi.org/10.1017/CBO9781139060035.008'
]

# To execute R code via jupyter-execute one needs to install the R kernel for jupyter
# https://github.com/IRkernel/IRkernel

jupyter_execute_default_kernel = 'ir'
jupyter_sphinx_linenos = False

# option to disable the execution of notebooks
nbsphinx_execute = "auto"  # "auto" | "always" | "never"
