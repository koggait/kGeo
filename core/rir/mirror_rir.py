from core.mirror_util import mirror_file
from core.root import Root
from core.root_util import print_state


def mirroring_rir():
    for name in Root.RIR_SET_STARTLINE.keys():
        mirror_file(name)
    print_state(Root.MIRROR, Root.END, Root.RIR)


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    mirroring_rir()
