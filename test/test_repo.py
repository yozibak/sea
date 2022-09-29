from notes.service import unit_of_work

def test_count_records(session_factory):
    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
    with uow:
        count = uow.notes.count(search='hey')
        print()
        print(count)
        
        # assert notes[0].title == 'foo'

