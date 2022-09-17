from domain import model
from service import unit_of_work
from datetime import date


def list_notes(
    uow: unit_of_work.AbstractUnitOfWork,
    pagination: int,
):
    notes = uow.notes.list(pagination=pagination)
    return notes


def get_note(
    uow: unit_of_work.AbstractUnitOfWork,
    note_id: str
):
    note = uow.notes.get(note_id)
    return note

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