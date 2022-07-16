from setup import setup
setup()

import sys
for p in sys.path:
    print(p)

from notes.interface import cli

if __name__ == '__main__':
    cli.start()