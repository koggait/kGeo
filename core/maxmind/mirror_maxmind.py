from core.file_util import gen_data_dir
from core.file_util import gen_file_extension
from core.file_util import gen_data_path_file
from core.file_util import gendir
from core.mirror_util import getfile
from core.mirror_util import mirror_decode_file
from core.root import Root
from core.root_runtime import RootRuntime
from core.root_util import print_state


def mirroring_maxmind():
    mirror_decode_file(Root.MAXASN, decompress_maxmind_archive)
    mirror_decode_file(Root.MAXCOUNTRY, decompress_maxmind_archive)
    print_state(Root.MIRROR, Root.END, Root.MAXMIND)


def backup_mirroring_maxmind():
    mirror_file(filename=Root.MAXASN)
    mirror_file(filename=Root.MAXCOUNTRY)


def mirror_file(filename):
    mirrored_file = gen_data_path_file(Root.MIRRORED, filename)
    getfile(Root.MIRROR_URLS[filename], mirrored_file)
    decompress_maxmind_archive(compressed_archive=mirrored_file)


def decompress_maxmind_archive(compressed_archive):
    import zipfile
    with zipfile.ZipFile(compressed_archive, 'r') as f:
        print(f.namelist())
        if Root.MAXASN in compressed_archive:
            RootRuntime.MAXASNLIST = [f.namelist()[2], f.namelist()[3]]
            saveRootRuntime(1, 'MAXASNLIST = ' + str(RootRuntime.MAXASNLIST))
            mlist = RootRuntime.MAXASNLIST
        elif Root.MAXCOUNTRY in compressed_archive:
            RootRuntime.MAXCOUNTRYLOCLIST = [f.namelist()[1]]
            saveRootRuntime(2, 'MAXCOUNTRYLOCLIST = ' + str(RootRuntime.MAXCOUNTRYLOCLIST))
            RootRuntime.MAXCOUNTRYLIST = [f.namelist()[6], f.namelist()[9]]
            saveRootRuntime(3, 'MAXCOUNTRYLIST = ' + str(RootRuntime.MAXCOUNTRYLIST))
            mlist = [RootRuntime.MAXCOUNTRYLOCLIST[0], RootRuntime.MAXCOUNTRYLIST[0], RootRuntime.MAXCOUNTRYLIST[1]]
        elif RootRuntime.MAXCITY in compressed_archive:
            RootRuntime.MAXCITYLOCLIST = [f.namelist()[0]]
            saveRootRuntime(4, 'MAXCITYLOCLIST = ' + str(RootRuntime.MAXCITYLOCLIST))
            RootRuntime.MAXCITYLIST = [f.namelist()[5], f.namelist()[12]]
            saveRootRuntime(5, 'MAXCITYLIST = ' + str(RootRuntime.MAXCITYLIST))
            mlist = [RootRuntime.MAXCITYLOCLIST[0], RootRuntime.MAXCITYLIST[0], RootRuntime.MAXCITYLIST[1]]
        for l in mlist:
            f.extract(l, gen_data_dir(Root.MIRRORED))
    print('decompressed Files: ')
    print(mlist)

def saveRootRuntime(no, content):
    input_file = gen_file_extension(gendir(Root.COREDIR, Root.ROOTRUNTIME), Root.PY)
    print(input_file)
    with open(input_file, 'r') as file:
        lines = file.readlines()
    lines[no] = '   ' + content + '\n'
    with open(input_file, 'w') as file:
        file.writelines(lines)


if __name__ == "__main__":
    Root.COREDIR = '../'
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    mirroring_maxmind()
    exit()

