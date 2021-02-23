from __future__ import annotations
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import sessionmaker, scoped_session, Session, Query
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.schema import MetaData
from typing import Generic, TypeVar, Final
import threading

import config
from service.utils import classproperty

T = TypeVar('T')
storage_engine: Final = create_engine(config.engine)
StorageSession: Final = scoped_session(sessionmaker(bind=storage_engine))
storage_session: Final = StorageSession()
storage_sessions = {threading.get_ident(): storage_session}


@as_declarative()
class Base(Generic[T]):
    metadata: MetaData = MetaData()

    @classmethod
    def query(cls: Base[T], *args: InstrumentedAttribute) -> Query:
        return cls.session.query(*args) if args else cls.session.query(cls)

    @classproperty
    def session(cls: Base[T]) -> Session:
        thread_id = threading.get_ident()
        if thread_id not in storage_sessions:
            storage_sessions[thread_id] = StorageSession()
        return storage_sessions[thread_id]
