#!/usr/bin/env python
#
# mri_sag_anon_192 fs ChRIS plugin app
#
# (c) 2021 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

from chrisapp.base import ChrisApp

import  os
from    os                      import listdir, sep
from    os.path                 import abspath, basename, isdir
from    distutils.dir_util      import copy_tree
import  shutil
import  sys
import  time
import  glob


Gstr_title = """
                _                                                __   _____  _____
               (_)                                              /  | |  _  |/ __  \.
 _ __ ___  _ __ _   ___  __ _  __ _     __ _ _ __   ___  _ __   `| | | |_| |`' / /'
| '_ ` _ \| '__| | / __|/ _` |/ _` |   / _` | '_ \ / _ \| '_ \   | | \____ |  / /
| | | | | | |  | | \__ \ (_| | (_| |  | (_| | | | | (_) | | | | _| |_.___/ /./ /___
|_| |_| |_|_|  |_| |___/\__,_|\__, |   \__,_|_| |_|\___/|_| |_| \___/\____/ \_____/
               ______          __/ |_____                   ______
              |______|        |___/______|                 |______|
"""

Gstr_synopsis = """

    NAME

       mri_sag_anon_192

    SYNOPSIS

        pip install ./
        mri_sag_anon_192                                                \\
            [--dir <dirToCopy>]                                         \\
            [-h] [--help]                                               \\
            [--json]                                                    \\
            [--man]                                                     \\
            [--meta]                                                    \\
            [--savejson <DIR>]                                          \\
            [-v <level>] [--verbosity <level>]                          \\
            [--version]                                                 \\
            <inputDir>                                                  \\
            <outputDir>

    BRIEF EXAMPLE

        * Bare bones execution

            docker run --rm -u $(id -u)                                 \\
                -v $(pwd)/out:/outgoing                                 \\
                fnndsc/pl-mri_sag_anon_192 mri_sag_anon_192             \\
                /outgoing

    DESCRIPTION

        ``mri_sag_anon_192.py`` copies a "built-in" set of anonymized neuro
        MRI images that are bundled within the container to the output
        directory.

        The plugin is a convenient delivery platform for a creating a
        new Feed with a set of MRI data suitable for further analysis.

    ARGS

        [--dir <directoryToCopyToOutput>]
        A directory to copy to the <outputDir>. Note that it you are
        running this as a container, then this path is a path located
        _within the container_!

        For the containerized build, the default path is

                    /usr/local/src/data/dcm

        An addition path is also available

                    /usr/local/src/data/nii

        [-h] [--help]
        If specified, show help message and exit.

        [--json]
        If specified, show json representation of app and exit.

        [--man]
        If specified, print (this) man page and exit.

        [--meta]
        If specified, print plugin meta data and exit.

        [--savejson <DIR>]
        If specified, save json representation file to DIR and exit.

        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.

        [--version]
        If specified, print version number and exit.
"""


class Mri_sag_anon_192(ChrisApp):
    """
    This application copies a set of image slices to the output directory.
    """
    PACKAGE                 = __package__
    TITLE                   = 'Anonymous sagittal neuro MRI image set of 192 slices'
    CATEGORY                = 'data'
    TYPE                    = 'fs'
    ICON                    = '' # url of an icon image
    MAX_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MAX_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT           = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT           = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """
        self.add_argument('--dir',
                          dest          ='dir',
                          type          = str,
                          default       = '/usr/local/src/data/dcm',
                          optional      = True,
                          help          = 'directory override')

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print('Version: %s' % self.get_version())

        if len(options.dir):
            print("Copying tree %s..." % options.dir)
            copy_tree(options.dir, options.outputdir)
            sys.exit(0)
        else:
            print("No directory specified and no copy performed.")
            sys.exit(1)

    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)
