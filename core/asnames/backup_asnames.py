from core.file_util import gen_data_path_extension
from core.mirror_util import copy_to_history
from core.root import Root
from core.root_util import print_state


def backuping_asnames():
    json_file = gen_data_path_extension(Root.SERIALIZED, Root.ASNAMES, Root.JSON)
    copy_to_history(json_file, Root.ASNAMES, Root.ASNAMES)
    print_state(Root.BACKUP, Root.END, Root.ASNAMES)


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    backuping_asnames()
