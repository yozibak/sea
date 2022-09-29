import tempfile, os
from subprocess import call
from typing import Tuple
from notes.domain import model

EDITOR = os.environ.get('EDITOR', 'vim')


def note_editor(note: model.Note = None) -> Tuple[str, str]:
    ini = ''
    if note:
        ini += note.title
        ini += '\n\n'
        ini += note.content
        ini += '\n'
    with tempfile.NamedTemporaryFile(suffix=".tmp", mode='r+') as tf:
        tf.write(ini)
        tf.flush()
        def edit():
            call([EDITOR, '+set backupcopy=yes', tf.name])
            # Once editing ends...
            tf.seek(0)
            edited = tf.read()
            if not validate(edited):
                print("You must set title & content")
                input("press key to edit again")
                return edit()
            return edited
        edited = edit()
    return retrieve(edited)


def validate(plain_txt: str) -> bool:
    return len(plain_txt.split('\n\n')) > 1


def retrieve(plain_txt: str) -> Tuple[str,str]:
    splitted = plain_txt.split('\n\n')
    title = splitted[0]
    content = '\n\n'.join(splitted[1:])
    return title, content
