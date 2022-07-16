import os

def get_sqlite_path():
    abs_path = os.path.abspath('sea.db')
    return f'sqlite:////{abs_path}'