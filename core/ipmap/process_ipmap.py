from core.file_util import gen_input_output_path_extension
from core.file_util import gen_data_path_extension
from core.json_util import delete_specific_keys
from core.json_util import read_from_jsonfile
from core.json_util import save_to_jsonfile
from core.json_util import aggregate_key
from core.json_util import order_key
from core.json_util import reduce_keys
from core.root import Root


def processing_ipmap():
    json_file = gen_data_path_extension(Root.SERIALIZED, Root.IPMAP, Root.JSON)
    data = read_from_jsonfile(json_file)
    output_file = gen_data_path_extension(Root.PREPROCESSED, Root.IPMAP, Root.JSON)
    reduce_keys(data, Root.IPMAP_REDUCE_FIELDS, output_file)
    output_file = gen_data_path_extension(Root.AGGREGATED, Root.IPMAP, Root.JSON)
    aggregate_key(data, Root.CC, output_file)
    output_file = gen_data_path_extension(Root.ACCUMULATED, Root.IPMAP, Root.JSON)
    aggregate_key(data, 'ip', output_file)
    output_file = gen_data_path_extension(Root.ORDERED, Root.IPMAP, Root.JSON)
    order_key(data, 'ip', output_file)

    print('data')


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    processing_ipmap()
    exit()

