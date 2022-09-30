from sqlalchemy import (
    Date, Column, Integer, String, Table, MetaData, Text, create_engine,
)
from sqlalchemy.orm import mapper, declarative_base, sessionmaker
from notes.domain import model
from config import sqlite_loc

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


Base = declarative_base()

engine = create_engine(sqlite_loc(), encoding='utf8', echo=False)

metadata.create_all(engine)

def start_mappers():
    mapper(
        model.Note,
        notes,   
    )


DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=engine
)