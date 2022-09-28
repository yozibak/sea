from .prompt import invalid_input
from .util import try_parse_int
from service import control
from .signal import Signal
from . import commands


def idle_act(ctl: control.Controller) -> Signal:
    val = input("[e]: exit, [l]: list, [r]: random, [s]: search, [a]: add\n")

    if val == 'e':
        return Signal.exit
    elif val == 'l':
        commands.list_latest(ctl)
        return Signal.list
    elif val == 's':
        commands.list_latest(ctl)
        return Signal.list
    elif val == 'r':
        return Signal.note
    elif val == 'a':
        return Signal.note
    
    invalid_input()


def list_act(ctl: control.Controller):
    val = try_parse_int(
        input("[index]: view note, [Enter]: next, [p]: prev, [q]: quit \n")
    )

    if type(val) == int:
        valid = commands.select_note(ctl, val)
        if valid:
            return Signal.note
    elif val == '':
        commands.next_list(ctl)
        return
    elif val == 'p':
        commands.prev_list(ctl)
        return
    elif val == 'q':
        return 'quit'

    invalid_input()


def note_act(ctl: control.Controller):
    val = try_parse_int(
        input("[r]: revise, [Enter]: next, [p]: prev, [e]: exit [d]: delete\n")
    )

    if val == 'r':
        # TODO
        return
    elif val == '':
        commands.next_note(ctl)
        return
    elif val == 'p':
        commands.prev_note(ctl)
        return
    elif val == 'e':
        return Signal.exit
    elif val == 'd':
        # TODO
        return Signal.exit
    
    invalid_input()
