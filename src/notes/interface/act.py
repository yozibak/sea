from typing import List
from domain import model
from .util import try_parse_int

def require_act(notes: List[model.Note]):
    if type(notes) == list:
        return list_act(notes)
    else:
        return view_act()


def list_act(notes: List[model.Note]):
    val = try_parse_int(
        input("[index]: view note, [Enter]: next, [p]: prev, [q]: quit \n")
    )

    if type(val) == int and val < len(notes):
        note = notes[val]
        return note
    elif val == '':
        return 'next'
    elif val == 'p':
        return 'prev'
    elif val == 'q':
        return 'quit'
    else:
        print('invalid input.')
        return list_act()


def view_act():
    return

