# -*- coding: utf-8 -*-
#
# gimli documentation build configuration file, created by
# sphinx-quickstart on Wed Apr 11 16:37:21 2012.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os, pip

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))
sys.path.append(os.path.abspath('./_sphinx-ext'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.0'

# Check for external sphinx extensions
deps = ['pybtex', 'sphinxcontrib-programoutput', 'sphinxcontrib-bibtex', 'numpydoc']
modules = [str(m).rsplit()[0] for m in pip.get_installed_distributions()]

req = []
for dep in deps:
    if dep not in modules:
        req.append(dep)
if req:
    msg = "Sorry, there are missing dependencies to build the docs. Try: pip install %s." \
    % (' '.join(req))
    raise ImportError(msg)

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.todo',
              'sphinx.ext.doctest',
              'sphinx.ext.viewcode',
              'sphinx.ext.autosummary',
              'matplotlib.sphinxext.plot_directive',
              'matplotlib.sphinxext.only_directives',
              #'matplotlib.sphinxext.mathmpl',
              'myexec_directive',
              'myliterate_directive',
              'plot2rst',
              'sphinx.ext.mathjax',
              'doxylink'
              ]

extensions += [dep.replace('-','.') for dep in deps]

plot2rst_paths = [('doc/tutorials', 'doc/_tutorials_auto'),
                  ('doc/examples', 'doc/_examples_auto')]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'doc/index'

# General information about the project.
project = u'GIMLi'
copyright = u'2013, Carsten Rücker and Thomas Günther'

import pygimli as g

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = g.versionStr()
# The full version, including alpha/beta/rc tags.
release = g.versionStr()

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['doc/_build', 'doc/_sphinx-ext', 'doc/_templates', 'doc/examples', 'doc/tutorials', 'doc/tutorial']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_themes']

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'gimli'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}


# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "GIMLi - Geophysical Inversion and Modelling Library"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "GIMLi"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = '_static/resisnet.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/G.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y with ' + version

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = True

html_index = 'index.html'

# If false, no index is generated.
html_use_index = True

html_use_modindex = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True # does not have any affect. sphinx credit is located in footer.html

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'gimlidoc'
html_additional_pages = {'index': 'index.html'}


# -- Options for LaTeX output --------------------------------------------------

from os import environ, path

extradir = path.abspath( '_static' ).replace('\\','/')

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble':
    '\\usepackage{amsfonts}\
    \\usepackage{amssymb}\
    \\usepackage{bm}\
    \\usepackage{pslatex} \
    \\input{mylatex-commands.tex}'
}

pngmath_latex_preamble = '\
        \\usepackage{amsfonts}\
        \\usepackage{amssymb}\
        \\usepackage{bm}\
        \\usepackage{pslatex}\
        \\input{' + extradir+ '/mylatex-commands.tex}'

_mathpng_tempdir = './mathtmp'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('doc/index', 'gimli.tex', u'GIMLi Documentation', u'Carsten Rücker and Thomas Günther', 'manual'),
]

latex_additional_files = ['./_static/mylatex-commands.tex' ]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'GIMLi', u'GIMLi Documentation', [u'Carsten Rücker and Thomas Günther'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'GIMLi', u'GIMLi Documentation',
     u'Carsten Rücker and Thomas Günther', 'GIMLi',
     'Geophysical Inversion and Modeling Library', 'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
texinfo_show_urls = 'footnote'


# -- Options for pybtex output -------------------------------------------------
# load our plugins for manual bibstyle
import pkg_resources

for dist in pkg_resources.find_distributions("_templates/pybtex_plugins/"):
    pkg_resources.working_set.add(dist)

#End pybtex stuff

# -- Options for doxylink ------------------------------------------------------
doxylink = {
    'gimliapi' : ('doxygen/gimli.tag', 'doxygen/html/')
}

# TEMP: Show TODOS while building documentation
[extensions]
todo_include_todos = True
