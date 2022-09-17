from control import Controller
import command

def start():
    controller = Controller()
    handle_command(controller)


def handle_command(controller: Controller):
    alive = True

    while alive:
        cmd_idx = input('which command? [1 2 3 4]')
        if cmd_idx == '1':
            command.list_notes(controller)
        elif cmd_idx == '2':
            command.show_first_note(controller)
        elif cmd_idx == '3':
            controller.next()
        elif cmd_idx == '4':
            controller.prev()
        elif cmd_idx == 'quit':
            alive = False
        else:
            print('invalid input')

