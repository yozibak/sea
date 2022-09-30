import os

def sqlite_loc():
    dir = os.path.dirname(os.path.realpath(__file__))
    abs_path = os.path.join(dir, 'sea.db')
    return f'sqlite:///{abs_path}'

