import functools
from ..service import control
from domain.model import Note
from notes.interface.act import list_act, view_act
from . import prompt
from .editor import editor
from service import services, unit_of_work, control
from domain import model

def command(command_name: str):
    def deco(fn):
        @functools.wraps(fn)
        def decorated(*args, **kwargs):
            # Maybe other modifications here
            return fn(*args, **kwargs)
        decorated.prompt_name = command_name
        return decorated
    return deco


@command('List Recent Notes')
def list_recent(ctl: control.Controller):
    ctl.list_latest()
    browse_list(ctl)


def browse_list(ctl: control.Controller):
    alive = True
    while alive:
        prompt.clear()
        notes = ctl.notes
        prompt.print_notes(notes)
        res = list_act(ctl)
        if res == 'quit':
            alive = False
        elif res == 'view':
            alive = False
        else:
            pass # loop with new list
    
    if ctl.note_idx:
        view_note(ctl)


def view_note(ctl: control.Controller):
    alive = True
    while alive:
        prompt.clear()
        note = ctl.current_note()
        prompt.print_content(note)
        res = view_act(ctl)
        if res == 'quit':
            alive == False
        elif res == 'edit':
            alive == False
        elif res == 'delete':
            alive == False
        else:
            pass # loop



@command('Search For Word')
def search_word(uow: unit_of_work.AbstractUnitOfWork):
    notes = services.list_notes(uow)
    prompt.print_notes(notes)


@command('Show Random Note')
def get_random(uow: unit_of_work.AbstractUnitOfWork):
    note = services.get_random(uow)
    print(note)


@command('Add New Note')
def add_note(uow: unit_of_work.AbstractUnitOfWork):
    # shouldn't this on service layer? later.
    title, content = editor()
    note = model.Note(title=title, content=content)
    uow.notes.add(note)
    uow.commit()


ENTRY_COMMANDS = [
    list_recent,
    # get_random,
    # search_word,
    # add_note,
]

# 
# Chained Commands
# 

@command('Edit Current Note')
def edit_note():
    pass