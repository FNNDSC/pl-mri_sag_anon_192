pl-mri_sag_anon_192
================================

.. image:: https://img.shields.io/docker/v/fnndsc/pl-mri_sag_anon_192?sort=semver
    :target: https://hub.docker.com/r/fnndsc/pl-mri_sag_anon_192

.. image:: https://img.shields.io/github/license/fnndsc/pl-mri_sag_anon_192
    :target: https://github.com/FNNDSC/pl-mri_sag_anon_192/blob/master/LICENSE

.. image:: https://github.com/FNNDSC/pl-mri_sag_anon_192/workflows/ci/badge.svg
    :target: https://github.com/FNNDSC/pl-mri_sag_anon_192/actions


.. contents:: Table of Contents


Abstract
--------

This application copies a set of image slices to the output directory.


Description
-----------

``mri_sag_anon_192.py`` copies a "built-in" set of anonymized neuro MRI images that are bundled within the container to the output directory.

The plugin is a convenient delivery platform for a creating a new Feed with a set of MRI data suitable for further analysis.


Usage
-----

.. code::

    mri_sag_anon_192                                            \
        [--dir <dirToCopy>                                      \
        [-h|--help]                                             \
        [--json] [--man] [--meta]                               \
        [--savejson <DIR>]                                      \
        [-v|--verbosity <level>]                                \
        [--version]                                             \
        <outputDir>


Arguments
~~~~~~~~~

.. code::

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


Getting inline help is:

.. code:: bash

    docker run --rm fnndsc/pl-mri_sag_anon_192 mri_sag_anon_192 --man

Run
~~~

You need you need to specify input and output directories using the `-v` flag to `docker run`.


.. code:: bash

    docker run --rm -u $(id -u)                                         \
        -v $(pwd)/out:/outgoing                                         \
        fnndsc/pl-mri_sag_anon_192 mri_sag_anon_192                     \
        /outgoing


Development
-----------

Build the Docker container:

.. code:: bash

    docker build -t local/pl-mri_sag_anon_192 .

Run unit tests:

.. code:: bash

    docker run --rm local/pl-mri_sag_anon_192 nosetests

Examples
--------

Copy DCM files
~~~~~~~~~~~~~~

.. code:: bash

    docker run --rm -u $(id -u)                                         \
        -v $(pwd)/out:/outgoing                                         \
        fnndsc/pl-mri_sag_anon_192 mri_sag_anon_192                     \
        /outgoing

Copy a NIfTI volume:

    docker run --rm -u $(id -u)                                         \
        -v $(pwd)/out:/outgoing                                         \
        fnndsc/pl-mri_sag_anon_192 mri_sag_anon_192                     \
        --dir /usr/local/src/data/nii                                   \
        /outgoing


.. image:: https://raw.githubusercontent.com/FNNDSC/cookiecutter-chrisapp/master/doc/assets/badge/light.png
    :target: https://chrisstore.co
