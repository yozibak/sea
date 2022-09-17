
class Note:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self) -> str:
        return f'Note({self.name})'

