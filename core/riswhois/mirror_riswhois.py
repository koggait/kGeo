from core.mirror_util import decompress_gz
from core.mirror_util import mirror_decode_file
from core.root import Root
from core.root_util import print_state


def mirroring_riswhois():
    mirror_decode_file(Root.RISWHO4, decompress_gz)
    mirror_decode_file(Root.RISWHO6, decompress_gz)
    print_state(Root.MIRROR, Root.END, Root.RISWHO)


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    mirroring_riswhois()
    exit()

