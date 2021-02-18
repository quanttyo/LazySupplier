from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.schema import MetaData
import threading

import config


def val_as_dict(obj):
    return obj._asdict()


class _Base(object):
    metadata = MetaData()
    storage_engine = create_engine(config.engine)
    StorageSession = scoped_session(sessionmaker(bind=storage_engine))
    storage_session = StorageSession()
    storage_sessions = {threading.get_ident(): storage_session}
    s_query = StorageSession.query_property()

    @classmethod
    @property
    def query(cls) -> object:
        return cls._get_storage_session().query

    @classmethod
    @property
    def session(cls) -> object:
        return cls._get_storage_session()

    @classmethod
    def _get_storage_session(cls) -> object:
        thread_id = threading.get_ident()
        if thread_id not in cls.storage_sessions:
            cls.storage_sessions[thread_id] = cls.StorageSession()
        return cls.storage_sessions[thread_id]


Base = declarative_base(cls=_Base)
