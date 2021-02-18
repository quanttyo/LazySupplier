from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import threading

import config

class _Base(object):
    storage_engine = create_engine(config.engine)
    StorageSession = scoped_session(sessionmaker(bind=storage_engine))
    storage_session = StorageSession()
    storage_sessions = {threading.get_ident(): storage_session}

    @classmethod
    @property
    def session(cls) -> object:
        thread_id = threading.get_ident()
        if thread_id not in cls.storage_sessions:
            cls.storage_sessions[thread_id] = cls.StorageSession()
        return cls.storage_sessions[thread_id]

    @classmethod
    def _create_tables(cls):
        cls.metadata.create_all(cls.storage_engine)

    @classmethod
    def _drop_tables(cls):
        cls.metadata.drop_all(cls.storage_engine)


Base = declarative_base(cls=_Base)
