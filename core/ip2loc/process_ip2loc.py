from core.file_util import gen_data_dir
from core.file_util import gen_data_path_extension
from core.file_util import gen_input_output_path_extension
from core.json_util import aggregate_key
from core.json_util import order_key
from core.json_util import reduce_keys
from core.json_util import read_from_jsonfile
from core.json_util import save_to_jsonfile
from core.root import Root


def processing_ip2loc():
    json_file = gen_data_path_extension(Root.SERIALIZED, Root.IP2LOC4, Root.JSON)
    data = read_from_jsonfile(json_file)
    output_file = gen_data_path_extension(Root.PREPROCESSED, Root.IP2LOC4, Root.JSON)
    reduce_keys(data, Root.IP2LOC_REDUCE_FIELDS, output_file)
    output_file = gen_data_path_extension(Root.AGGREGATED, Root.IP2LOC4, Root.JSON)
    aggregate_key(data, Root.CC, output_file)
    output_file = gen_data_path_extension(Root.ORDERED, Root.IP2LOC4, Root.JSON)
    order_key(data, Root.START, output_file)
    json_file = gen_data_path_extension(Root.SERIALIZED, Root.IP2LOC6, Root.JSON)
    data = read_from_jsonfile(json_file)
    output_file = gen_data_path_extension(Root.PREPROCESSED, Root.IP2LOC6, Root.JSON)
    reduce_keys(data, Root.IP2LOC_REDUCE_FIELDS, output_file)
    output_file = gen_data_path_extension(Root.AGGREGATED, Root.IP2LOC6, Root.JSON)
    aggregate_key(data, Root.CC, output_file)
    output_file = gen_data_path_extension(Root.ORDERED, Root.IP2LOC6, Root.JSON)
    order_key(data, Root.START, output_file)
    print('data preprocessed')


#####################################################################


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    processing_ip2loc()
    exit()
