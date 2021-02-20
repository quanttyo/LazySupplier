from __future__ import annotations
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import sessionmaker, scoped_session, Session, Query
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.schema import MetaData
from typing import Generic, Any, Type, TypeVar, List, Dict
import threading

import config
from service.utils import classproperty

T = TypeVar('T')


@as_declarative()
class Base(Generic[T]):
    metadata: MetaData = MetaData()
    storage_engine = create_engine(config.engine)
    StorageSession = scoped_session(sessionmaker(bind=storage_engine))
    storage_session = StorageSession()
    storage_sessions = {threading.get_ident(): storage_session}

    @classmethod
    def query(cls: Type[Base], *args: InstrumentedAttribute) -> Query:
        if args:
            return cls.session.query(*args)
        else:
            return cls.session.query(cls)

    @classproperty
    def session(cls: Type[Base]) -> Session:
        thread_id = threading.get_ident()
        if thread_id not in cls.storage_sessions:
            cls.storage_sessions[thread_id] = cls.StorageSession()
        return cls.storage_sessions[thread_id]
