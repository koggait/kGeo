from core.file_util import gen_data_path_extension
from core.file_util import gen_specific_filename
from core.mirror_util import copy_to_history
from core.root import Root


def backuping_rir():

    for name in Root.RIR_SET_STARTLINE.keys():
        for rirtype in split_stats_name(name):
            backup_data(rirtype)


def split_stats_name(name):
    return gen_specific_filename(name, Root.IP4), gen_specific_filename(name, Root.IP6), gen_specific_filename(name,
                                                                                                               Root.ASN)


def backup_data(name):
    json_file = gen_data_path_extension(Root.SERIALIZED, name, Root.JSON)
    copy_to_history(json_file, Root.RIR, name)
    print('rir stored')


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    backuping_rir()
