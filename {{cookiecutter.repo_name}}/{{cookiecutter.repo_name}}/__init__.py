from pyramid.config import Configurator

{% if cookiecutter.persistence == 'zodb' -%}
from pyramid_zodbconn import get_connection
from .models import appmaker


def root_factory(request):
    conn = get_connection(request)
    return appmaker(conn.root())
{% endif %}
{% if cookiecutter.persistence == 'sqlalchemy' -%}
from sqlalchemy import engine_from_config
from .models import (
    DBSession,
    Base,
    )
{% endif %}

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    {% if cookiecutter.persistence == 'sqlalchemy' -%}
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    {% endif -%}
    {% if cookiecutter.persistence == 'zodb' -%}
    config = Configurator(root_factory=root_factory, settings=settings)
    {% else -%}
    config = Configurator(settings=settings)
    config.add_route('home', '/')
    {% endif -%}
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.scan()
    return config.make_wsgi_app()
