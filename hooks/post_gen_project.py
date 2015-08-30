""" remove template files for all unselected engines and persistence options """
import os
import shutil


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
