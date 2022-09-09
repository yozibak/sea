from domain import model
from service import unit_of_work
from datetime import date


def get_random(
    uow: unit_of_work.AbstractUnitOfWork,
):
    notes = uow.notes.list()
    return model.get_random(notes)


def list_recent(
    uow: unit_of_work.AbstractUnitOfWork,
):
    notes = uow.notes.list()
    for note in notes:
        print(note)


def edit_note(
    id: int, title: str, content: str,
    uow: unit_of_work.AbstractUnitOfWork
):
    note = uow.notes.get(id)
    note.title = title
    note.content = content
    note.updated = date.today()
    uow.commit()


def add_note(
    title: str, content: str,
    uow: unit_of_work.AbstractUnitOfWork    
):
    note = model.Note(
        title=title, 
        content=content,
        created=date.today(),
        updated=date.today(),
    )
    uow.notes.add(note)
    uow.commit()