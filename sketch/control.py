from model import Note

class Controller:
    
    def __init__(self):
        self.notes = [Note('a'), Note('b'), Note('c')] 
        self.index = 0
    
    def next(self):
        self.index += 1
    
    def prev(self):
        self.index -= 1

    @property
    def current_note(self):
        return self.notes[self.index]

