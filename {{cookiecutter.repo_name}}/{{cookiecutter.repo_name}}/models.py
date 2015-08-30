{% if cookiecutter.persistence == 'sqlalchemy' -%}
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

Index('my_index', MyModel.name, unique=True, mysql_length=255)
{% endif -%}
{% if cookiecutter.persistence == 'zodb' -%}
from persistent.mapping import PersistentMapping


class MyModel(PersistentMapping):
    __parent__ = __name__ = None


def appmaker(zodb_root):
    if 'app_root' not in zodb_root:
        app_root = MyModel()
        zodb_root['app_root'] = app_root
        import transaction
        transaction.commit()
    return zodb_root['app_root']
{% endif -%}
