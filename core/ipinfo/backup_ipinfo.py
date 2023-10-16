from core.file_util import gen_data_path_extension
from core.mirror_util import copy_to_history
from core.root import Root


def backuping_ipinfo():
    json_file = gen_data_path_extension(Root.SERIALIZED, Root.IPINFO_COUNTRY_ASN, Root.JSON)
    directory = Root.IPINFO
    filename = Root.IPINFO
    copy_to_history(json_file, directory, filename)
    print('maxmind stored')


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    backuping_ipinfo()
