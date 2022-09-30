from .signal import Signal
from . import prompt, act
from notes.service import unit_of_work, control
from notes.adapters import orm

def start():
    orm.start_mappers()
    uow = unit_of_work.SqlAlchemyUnitOfWork()
    controller = control.Controller(uow)
    with uow:
        process_idle(controller)


def process_idle(controller: control.Controller):
    alive = True
    while alive:
        prompt.clear()
        signal = act.idle_act(controller)
        if signal == Signal.exit:
            alive = False
        elif signal == Signal.list:
            process_list(controller)
        elif signal == Signal.note:
            process_note(controller)


def process_list(ctl: control.Controller):
    '''
    Process to handle commands on notes list. 
    It assumes that notes list are updated prior to enter each process.
    '''
    alive = True
    while alive:
        prompt.clear()
        notes = ctl.notes
        prompt.print_notes(notes)
        res = act.list_act(ctl)
        if res == Signal.exit:
            alive = False
        elif res == Signal.note:
            process_note(ctl)


def process_note(ctl: control.Controller):
    '''
    Process to handle commands on individual note
    It assumes that selected note id is present on control state
    '''
    alive = True
    while alive:
        prompt.clear()
        note = ctl.current_note
        prompt.print_content(note)
        res = act.note_act(ctl)
        if res == Signal.exit:
            alive = False

