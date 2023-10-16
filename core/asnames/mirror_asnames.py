from core.mirror_util import mirror_file
from core.root import Root
from core.root_util import print_state


def mirroring_asnames():
    mirror_file(filename=Root.ASNAMES)
    print_state(Root.MIRROR, Root.END, Root.ASNAMES)


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    mirroring_asnames()
