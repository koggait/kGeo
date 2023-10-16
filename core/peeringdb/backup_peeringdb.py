from core.file_util import gen_data_path_extension
from core.mirror_util import copy_to_history
from core.root import Root


def backuping_peeringdb():
    backup_data(Root.PEERINGDB)


def backup_data(name):
    json_file = gen_data_path_extension(Root.SERIALIZED, name, Root.JSON)
    copy_to_history(json_file, Root.PEERINGDB, name)
    print('peeringdb stored')


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    backuping_peeringdb()
    exit()

