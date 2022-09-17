from control import Controller

def list_notes(controller: Controller):
    notes = controller.notes
    print(notes)


def show_first_note(contoller: Controller):
    note = contoller.current_note
    print(note)
