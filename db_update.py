from db import Base
from db.models import *
from alembic import config, script
from alembic.autogenerate import compare_metadata
from alembic.runtime import migration
from alembic.runtime.environment import EnvironmentContext
from sqlalchemy import create_engine
from config import engine as db_path
from logger import logger

engine = create_engine(db_path)


def assert_database_is_up_to_date():
    alembic_cfg = config.Config('alembic.ini')
    script_directory = script.ScriptDirectory.from_config(alembic_cfg)
    with engine.begin() as conn:
        context = migration.MigrationContext.configure(conn)
        if context.get_current_revision() != script_directory.get_current_head():
            logger.error('DB isn`t up to date')
            logger.warning('Needs upgrade the DB')
            return True
        else:
            return False


def assert_migrations_are_up_to_date():
    with engine.begin() as conn:
        context = migration.MigrationContext.configure(conn)
        diff = compare_metadata(context, Base.metadata)
        if len(diff) > 0:
            logger.error(
                "Migrations are not up to date. The following changes have been detected:\n"
                + "\n".join(str(d) for d in diff)
            )
            logger.warning("Create a new revision")
            return True
        else:
            return False


def create_tables(_cls: Base = Base):
    _cls.metadata.create_all(Base.storage_engine)


def drop_tables(_cls: Base = Base):
    _cls.metadata.drop_all(Base.storage_engine)
