from enum import Enum

class Signal(Enum):
    '''
    enum to communicate between process and command
    '''
    exit = 'quit'
    list = 'list'
    note = 'note'