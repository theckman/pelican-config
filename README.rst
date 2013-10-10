Pelican Configuration
#####################

This is my Pelican configuration repository. Depending on whether this
is my local development environment I will symlink a different file to
``pelicanconf.py``.

For development::

    ln -sf dev.py pelicanconf.py

For production::

    ln -sf prod.py pelicanconf.py

In the future, the ``content`` and ``output`` directories will be
removed from this repository. Reason being is that in
development/production the ``content`` directory will be my `blog`_
repository and the output directory will be created when ``make html``
is ran to build the site.

.. _blog: https://github.com/theckman/blog

As a note, the theme I use in my configuration can be found on GitHub
(`pelican-svbheck`_).

.. _pelican-svbheck: https://github.com/theckman/pelican-svbheck

License
^^^^^^^
These configuration files are released under the ``MIT`` license. See
the provided ``LICENSE`` file for more information.

