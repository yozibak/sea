import sys
import os

def setup():
    dir = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(dir)