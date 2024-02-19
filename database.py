import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(os.environ.get("DATABASE_URL"))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def tables_exist(engine):
    meta = MetaData()
    meta.reflect(bind=engine)
    return len(meta.tables) > 0


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# if not tables_exist(engine):
Base.metadata.create_all(bind=engine)
