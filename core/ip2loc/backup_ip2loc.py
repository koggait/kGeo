from core.file_util import gen_data_path_extension
from core.mirror_util import copy_to_history
from core.root import Root


def backuping_ip2loc():
    json_file = gen_data_path_extension(Root.SERIALIZED, Root.IP2LOC4, Root.JSON)
    copy_to_history(json_file, Root.IP2LOC, Root.IP2LOC4)
    json_file = gen_data_path_extension(Root.SERIALIZED, Root.IP2LOC6, Root.JSON)
    copy_to_history(json_file, Root.IP2LOC, Root.IP2LOC6)
    print('ip2loc stored')


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    backuping_ip2loc()
