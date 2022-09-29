from notes.service import unit_of_work
from notes.adapters import orm
from notes.domain import model


def test_count_records():
    orm.start_mappers()
    uow = unit_of_work.SqlAlchemyUnitOfWork()
    with uow:
        count = uow.notes.count(search='hey')
        print()
        print(count)
        
        # assert notes[0].title == 'foo'

