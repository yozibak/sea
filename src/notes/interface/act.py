from . import prompt
from .util import try_parse_int
from notes.service import control
from notes.interface.signal import Signal


def idle_act(ctl: control.Controller) -> Signal:
    val = input("[e]: exit, [l]: list, [r]: random, [s]: search, [a]: add\n")

    if val == 'e':
        return Signal.exit
    elif val == 'l':
        ctl.list_latest()
        return Signal.list
    elif val == 's':
        ctl.search_word()
        return Signal.list
    elif val == 'r':
        ctl.get_random_note()
        return Signal.note
    elif val == 'a':
        ctl.add_note()
        return Signal.note
    
    prompt.invalid_input()


def list_act(ctl: control.Controller):
    val = try_parse_int(
        input("[index]: view note, [Enter]: next, [p]: prev, [e]: exit \n")
    )

    if type(val) == int:
        valid = ctl.select_note(val)
        if valid:
            return Signal.note
    elif val == '':
        ctl.next_list()
        return
    elif val == 'p':
        ctl.prev_list()
        return
    elif val == 'e':
        ctl.reset()
        return Signal.exit

    prompt.invalid_input()


def note_act(ctl: control.Controller):
    val = try_parse_int(
        input("[r]: revise, [Enter]: next, [p]: prev, [e]: exit [d]: delete\n")
    )

    if val == 'r':
        ctl.edit_note(ctl.current_note)
        return
    elif val == '':
        ctl.next_note()
        return
    elif val == 'p':
        ctl.prev_note()
        return
    elif val == 'e':
        return Signal.exit
    elif val == 'd':
        ctl.delete_note(ctl.current_note)
        return Signal.exit
    
    prompt.invalid_input()
