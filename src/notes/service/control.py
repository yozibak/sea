from select import select
from . import unit_of_work, services
from typing import List
from domain import model

class Controller:
    def __init__(self, uow: unit_of_work.AbstractUnitOfWork):
        self.uow = uow

        # state? 
        self.notes = [] # type: List[model.Note]
        self.pagination = ListCursor()
        self.note_idx = NoteCursor()
        self.selected_note_id = None
    
    # note list mgmt

    def fetch_notes_list(self):
        self.notes = services.list_notes(self.uow, self.pagination.current)
    
    def list_latest(self):
        self.pagination.set(0)
        self.fetch_notes_list()
    
    def next_list(self):
        self.pagination.next()
        self.fetch_notes_list()

    def prev_list(self):
        self.pagination.prev()
        self.fetch_notes_list()
    
    # note select mgmt
    
    def adjust_note(self): 
        note_id = self.notes[self.note_idx.current].id
        self.set_note(note_id)

    def set_note(self, note_id: str):
        self.selected_note_id = note_id
    
    def next_note(self):
        self.note_idx.next()
        self.adjust_note()
    
    def prev_note(self):
        self.note_idx.prev()
        self.adjust_note()
    
    def latest_note(self):
        self.pagination.set(0)
        self.fetch_notes_list()
        self.note_idx.set(0)
        self.adjust_note()
    
    @property
    def current_note(self):
        if not self.selected_note_id:
            self.adjust_note()
        note = services.get_note(self.uow, self.selected_note_id)
        return note
    
    # mutation

    def add_note(self, title: str, content: str):
        services.add_note(title, content, self.uow)
        self.latest_note()

    def edit_note(self, id: str, title: str, content: str):
        services.edit_note(id, title, content, self.uow)
        self.latest_note()


class Cursor():

    def __init__(self):
        self.current = 0
    
    def set(self, dest: int):
        self.current = dest

    def next(self):
        self.current += 1
    
    def prev(self):
        self.current -= 1


class ListCursor(Cursor):
    pass


class NoteCursor(Cursor):
    pass

