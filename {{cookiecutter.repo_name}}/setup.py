##############################################################################
#
# Copyright (c) 2008-2012 Agendaless Consulting and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the BSD-like license at
# http://www.repoze.org/LICENSE.txt.  A copy of the license should accompany
# this distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
# EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
# FITNESS FOR A PARTICULAR PURPOSE
#
##############################################################################

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    README = CHANGES = ''

install_requires = [
    'pyramid', 
    'waitress',
    'pyramid_debugtoolbar',
    {% if cookiecutter.persistence == 'zodb' -%}'ZODB3',
    'pyramid_zodbconn',
    'transaction',
    'pyramid_tm',
    {% endif -%}
    {% if cookiecutter.persistence == 'sqlalchemy' -%}'SQLAlchemy',
    'zope.sqlalchemy',
    'pyramid_tm',
    {% endif -%}
    {% if cookiecutter.template_engine == 'chameleon' -%}'pyramid_chameleon',
    {% endif -%}
    {% if cookiecutter.template_engine == 'jinja2' -%}'pyramid_jinja2',
    {% endif -%}
    {% if cookiecutter.template_engine == 'mako' -%}'pyramid_mako',
    {% endif -%}
    ]

docs_extras = ['Sphinx']
testing_extras = ['nose', 'coverage', 'mock', 'virtualenv']
i18n_extras = ['Babel', 'transifex-client', 'lingua<2.0']

setup(name='{{ cookiecutter.repo_name }}',
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.project_short_description }}',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "License :: BSD",
        ],
    keywords='wsgi pylons pyramid',
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}'",
    license="BSD",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=install_requires,
    test_suite="{{ cookiecutter.repo_name }}",
    message_extractors={
        '{{ cookiecutter.repo_name }}': [
              ('**.py', 'python', None),  # babel extractor supports plurals
              ('**.pt', 'lingua_xml', None),
          ],
    },
    extras_require = {
        'testing':testing_extras,
        'docs':docs_extras,
        'i18n':i18n_extras,
    },
    entry_points="""\
    [paste.app_factory]
    main = {{ cookiecutter.repo_name }}:main
    {% if cookiecutter.persistence == 'sqlalchemy' -%}[console_scripts]
    initialize_{{ cookiecutter.repo_name }}_db = {{ cookiecutter.repo_name }}.scripts.initializedb:main
    {% endif -%}
    """,
    ),
