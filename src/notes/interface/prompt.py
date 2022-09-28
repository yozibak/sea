from typing import List
from domain.model import Note
import subprocess


def print_commands(commands: List[str]):
    for n, cmd in enumerate(commands):
        print(f"[{n}]: {cmd}")


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
    print('---END---')


def clear():
    subprocess.run('clear')


def invalid_input():
    print("invalid input.")
    input("press any key to continue.")