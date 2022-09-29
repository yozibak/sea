from notes.domain import model
from service import unit_of_work
from datetime import date

def count_notes(
    uow: unit_of_work.AbstractUnitOfWork,
    search = ''
):
    return uow.notes.count(search)


def list_notes(
    uow: unit_of_work.AbstractUnitOfWork,
    pagination: int,
    query: str
):
    notes = uow.notes.list(pagination=pagination*10, search=query)
    return notes


def get_note(
    uow: unit_of_work.AbstractUnitOfWork,
    note_idx: int,
    query = ''
):
    note = uow.notes.get(note_idx, search=query)
    return note


def edit_note(
    idx: int, title: str, content: str,
    uow: unit_of_work.AbstractUnitOfWork
):
    note = uow.notes.get(idx)
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


def delete_note(
    note: model.Note,
    uow: unit_of_work.AbstractUnitOfWork
):
    uow.notes.delete(note)
    uow.commit()

