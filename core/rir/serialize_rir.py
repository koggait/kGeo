from core.file_util import gen_file_extension
from core.file_util import gen_input_output_path_files
from core.file_util import gen_specific_filename
from core.json_util import line_to_dict
from core.json_util import save_to_jsonfile
from core.json_util import split_line
from core.root import Root
from core.root_util import print_state


def serialization_rir():
    for name in Root.RIR_SET_STARTLINE.keys():
        serialize_data(name, Root.RIR_SET_STARTLINE[name])
    print_state(Root.SERIALIZE, Root.END, Root.RIR)


def serialize_data(filename, start_at):
    input_file, output_file = gen_input_output_path_files(filename, Root.MIRRORED, Root.SERIALIZED)
    get_data(input_file, output_file, start_at, fields=Root.RIR_STATS_FIELDS, delimiter=Root.RIR_STATS_DELIMITER)
    print('data serialized')


#####################################################################

def get_data(input_file, output_file, start_at, fields, delimiter):
    # resultant dictionary
    dict_ip4 = []
    dict_asn = []
    dict_ip6 = []

    # Write files
    with open(input_file, 'r') as file:
        # iterate each line
        for x, line in enumerate(file):

            if x >= start_at:
                value_list = split_line(line, delimiter)
                dict_object = line_to_dict(value_list, fields)

                choose_dictionary_by_type(value_list, dict_asn, dict_ip4, dict_ip6, dict_object)

    # creating json files
    output_file_ip4, output_file_ip6, output_file_asn = slice_rir_types(output_file)
    save_to_jsonfile(dict_ip4, output_file_ip4)
    save_to_jsonfile(dict_asn, output_file_asn)
    save_to_jsonfile(dict_ip6, output_file_ip6)


# for checking type
# appending the record line to type
def choose_dictionary_by_type(value_list, dict_asn, dict_ip4, dict_ip6, dict_object):
    if value_list[2] == Root.IP4:
        dict_ip4.append(dict_object)
    if value_list[2] == Root.ASN:
        dict_asn.append(dict_object)
    if value_list[2] == Root.IP6:
        dict_ip6.append(dict_object)


def slice_rir_types(filename):
    rir4 = gen_specific_filename(filename=filename, specific=gen_file_extension(Root.IP4, Root.JSON))
    rir6 = gen_specific_filename(filename=filename, specific=gen_file_extension(Root.IP6, Root.JSON))
    rirasn = gen_specific_filename(filename=filename, specific=gen_file_extension(Root.ASN, Root.JSON))
    return rir4, rir6, rirasn


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    serialization_rir()
