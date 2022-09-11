from typing import List
from domain.model import Note
import subprocess
from .util import try_parse_int


def print_commands(
    commands: List[str]
) -> int:
    for n, cmd in enumerate(commands):
        print(f"[{n}]: {cmd}")
    action_number = try_parse_int(input(''))
    return action_number if type(action_number) == int else None


def print_notes(notes: List[Note]):
    for idx, note in enumerate(notes):
        print(f'[{idx}]: ', note)


def print_content(note: Note):
    print(note.title)
    print('\n')
    print(note.content)
    print('\n')
    print(f'Created: {note.created}')
    print(f'Revised: {note.updated}')
    print('\n')
    print('---EOL---')


def clear():
    subprocess.run('clear')