from sqlalchemy import (
    Date, Column, Integer, String, Table, MetaData, Text,
    create_engine,
)
from sqlalchemy.orm import mapper
from config import get_sqlite_path
from domain import model

metadata = MetaData()

notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(100)),
    Column("content", Text),
    Column("created", Date), # isofomratted date string
    Column("updated", Date),
)

meta_infos = Table(
    "meta_infos",
    metadata,
    Column("id", Integer, primary_key=True),
)



def start_mappers():
    mapper(
        model.Note,
        notes,   
    )