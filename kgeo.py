import sys

from core.root import Root
from cli.controller import control


def main():
    control(sys.argv)


if __name__ == "__main__":
    Root.DATADIR = 'core/data/'
    Root.HISTORYDIR = 'core/history/'
    main()
    exit()
