from sqlalchemy import MetaData, create_engine, event
from sqlalchemy.orm import sessionmaker, scoped_session
import threading

storage_engine = create_engine("sqlite:///test.db")
storage_meta = MetaData()
storage_meta.bind = storage_engine
StorageSession = scoped_session(sessionmaker(bind=storage_engine))
storage_session = StorageSession()

storage_sessions = {threading.get_ident(): storage_session}

from data.db.storage import node, nomenclature


def get_storage_session() -> object:
    thread_id = threading.get_ident()
    if thread_id not in storage_sessions:
        storage_sessions[thread_id] = StorageSession()
    return storage_sessions[thread_id]
