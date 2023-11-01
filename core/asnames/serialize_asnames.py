from core.file_util import gen_data_path_extension
from core.file_util import gen_data_path_file
from core.json_util import line_to_dict
from core.json_util import save_to_jsonfile
from core.root import Root
from core.root_util import print_state


def serialization_asnames():
    input_file = gen_data_path_file(Root.MIRRORED, Root.ASNAMES)
    output_file = gen_data_path_extension(Root.SERIALIZED, Root.ASNAMES, Root.JSON)
    data = serialize_data(input_file)
    save_to_jsonfile(data, output_file)
    print_state(Root.SERIALIZE, Root.END, Root.ASNAMES)


#####################################################################
def serialize_data(filename):
    dic = []
    # fields in the sample file
    fields = Root.ASNAMES_FIELDS

    # split each line into values and append to dictionary
    with open(filename) as file:
        for line in file:
            value_list = _split_line_to_value_list(line)
            dict_object = line_to_dict(value_list, fields)
            dic.append(dict_object)

    # return json dictionary
    return dic


def _split_line_to_value_list(line):
    # reading line by line from the text file
    as_number = list(line.strip().split(' ', 1))
    as_list_name_cc = list(as_number[1].strip().rsplit(', ', 1))
    if len(as_list_name_cc) == 1:
        as_list_name_cc = ['-', '-']
    return [as_number[0], as_list_name_cc[0], as_list_name_cc[1]]


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    serialization_asnames()
