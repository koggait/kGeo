import sys

from core.root import Root
from cli.controller import control

if __name__ == "__main__":
    Root.DATADIR = 'data/'
    Root.HISTORYDIR = 'history/'
    control(sys.argv)
    exit()
