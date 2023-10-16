from core.file_util import gen_data_path_file
from core.mirror_util import getfile
from core.root import Root
from core.root_util import print_state


def mirroring_peeringdb():
    mirroring(Root.PEERINGDB)
    print_state(Root.MIRROR, Root.END, Root.PEERINGDB)


def mirroring(filename):
    mirrored_file = gen_data_path_file(Root.MIRRORED, filename)
    getfile(Root.MIRROR_URLS[filename], mirrored_file)


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    mirroring_peeringdb()
    exit()

