from select import select
from . import unit_of_work, services
from typing import List
from domain import model

class Controller:
    def __init__(self, uow: unit_of_work.AbstractUnitOfWork):
        self.uow = uow
        self.notes = [] # type: List[model.Note]
        self.pagination = ListCursor()
        self.note_idx = NoteCursor()
        self.selected_note_id = None
    
    def list_latest(self):
        self.pagination.set(0)
        self.notes = services.list_notes(self.uow, self.pagination.current)
    
    def next_list(self):
        self.pagination.next()
        self.notes = services.list_notes(self.uow, self.pagination.current)

    def prev_list(self):
        self.pagination.prev()
        self.notes = services.list_notes(self.uow, self.pagination.current)
    
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
    
    def current_note(self):
        if self.selected_note_id:
            note = services.get_note(self.uow, self.selected_note_id)
            return note
        else:
            self.adjust_note()
            note = services.get_note(self.uow, self.selected_note_id)
            return note


# TODO index validation needs modifications

class Cursor():

    def __init__(self):
        self.current = 0
    
    def set(self, dest: int):
        self.current = dest

    def next(self):
        if self.current < 9:
            self.current += 1
    
    def prev(self):
        if self.current > 0:
            self.current -= 1


class ListCursor(Cursor):
    pass


class NoteCursor(Cursor):
    pass

