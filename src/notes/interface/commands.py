import functools
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
def list_recent(uow: unit_of_work.AbstractUnitOfWork):
    services.list_recent(uow)


@command('Show Random Note')
def get_random(uow: unit_of_work.AbstractUnitOfWork):
    note = services.get_random(uow)
    print(note)


@command('Search For Word')
def search_word():
    pass


@command('Edit Current Note')
def edit_note():
    pass


@command('Add New Note')
def add_note(uow: unit_of_work.AbstractUnitOfWork):
    # shouldn't this on service layer? 
    title, content = editor()
    note = model.Note(title=title, content=content)
    uow.notes.add(note)
    uow.commit()
