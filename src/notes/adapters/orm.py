from sqlalchemy import (
    Date, Column, Integer, String, Table, MetaData, Text, create_engine,
)
from sqlalchemy.orm import mapper, declarative_base, sessionmaker
from notes.domain import model
from config import get_sqlite_path


# mappings

metadata = MetaData()

notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(100)),
    Column("content", Text),
    Column("created", Date),
    Column("updated", Date),
)

meta_infos = Table(
    "meta_infos",
    metadata,
    Column("id", Integer, primary_key=True),
)


# now make it real...

Base = declarative_base()

engine = create_engine(get_sqlite_path(), encoding='utf8', echo=False)

metadata.create_all(engine)

def start_mappers():
    mapper(
        model.Note,
        notes,   
    )


# use session from this 
DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=engine
)