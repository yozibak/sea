from service import control
from domain import model
from service import editor


def list_latest(ctl: control.Controller):
    ctl.list_latest()


def search_word(ctl: control.Controller):
    pass


def get_random(ctl: control.Controller):
    pass


def add_note(ctl: control.Controller):
    title, content = editor.note_editor()
    ctl.add_note(title, content)


def edit_note(ctl: control.Controller, note: model.Note):
    title, content = editor.note_editor(note)
    ctl.edit_note(note.id, title, content)


def select_note(ctl: control.Controller, idx: int):
    if -1 < idx < len(ctl.notes):
        ctl.note_idx.set(idx)
        return True


def next_list(ctl: control.Controller):
    ctl.next_list()


def prev_list(ctl: control.Controller):
    # TODO validation
    ctl.prev_list()


def next_note(ctl: control.Controller):
    ctl.next_note()


def prev_note(ctl: control.Controller):
    ctl.prev_note()

