from datetime import date
from notes.service import unit_of_work, control


def insert_note(session, title, content, created, updated):
    session.execute(
        "INSERT INTO notes (title, content, created, updated) VALUES (:title, :content, :created, :updated)",
        dict(title=title, content=content, created=created, updated=updated),
    )


def prepare_notes(session, num:int):
    for i in range(1, num+1):
        insert_note(
            session,
            title=f'note-{i}', 
            content='content',
            created=date.today(),
            updated=date.today()
        )


def test_can_move_cursor_beyond_list(session_factory):
    session = session_factory()
    prepare_notes(session, 20)
    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
    ctl = control.Controller(uow)
    with uow:
        assert ctl.current_note.title == 'note-1'
        ctl.next_note()
        assert ctl.current_note.title == 'note-2'
        ctl.select_note(9)
        assert ctl.current_note.title == 'note-10'
        ctl.next_note()
        assert ctl.current_note.title == 'note-11'


def test_can_not_move_cursor_in_the_end_of_records(session_factory):
    session = session_factory()
    prepare_notes(session, 3)
    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
    ctl = control.Controller(uow)
    with uow:
        assert ctl.current_note.title == 'note-1'

        ctl.prev_note()
        assert ctl.current_note.title == 'note-1'

        ctl.next_note()
        ctl.next_note()
        assert ctl.current_note.title == 'note-3'

        ctl.next_note()
        assert ctl.current_note.title == 'note-3'

        ctl.prev_note()
        assert ctl.current_note.title == 'note-2'


def test_can_get_random_note(session_factory):
    session = session_factory()
    prepare_notes(session, 3)
    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
    ctl = control.Controller(uow)
    with uow:
        for _ in range(30):
            ctl.get_random_note()
            assert ctl.current_note
