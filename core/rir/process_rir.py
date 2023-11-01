from core.file_util import gen_data_dir
from core.file_util import gen_file_extension
from core.file_util import gen_specific_filename
from core.file_util import gen_data_path_extension
from core.json_util import reduce_keys
from core.json_util import read_from_jsonfile
from core.json_util import save_to_jsonfile
from core.json_util import transfer_specific_objects
from core.json_util import order_key
from core.json_util import aggregate_key
from core.root import Root
from core.root_util import print_state


def processing_rir():
    for name in Root.RIR_SET_STARTLINE.keys():
        rir4, rir6, rirasn = slice_rir_data(name)
        output4, output6, outputasn = slice_rir_output(name, Root.PREPROCESSED)
        reduce_keys(rir4, Root.RIR_STATS_REDUCE_FIELDS, output4)
        reduce_keys(rir6, Root.RIR_STATS_REDUCE_FIELDS, output6)
        reduce_keys(rirasn, Root.RIR_STATS_REDUCE_FIELDS, outputasn)
        output4, output6, outputasn = slice_rir_output(name, Root.AGGREGATED)
        aggregate_key(rir4, Root.CC, output4)
        aggregate_key(rir6, Root.CC, output6)
        aggregate_key(rirasn, Root.CC, outputasn)
        output4, output6, outputasn = slice_rir_output(name, Root.ORDERED)
        order_key(rir4, Root.START, output4)
        order_key(rir6, Root.START, output6)
        order_key(rirasn, Root.START, outputasn)

    print_state(Root.SERIALIZE, Root.END, Root.RIR)

    print('data preprocessed')


#####################################################################


def split_reduce_objects(name, key, value):
    json_file = gen_data_dir(Root.PREPROCESSED) + name
    output_file = gen_data_dir(Root.PROCESSED) + name
    bad_output_file = gen_data_dir(Root.PROCESSED) + 'bad_' + name
    data = read_from_jsonfile(json_file)
    data, bad_data = transfer_specific_objects(data, key, value)
    save_to_jsonfile(data, output_file)
    save_to_jsonfile(bad_data, bad_output_file)
    print('Processed good & bad Files: ' + output_file)


def slice_rir_data(filename):
    rir4 = gen_specific_filename(filename=filename, specific=Root.IP_VER_4)
    json_file = gen_data_path_extension(Root.SERIALIZED, rir4, Root.JSON)
    data4 = read_from_jsonfile(json_file)
    rir6 = gen_specific_filename(filename=filename, specific=Root.IP_VER_6)
    json_file = gen_data_path_extension(Root.SERIALIZED, rir6, Root.JSON)
    data6 = read_from_jsonfile(json_file)
    rirasn = gen_specific_filename(filename=filename, specific=Root.ASN)
    json_file = gen_data_path_extension(Root.SERIALIZED, rirasn, Root.JSON)
    dataasn = read_from_jsonfile(json_file)
    return data4, data6, dataasn


def slice_rir_output(filename, directory):
    rir4, rir6, rirasn = slice_rir(filename)
    output4 = gen_data_path_extension(directory, rir4, Root.JSON)
    output6 = gen_data_path_extension(directory, rir6, Root.JSON)
    outputasn = gen_data_path_extension(directory, rirasn, Root.JSON)
    return output4, output6, outputasn


def slice_rir(filename):
    rir4 = gen_specific_filename(filename=filename, specific=Root.IP_VER_4)
    rir6 = gen_specific_filename(filename=filename, specific=Root.IP_VER_6)
    rirasn = gen_specific_filename(filename=filename, specific=Root.ASN)
    return rir4, rir6, rirasn


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    processing_rir()
