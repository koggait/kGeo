from core.file_util import gen_data_dir
from core.file_util import gen_data_path_file
from core.file_util import gen_file_extension
from core.json_util import delete_specific_keys
from core.json_util import read_from_jsonfile
from core.json_util import save_to_jsonfile
from core.root import Root
from core.root_util import print_state


def serialization_peeringdb():
    file = gen_data_dir(Root.MIRRORED) + Root.PEERINGDB
    data = read_from_jsonfile(file)
    save_to_jsonfile(data['data'], gen_data_path_file(Root.SERIALIZED, gen_file_extension(Root.PEERINGDB, Root.JSON)))
    print_state(Root.SERIALIZE, Root.END, Root.PEERINGDB)


#####################################################################


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    serialization_peeringdb()
    exit()

