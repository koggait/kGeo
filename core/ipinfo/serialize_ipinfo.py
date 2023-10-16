from core.file_util import gen_data_path_extension
from core.file_util import gen_data_path_file
from core.json_util import load_multiple_from_jsonfile
from core.json_util import save_to_jsonfile
from core.root import Root
from core.root_util import print_state


def serialization_ipinfo():
    data = load_multiple_from_jsonfile(gen_data_path_file(Root.MIRRORED, Root.IPINFO_COUNTRY_ASN))
    save_to_jsonfile(data, gen_data_path_extension(Root.SERIALIZED, Root.IPINFO_COUNTRY_ASN, Root.JSON))
    print_state(Root.SERIALIZE, Root.END, Root.IPINFO)


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    serialization_ipinfo()
    exit()
