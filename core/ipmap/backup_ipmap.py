from core.file_util import gen_data_path_extension
from core.mirror_util import copy_to_history
from core.root import Root


def backuping_ipmap():
    json_file = gen_data_path_extension(Root.SERIALIZED, Root.IPMAP, Root.JSON)
    directory = Root.IPMAP
    filename = Root.IPMAP
    copy_to_history(json_file, directory, filename)
    print('ipmap stored')


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    backuping_ipmap()
    exit()
