Lantern provider for Plainbox
=============================

This directory contains the Lantern provider for Plainbox.

Basic Setup
-----------

To use this provider you will need to use python virtualenv (even if you have
packaged version of plainbox available it is likely too old)::

    virtualenv -p python3 venv
    . venv/bin/activate
    pip install plainbox==0.20

This procedure was tested on Ubuntu, Debian and Fedora.

Usage
-----

As long as the virtual environment is active, you can run all of the tests by
running this command::

    ./manage.py run

This will perform an interactive test run culminated with printing of the
summary of the test run and creation of 'lantern-submission-<UUID>.json' file.
Please send me that file!

This is it for the moment. A more elaborate version is under construction.

Hacking
-------

If you make some changes you can re-validate the provider. This isn't perfect
but it can catch a good number of issues. To do that simply run::

    ./manage.py validate -N
