import sys
import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from src.notes.adapters.orm import metadata, start_mappers


def setup():
    dir = os.path.dirname(os.path.realpath(__file__))
    src = os.path.join(dir, '..', 'src')
    sys.path.append(os.path.join(src))
    sys.path.append(os.path.join(src, 'notes'))

def pytest_configure(config):
    setup()


@pytest.fixture
def in_memory_db():
    engine = create_engine("sqlite:///:memory:")
    metadata.create_all(engine)
    return engine

@pytest.fixture
def session_factory(in_memory_db):
    start_mappers()
    yield sessionmaker(bind=in_memory_db)
    clear_mappers()

@pytest.fixture
def session(session_factory):
    return session_factory()
