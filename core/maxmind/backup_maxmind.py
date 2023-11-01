from core.file_util import gen_data_path_file
from core.file_util import getname
from core.mirror_util import copy_to_history
from core.root import Root


def backuping_maxmind():
    backup_data(Root.MAXMIND_MERG_NAME_LIST[0])
    backup_data(Root.MAXMIND_MERG_NAME_LIST[1])


def backup_data(name):
    json_file = gen_data_path_file(Root.PROCESSED, name)
    directory = Root.MAXMIND[Root.NAME]
    copy_to_history(json_file, directory, getname(name))
    print('maxmind stored')


if __name__ == "__main__":
    import sys
    sys.path.append('/kGeo')
    backuping_maxmind()
    exit()
