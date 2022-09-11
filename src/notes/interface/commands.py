import functools
from domain.model import Note
from notes.interface.act import require_act
from . import prompt
from .editor import editor
from service import services, unit_of_work
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
def list_recent(uow: unit_of_work.AbstractUnitOfWork, pagination=0):
    notes = services.list_recent(uow, pagination)
    prompt.print_notes(notes)
    res = require_act(notes)
    if type(res) == Note:
        pass
        # prompt.print_content(res)
    elif res == 'prev':
        pass
    elif res == 'next':
        pass
    elif res == 'quit':
        pass
    


@command('Search For Word')
def search_word(uow: unit_of_work.AbstractUnitOfWork):
    notes = services.list_recent(uow)
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
    get_random,
    search_word,
    add_note,
]

# 
# Chained Commands
# 

@command('Edit Current Note')
def edit_note():
    pass