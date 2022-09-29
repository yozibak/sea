from domain import model
from . import unit_of_work, services, editor

class Controller:
    def __init__(self, uow: unit_of_work.AbstractUnitOfWork):
        self.uow = uow
        self.pagination = 0
        self.note_idx = 0
        self.selected_note_id = None

    @property
    def notes(self):
        return services.list_notes(self.uow, self.pagination)

    @property
    def current_note(self):
        if not self.selected_note_id:
            self._adjust_nid()
        note = services.get_note(self.uow, self.selected_note_id)
        return note
    
    def list_latest(self):
        self.pagination = 0
    
    def next_list(self):
        self.pagination += 1 #
        if len(self.notes) == 0:
            self.prev_list()
        else:
            self.note_idx = 0

    def prev_list(self):
        if self.pagination > 1:
            self.pagination -= 1
            self.note_idx = len(self.notes) - 1

    def _adjust_nid(self):
        self.selected_note_id = self.notes[self.note_idx].id

    def select_note(self, idx: int):
        if -1 < idx < len(self.notes):
            self.note_idx = idx
            self._adjust_nid()
            return True
    
    def next_note(self):
        if self.note_idx < len(self.notes)-1:
            self.note_idx += 1
            self._adjust_nid()
        else:
            self.next_list()
    
    def prev_note(self):
        if self.note_idx == 0:
            self.prev_list()
        else:
            self.note_idx -= 1
            self._adjust_nid()
    
    def latest_note(self):
        self.pagination = 0
        self.note_idx = 0
        self._adjust_nid()

    def add_note(self):
        title, content = editor.note_editor()
        services.add_note(title, content, self.uow)
        self.latest_note()

    def edit_note(self, note: model.Note):
        title, content = editor.note_editor(note)
        services.edit_note(note.id, title, content, self.uow)
        self.latest_note()

    def delete_note(self, id: str):
        pass
