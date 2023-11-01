from core.file_util import gen_data_dir
from core.file_util import gen_data_path_file
from core.mirror_util import getfile
from core.root import Root
from core.root_util import print_state


def mirroring_ip2loc():
    mirroring(filename=Root.IP2LOC4)
    mirroring(filename=Root.IP2LOC6)
    print_state(Root.MIRROR, Root.END, Root.IP2LOC)


def mirroring(filename):
    mirrored_file = gen_data_path_file(Root.MIRRORED, filename)
    getfile(Root.MIRROR_URLS[filename], mirrored_file)
    decompress_ip2loc_archive(compressed_archive=mirrored_file)


def decompress_ip2loc_archive(compressed_archive):
    import zipfile
    with zipfile.ZipFile(compressed_archive, 'r') as f:
        print(f.namelist())
        file_to_extract = f.namelist()[2]
        f.extract(file_to_extract, gen_data_dir(Root.MIRRORED))
    print('decompressed Files: ' + file_to_extract)


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    mirroring_ip2loc()
