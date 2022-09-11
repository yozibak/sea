from datetime import date
from random import randint
from typing import List


class Note:
    def __init__(
        self, title: str, content: str,
        id: int = None,
        created: date = date.today(), 
        updated: date = date.today()
    ):
        self.id = id
        self.title = title
        self.content = content
        self.created = created
        self.updated = updated
    
    def __str__(self) -> str:
        return f'{date_format(self.updated)} - {self.title}'


def get_random(notes: List[Note]):
    if len(notes):
        return notes[randint(0, len(notes)-1)]


def date_format(date: date):
    return date.strftime("%y/%m/%d")