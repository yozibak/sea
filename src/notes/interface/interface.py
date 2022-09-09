from interface.prompt import prompt
from service import unit_of_work
from adapters import orm
from . import commands

def start():
    orm.start_mappers()
    uow = unit_of_work.SqlAlchemyUnitOfWork()
    with uow:
        handle_actions(uow)


def handle_actions(uow: unit_of_work.AbstractUnitOfWork):
    alive = True
    while alive:
        print('What do you want?')
        action = prompt(commands=[
            "Exit",
            commands.list_recent.prompt_name,
            commands.get_random.prompt_name,
            commands.add_note.prompt_name,
        ])
        if action == 1:
            commands.list_recent(uow)
        elif action == 2:
            commands.get_random(uow)
        elif action == 3:
            commands.add_note(uow)
        else:
            alive = False
