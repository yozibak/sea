from notes.domain import model
from . import unit_of_work, services, editor
from random import randint

class Controller:
    def __init__(self, uow: unit_of_work.AbstractUnitOfWork):
        self.uow = uow
        self.cursor = 0 # 0 ~ last of query result
        self.query = ''
    
    def reset(self):
        self.cursor = 0
        self.query = ''
    
    @property
    def pagination(self):
        return self.cursor // 10
    
    @property
    def notes_count(self): 
        # maybe better call on demand, if it's gonna unbearably slow
        return services.count_notes(self.uow, search=self.query)

    @property
    def notes(self):
        return services.list_notes(self.uow, self.pagination, self.query)

    @property
    def current_note(self):
        return services.get_note(self.uow, self.cursor, self.query)
    
    def list_latest(self):
        self.cursor = 0
    
    def next_list(self):
        if self.pagination < self.notes_count // 10:
            self.cursor = (self.pagination + 1) * 10

    def prev_list(self):
        if self.pagination > 1:
            self.cursor = (self.pagination - 1) * 10

    def select_note(self, idx: int):
        if -1 < idx < len(self.notes):
            self.cursor = self.pagination * 10 + idx
            return True
    
    def next_note(self):
        if self.cursor < self.notes_count-1:
            self.cursor += 1
    
    def prev_note(self):
        if self.cursor != 0:
            self.cursor -= 1

    def get_random_note(self):
        self.cursor = randint(0, self.notes_count-1)
    
    def search_word(self):
        self.query = input('Enter search query: ')

    def add_note(self):
        title, content = editor.note_editor()
        services.add_note(title, content, self.uow)

    def edit_note(self, note: model.Note):
        title, content = editor.note_editor(note)
        services.edit_note(self.cursor, title, content, self.uow)

    def delete_note(self, note: model.Note):
        if input('Are you sure? [y/n]: ') == 'y':
            services.delete_note(note, self.uow)

