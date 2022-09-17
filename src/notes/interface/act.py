from .util import try_parse_int
from service import control

def list_act(ctl: control.Controller):
    val = try_parse_int(
        input("[index]: view note, [Enter]: next, [p]: prev, [q]: quit \n")
    )

    # TODO this seems a little strange to put here. but later. 
    if type(val) == int and val < len(ctl.notes):
        ctl.note_idx.set(val)

        return 'view'
    elif val == '':
        ctl.next_list()
    elif val == 'p':
        ctl.prev_list()
    elif val == 'q':
        return 'quit'
    else:
        print('invalid input.')
        return list_act()


def view_act(ctl: control.Controller):
    val = try_parse_int(
        input("[e]: edit note, [Enter]: next, [p]: prev, [q]: quit [d]: delete\n")
    )

    if val == 'e':
        return 'edit'
    elif val == '':
        ctl.next_note()
    elif val == 'p':
        ctl.prev_note()
    elif val == 'q':
        return 'quit'
    elif val == 'd':
        return 'delete'
    else:
        print('invalid input.')
        return view_act()
