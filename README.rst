====================
cookiecutter-pyramid
====================

Cookiecutter template for a Pyramid package. See https://github.com/audreyr/cookiecutter.

* Pick template engine and persistence backend
* Virtualenv automatically created and setup in development mode
* Free software: BSD license
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 2.6, 2.7, 3.3, 3.4
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_

Usage
-----

Generate a Pyramid project::

    cookiecutter https://github.com/cguardia/cookiecutter-pyramid.git

Then:

* cd to project name given in the last cookicutter question
* Run bin/pserve development.ini
