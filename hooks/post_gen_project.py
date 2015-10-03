""" remove template files for all unselected engines and persistence options """
import os
import shutil
import subprocess
import sys

from textwrap import dedent

try:
    import virtualenv
    VIRTUALENV_AVAILABLE = True
except ImportError:
    VIRTUALENV_AVAILABLE = False

ENGINES = {'chameleon': 'pt', 'jinja2': 'jinja2', 'mako': 'mako'}
SELECTED_ENGINE = '{{ cookiecutter.template_engine }}'
PERSISTENCE_OPTIONS = ['zodb', 'sqlalchemy']
SELECTED_PERSISTENCE = '{{ cookiecutter.persistence }}'


for engine, extension in ENGINES.items():
    if engine != SELECTED_ENGINE:
        os.remove('./{{ cookiecutter.repo_name }}/templates/mytemplate.{}'.format(extension))

if SELECTED_PERSISTENCE not in PERSISTENCE_OPTIONS:
    os.remove('./{{ cookiecutter.repo_name }}/models.py')

if SELECTED_PERSISTENCE != 'sqlalchemy':
    shutil.rmtree('./{{ cookiecutter.repo_name }}/scripts')

if VIRTUALENV_AVAILABLE:
    virtualenv.create_environment('.')
    proc = subprocess.Popen(
            ['bin/python', 'setup.py', 'develop'],
            shell=sys.platform.startswith('win'),
            cwd='.'
    )
    proc.wait()

separator = "=" * 79
msg = dedent(
    """
    %(separator)s
    Tutorials: http://docs.pylonsproject.org/projects/pyramid_tutorials
    Documentation: http://docs.pylonsproject.org/projects/pyramid
    Twitter (tips & updates): http://twitter.com/pylons
    Mailing List: http://groups.google.com/group/pylons-discuss
    Welcome to Pyramid.  Sorry for the convenience.
    %(separator)s
""" % {'separator': separator})
print msg

if SELECTED_PERSISTENCE == 'sqlalchemy':
    print "*Important:* after setup, run initialize_{{ cookiecutter.repo_name }}_db to initialize database" 
