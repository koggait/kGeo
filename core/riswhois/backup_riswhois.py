from core.file_util import gen_data_path_extension
from core.mirror_util import copy_to_history
from core.root import Root


def backuping_riswhois():
    backup_data(Root.RISWHO4)
    backup_data(Root.RISWHO6)


def backup_data(name):
    json_file = gen_data_path_extension(Root.SERIALIZED, name, Root.JSON)
    directory = Root.RISWHO
    filename = name
    copy_to_history(json_file, directory, filename)
    print('ris whois stored')


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    backuping_riswhois()
