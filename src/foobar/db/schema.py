from __future__ import annotations

from collections.abc import Generator

from sqlalchemy import (
    create_engine,
)
from sqlalchemy.engine import Engine
from sqlalchemy.orm import (
    DeclarativeBase,
    sessionmaker,
)
from sqlalchemy.orm.session import Session

from foobar.core.config import db_config

engine: Engine = create_engine(db_config.db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db() -> Generator[Session]:
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
