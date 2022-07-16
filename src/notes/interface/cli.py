from adapters import orm
from notes.service import unit_of_work

def start():
    orm.start_mappers()
    handle_actions(
        unit_of_work.SqlAlchemyUnitOfWork()
    )


def handle_actions(
    uow: unit_of_work.AbstractUnitOfWork
):
    with uow:
        alive = True
        while alive:
            print("""
            What do you want?

            [0]: Exit
            [1]: Get recent notes
            [2]: Get random note

            """)
            action = int(input()) or 0
            if action == 1:
                print('get recent notes!')
            elif action == 2:
                print('get random')
            else:
                alive = False

