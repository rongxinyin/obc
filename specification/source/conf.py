# -*- coding: utf-8 -*-
#
# Documentation build configuration file, created by
# sphinx-quickstart on Wed Jun  1 22:56:43 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
#extensions = ['sphinx.ext.autodoc', 'sphinx.ext.pngmath']
extensions = ['sphinxcontrib.bibtex', \
              'sphinx.ext.autodoc', 'mathjax', \
              'sphinxcontrib.plantuml', 'sphinx.ext.todo']

# mathjax_path is based on http://www.mathjax.org/docs/2.0/start.html
mathjax_path = "https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"

plantuml = 'java -jar plantuml.jar'
plantuml_output_format = 'svg'
plantuml_latex_output_format = 'pdf'

todo_include_todos = True

# 'sphinxcontrib.bibtex' is based on http://sphinxcontrib-bibtex.readthedocs.org/en/latest/quickstart.html
# which may be installed using
#   pip install sphinxcontrib-bibtex

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Open Building Control'
copyright = u'(c) All rights reserved'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []
exclude_patterns = ['templates']
# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
#html_theme = 'sphinxdoc'

import sphinx_bootstrap_theme
# Activate the theme.
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
print "*********** {}".format(html_theme_path)
html_logo = '_static/cdl-logo.png'
# Theme options are theme-specific and customize the look and feel of a
# theme further.
html_theme_options = {
    # Navigation bar title. (Default: ``project`` value)
    'navbar_title': " ", # Leave an empty space to avoid title under image.

    # Tab name for entire site. (Default: "Site")
    'navbar_site_name': "Site",

    # A list of tuples containing pages or urls to link to.
    # Valid tuples should be in the following forms:
    #    (name, page)                 # a link to a page
    #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
    #    (name, "http://example.com", True) # arbitrary absolute url
    # Note the "1" or "True" value above as the third argument to indicate
    # an arbitrary url.
    'navbar_links': [
        ("Home", "http://obc.lbl.gov", True),
        ("Table of Contents", "index"),
#        ("Download", "download"),
#        ("Python", "http://simulationresearch.lbl.gov/modelica/buildingspy", True),
#        ("Development", "https://github.com/lbl-srg/modelica-buildings", True),
#        ("Publications", "publications"),
#        ("Help", "help"),
    ],

#    'navbar_links': [
#        ("Examples", "examples"),
#        ("Link", "http://example.com", True),
#    ],

    # Render the next and previous page links in navbar. (Default: true)
    'navbar_sidebarrel': True,

    # Render the current pages TOC in the navbar. (Default: true)
    'navbar_pagenav': True,

    # Tab name for the current pages TOC. (Default: "Page")
    'navbar_pagenav_name': "Page",

    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    'globaltoc_depth': 2,

    # Include hidden TOCs in Site navbar?
    #
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    #
    # Values: "true" (default) or "false"
    'globaltoc_includehidden': "true",

    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': "navbar",

    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "false",

    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    'source_link_position': "footer",

    # Bootswatch (http://bootswatch.com/) theme.
    #
    # Options are nothing (default) or the name of a valid theme
    # such as "amelia" or "cosmo".
    'bootswatch_theme': "united",

    # Choose Bootstrap version.
    # Values: "3" (default) or "2" (in quotes)
    'bootstrap_version': "3",
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Control Description Language"

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.


# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/lbl-icon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'Documentation'

#supported_image_types = ['image/svg+xml', 'image/png', 'image/gif', 'image/jpeg']
supported_image_types = ['image/svg+xml', 'image/png', 'image/gif', 'image/jpeg']

# Number figures in html output
numfig = True

# -- Options for LaTeX output --------------------------------------------------


latex_additional_files = ['_static/latex-note.png', '_static/latex-warning.png']

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index',
   'cdl_report.tex',
   u'Control Description Language',
   '', 'manual'),
]


