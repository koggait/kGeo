from core.file_util import gen_data_path_extension
from core.file_util import gen_good_bad_path_extension
from core.file_util import gen_input_output_path_extension
from core.json_util import reduce_keys
from core.json_util import delete_specific_objects
from core.json_util import read_from_jsonfile
from core.json_util import save_to_jsonfile
from core.json_util import transfer_specific_objects
from core.json_util import transform_key_to_primary
from core.root import Root


def processing_riswhois():
    input_file, output_file = gen_input_output_path_extension(Root.RISWHO4, Root.SERIALIZED, Root.PREPROCESSED,
                                                              Root.JSON)
    data4 = read_from_jsonfile(input_file)
    reduce_keys(data4, Root.RISWHO_REDUCE_FIELDS, output_file)
    input_file, output_file = gen_input_output_path_extension(Root.RISWHO6, Root.SERIALIZED, Root.PREPROCESSED,
                                                              Root.JSON)
    data6 = read_from_jsonfile(input_file)
    reduce_keys(data6, Root.RISWHO_REDUCE_FIELDS, output_file)

    input_file = gen_data_path_extension(Root.PREPROCESSED, Root.RISWHO4, Root.JSON)
    output_file_good, output_file_bad = gen_good_bad_path_extension(Root.RISWHO4, Root.PREPROCESSED, Root.JSON)
    split_reduce_objects(input_file, Root.RISWHO_FIELDS[1], Root.RISWHO4_REDUCE_OBJECTS, output_file_good,
                         output_file_bad)

    input_file = gen_data_path_extension(Root.PREPROCESSED, Root.RISWHO6, Root.JSON)
    output_file_good, output_file_bad = gen_good_bad_path_extension(Root.RISWHO6, Root.PREPROCESSED, Root.JSON)
    split_reduce_objects(input_file, Root.RISWHO_FIELDS[1], Root.RISWHO6_REDUCE_OBJECTS, output_file_good,
                         output_file_bad)

    input_file = gen_data_path_extension(Root.PREPROCESSED, Root.RISWHO4GOOD, Root.JSON)
    output_file = gen_data_path_extension(Root.PROCESSED, Root.RISWHO4, Root.JSON)
    input_data = read_from_jsonfile(input_file)
    riswhois4 = transform_key_to_primary(input_data, Root.RISWHO_FIELDS[0])
    sorted_riswhois4 = dict(sorted(riswhois4.items()))
    save_to_jsonfile(sorted_riswhois4, output_file)

    input_file = gen_data_path_extension(Root.PREPROCESSED, Root.RISWHO6GOOD, Root.JSON)
    output_file = gen_data_path_extension(Root.PROCESSED, Root.RISWHO6, Root.JSON)
    input_data = read_from_jsonfile(input_file)
    riswhois6 = transform_key_to_primary(input_data, Root.RISWHO_FIELDS[0])
    sorted_riswhois6 = dict(sorted(riswhois6.items()))
    save_to_jsonfile(sorted_riswhois6, output_file)
    print('data preprocessed')


def append_to_or_init_key(json_dic, number, json_value):
    if number not in json_dic:
        json_dic[number] = []
        json_dic[number].append(json_value)
    else:
        json_dic[number].append(json_value)


def reduce_objects(input_file, key, value, output_file):
    data = read_from_jsonfile(input_file)
    data, removedData = delete_specific_objects(data, key, value)
    save_to_jsonfile(data, output_file)
    print('Preprocessed File: ' + output_file)


def split_reduce_objects(input_file, key, value, output_file_good, output_file_bad):
    data = read_from_jsonfile(input_file)
    good_data, bad_data = transfer_specific_objects(data, key, value)
    save_to_jsonfile(data, output_file_good)
    save_to_jsonfile(bad_data, output_file_bad)
    print('Preprocessed Files: ' + output_file_good + ' and ' + output_file_bad)


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    processing_riswhois()
    exit()

