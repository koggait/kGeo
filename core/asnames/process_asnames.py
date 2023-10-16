from core.root_util import print_state
from core.file_util import gen_data_path_extension
from core.json_util import save_to_jsonfile
from core.json_util import transform_key_to_primary
from core.json_util import aggregate_by_cc
from core.json_util import read_from_jsonfile
from core.root import Root


def processing_asnames():
    input_file = gen_data_path_extension(directory_type=Root.SERIALIZED, filename=Root.ASNAMES, extension=Root.JSON)

    # no fields reduced

    # no objects reduced
    input_data = read_from_jsonfile(input_file)
    data = aggregate_by_cc(input_data, Root.CC)
    output_file = gen_data_path_extension(directory_type=Root.AGGREGATED, filename=Root.ASNAMES, extension=Root.JSON)
    save_to_jsonfile(data, output_file)

    input_data = read_from_jsonfile(input_file)
    data = transform_key_to_primary(input_data, Root.ASNUMBER)
    output_file = gen_data_path_extension(directory_type=Root.ORDERED, filename=Root.ASNAMES, extension=Root.JSON)
    save_to_jsonfile(data, output_file)

    print_state(Root.PROCESSED, Root.END, Root.ASNAMES)

if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    processing_asnames()
