from core.file_util import gen_data_dir
from core.file_util import gen_data_path_extension
from core.json_util import keep_specific_keys
from core.json_util import read_from_jsonfile
from core.json_util import save_to_jsonfile
from core.json_util import aggregate_key
from core.json_util import order_key
from core.json_util import reduce_keys
from core.json_util import filter_keys
from core.root import Root


def processing_peeringdb():
    json_file = gen_data_path_extension(Root.SERIALIZED, Root.PEERINGDB, Root.JSON)
    data = read_from_jsonfile(json_file)
    output_file = gen_data_path_extension(Root.PREPROCESSED, Root.PEERINGDB, Root.JSON)
    filter_keys(data, Root.PEERINGDB_KEEP_FIELDS, output_file)
    output_file = gen_data_path_extension(Root.ORDERED, Root.PEERINGDB, Root.JSON)
    order_key(data, Root.PEERINGDB_KEEP_FIELDS[0], output_file)
    print('data preprocessed')


#####################################################################


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    processing_peeringdb()
    exit()

