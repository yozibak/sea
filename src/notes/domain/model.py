
from datetime import date


class Note:
    def __init__(self, id: int, title: str, content: str, created: date, updated: date):
        self.id = id
        self.title = title
        self.content = content
        self.created = created
        self.updated = updated