from . import commands, prompt
from service import unit_of_work, control
from adapters import orm

def start():
    orm.start_mappers()
    uow = unit_of_work.SqlAlchemyUnitOfWork()
    controller = control.Controller(uow)
    with uow:
        handle_actions(controller)


def handle_actions(controller: control.Controller):
    alive = True
    while alive:
        # prompt.clear()
        print('Enter command number.')

        cmd_list = ["Exit"] + [c.prompt_name for c in commands.ENTRY_COMMANDS]
        cmd_num = prompt.print_commands(cmd_list)

        if type(cmd_num) == int and 0 < cmd_num < len(cmd_list):
            execute_command = commands.ENTRY_COMMANDS[cmd_num-1]
            execute_command(controller)
        else:
            alive = False
