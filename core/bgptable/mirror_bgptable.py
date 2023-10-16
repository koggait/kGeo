from core.mirror_util import decompress_gz
from core.mirror_util import mirror_decode_file
from core.root import Root
from core.root_util import print_state


def mirroring_bgptable():
    mirror_decode_file(Root.BGPTABLE, decompress_gz)
    print_state(Root.MIRROR, Root.END, Root.BGPTABLE)


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    mirroring_bgptable()
    exit()
