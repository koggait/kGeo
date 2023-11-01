from core.file_util import gen_data_path_extension
from core.mirror_util import copy_to_history
from core.root import Root


def backuping_bgptable():
    json_file = gen_data_path_extension(Root.PROCESSED, Root.BGPTABLE4, Root.JSON)
    directory = Root.BGPTABLE
    filename = Root.BGPTABLE4
    copy_to_history(json_file, directory, filename)
    bgptable4 = gen_data_path_extension(Root.PROCESSED, Root.BGPTABLE4, Root.JSON)
    bgptable6 = gen_data_path_extension(Root.PROCESSED, Root.BGPTABLE6, Root.JSON)
    copy_to_history(bgptable4, Root.BGPTABLE, Root.BGPTABLE4)
    copy_to_history(bgptable6, Root.BGPTABLE, Root.BGPTABLE6)
    print('BGPTABLE core attributes stored to history')


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    backuping_bgptable()
    exit()
