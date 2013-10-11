Pelican Configuration
#####################

This is my Pelican configuration repository. Depending on whether this
is my local development environment I will symlink a different file to
``pelicanconf.py``.

For development::

    ln -sf dev.py pelicanconf.py

For production::

    ln -sf prod.py pelicanconf.py

Note
^^^^

The ``content`` directory, which the Makefile expects to be there, has
been removed and will need to be recreated to contain the blog content.
This folder as removed as on my systems I will be cloning my `blog`_
repository to it. The ``output`` directory should be auto-created by
Pelican during the build.

.. _blog: https://github.com/theckman/blog

As a note, the theme I use in my configuration can be found on GitHub
(`pelican-svbheck`_).

.. _pelican-svbheck: https://github.com/theckman/pelican-svbheck

License
^^^^^^^
These configuration files are released under the ``MIT`` license. See
the provided ``LICENSE`` file for more information.