##latex_elements = {'fontpkg': '\\usepackage[scaled]{helvet}',
##                  'fontpkg': '\\renewcommand*\\familydefault{\\sfdefault}'}
#'classoptions': ',openany'                        : remove blank pages in PDF.
#'babel': '\\usepackage[english]{babel}'           : suppress error message caused by undefined language.
#'maketitle': '\\pagenumbering{gobble}\\maketitle' : switch off the page numbering in the tile and the index.
release = ''
latex_elements = {'classoptions': ', openany',         # remove blank pages in PDF.
                   'releasename': '',
                  'babel': '\\usepackage[english]{babel}'}



#                 'fontpkg': '\\usepackage[scaled]{helvet}'

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = '_static/cdl-logo.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = False

# Additional stuff for the LaTeX preamble.
latex_elements['preamble'] = r'''
% The pdf output has too large picture compared to the html output.
% The next statement reduces the figure size
\pdfpxdimen=0.75\sphinxpxdimen

% Format of chapter fonts
\makeatletter
\ChNameVar{\raggedleft\sf\bfseries\Large} % sets the style for name
\ChNumVar{\raggedleft\sf\bfseries\Large} % sets the style for name
\ChTitleVar{\raggedleft\sf\bfseries\Large} % sets the style for name
\makeatother


\usepackage[scaled]{helvet}
\usepackage[helvet]{sfmath}

%% Fontsizes according to guideline from Andreas Eckmanns, Aug. 2018
\usepackage{sectsty}
\chapterfont{\fontsize{24}{26}\selectfont}
\sectionfont{\fontsize{14}{16}\selectfont}
\subsectionfont{\fontsize{12}{14}\selectfont}

%\usepackage[T1]{fontenc}
%%\titleformat*{\chapter}{\fontencoding{OT1}\fontfamily{cmr}\fontseries{m}%
%%  \fontshape{n}\fontsize{24pt}{24}\selectfont}
%%\titleformat*{\section}{\fontencoding{OT1}\fontfamily{cmr}\fontseries{m}%
%%  \fontshape{n}\fontsize{6pt}{6}\selectfont}
%%\titleformat*{\subsection}{\fontencoding{OT1}\fontfamily{cmr}\fontseries{m}%
%%  \fontshape{n}\fontsize{12pt}{12}\selectfont}
%%\titleformat*{\subsubsection}{\fontencoding{OT1}\fontfamily{cmr}\fontseries{m}%
%%  \fontshape{n}\fontsize{11pt}{11}\selectfont}
\titleformat*{\paragraph}
  {\rmfamily\slshape}
  {}{}{}
  \titlespacing{\paragraph}
  {0pc}{1.5ex minus .1 ex}{0pc}

\renewcommand\familydefault{\sfdefault}
\renewcommand{\baselinestretch}{1.1}


\usepackage{xcolor}
\definecolor{OldLace}{rgb}{0.99, 0.96, 0.9}
\definecolor{light-gray}{gray}{0.95}
\sphinxsetup{%
  verbatimwithframe=false,
  VerbatimColor={named}{light-gray},
%  TitleColor={named}{DarkGoldenrod},
%  hintBorderColor={named}{LightCoral},
  attentionborder=3pt,
%  attentionBorderColor={named}{Crimson},
%  attentionBgColor={named}{FloralWhite},
  noteborder=2pt,
%  noteBorderColor={named}{Olive},
  cautionborder=3pt,
%  cautionBorderColor={named}{Cyan},
%  cautionBgColor={named}{LightCyan}
}


\usepackage{sectsty}
\definecolor{lbl}{RGB}{2, 46, 77}
\chapterfont{\color{lbl}}  % sets colour of chapters
\sectionfont{\color{lbl}}  % sets colour of sections
\subsectionfont{\color{lbl}}  % sets colour of sections


% Reduce the list spacing
\usepackage{enumitem}
\setlist{nosep} % or \setlist{noitemsep} to leave space around whole list

% This allows adding :cite: in the label of figures.
% It is a work-around for https://github.com/mcmtroffaes/sphinxcontrib-bibtex/issues/92
\usepackage{etoolbox}
\AtBeginEnvironment{figure}{\renewcommand{\phantomsection}{}}



\renewcommand{\chaptermark}[1]{\markboth{#1}{}}
\renewcommand{\sectionmark}[1]{\markright{\thesection\ #1}}


\setcounter{secnumdepth}{3}
\usepackage{amssymb,amsmath}

% Figure and table caption in italic fonts
\makeatletter
\renewcommand{\fnum@figure}[1]{\small \textit{\figurename~\thefigure}: \it }
\renewcommand{\fnum@table}[1]{\small \textit{\tablename~\thetable}: \it }
\makeatother

% The next two lines patch the References title
\usepackage{etoolbox}
\patchcmd{\thebibliography}{\chapter*}{\phantom}{}{}

\definecolor{TitleColor}{rgb}{0 ,0 ,0} % black rathern than blue titles

\renewcommand{\Re}{{\mathbb R}}
\newcommand{\Na}{{\mathbb N}}
\newcommand{\Z}{{\mathbb Z}}

\usepackage{listings}
% see: http://mirror.aarnet.edu.au/pub/CTAN/macros/latex/contrib/listings/listings-1.3.pdf
\lstset{%
  basicstyle=\small, % print whole listing small
  keywordstyle=\color{red},
  identifierstyle=, % nothing happens
  commentstyle=\color{blue}, % white comments
  stringstyle=\color{OliveGreen}\it, % typewriter type for strings
  showstringspaces=false,
  numbers=left,
  numberstyle=\tiny,
  numbersep=5pt} % no special string space

\lstset{
    frame=single,
    breaklines=true,
    postbreak=\raisebox{0ex}[0ex][0ex]{\ensuremath{\color{red}\hookrightarrow\space}}
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\lstdefinelanguage{Modelica}{%
  morekeywords={Thermal,HeatTransfer,Interfaces, flow, %
    SI,Temperature,HeatFlowRate,HeatPort},
  morecomment=[l]{//},
  morecomment=[s]{/*}{*/},
  morestring=[b]",
  emph={equation, partial, connector, model, public, end, %
    extends, parameter}, emphstyle=\color{blue},
}


% Set format to 6x9 inches for report to be printed as a book.
%\usepackage[margin=0.75in, paperwidth=6in, paperheight=9in, includehead, includefoot, centering]{geometry}
\usepackage[margin=0.75in, includehead, includefoot, centering]{geometry}
%\geometry{margin=0.75in, includehead, includefoot, centering}


% Replace the threeparttable as it causes the caption to
% be no wider than the table, which looks quite bad.
% Also, center the caption and table.
%\renewenvironment{threeparttable}{ \begin{table}\centering }{ \end{table} }
% Increase distance of caption
\belowcaptionskip=5pt


\pagestyle{normal}
\renewcommand{\chaptermark}[1]{\markboth{#1}{}}
\renewcommand{\sectionmark}[1]{\markright{\thesection\ #1}}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\leftmark}
\fancyhead[LO]{\rightmark}
\fancypagestyle{plain}{%
   \fancyhead{} % get rid of headers
   \fancyhead[R]{\leftmark}
   \fancyfoot[R]{\thepage}
   \fancyfoot[L]{}
   \renewcommand{\headrulewidth}{0.5pt} % and the line
}

%%\rfoot[LE,RO]{\thepage}
%%\renewcommand{\headrulewidth}{0.4pt}
%%\renewcommand{\footrulewidth}{0.4pt}

\renewcommand{\chaptermark}[1]{\markboth{#1}{}}
\renewcommand{\sectionmark}[1]{\markright{\thesection\ #1}}

\renewcommand{\chaptermark}[1]{\markboth{#1}{}}
\renewcommand{\sectionmark}[1]{\markright{\thesection\ #1}}

%\hypersetup{hidelinks = true} % Makefile enables this for the 2 page printout

% Set format of table of content. Otherwise, the titles stick to the page numbers in some cases
\usepackage[tocgraduated]{tocstyle}
\usetocstyle{nopagecolumn}
\usepackage{pdfpages}

\usepackage{tikz}
\usepackage{graphicx}
\usetikzlibrary{calc}

'''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True
