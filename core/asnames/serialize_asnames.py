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
            description = split_line_asnames(line)
            dict_object = line_to_dict(description, fields)
            dic.append(dict_object)

    # return json dictionary
    return dic


def split_line_asnames(line):
    # reading line by line from core.the text file
    d = list(line.strip().split(' ', 1))
    e = list(d[1].strip().rsplit(', ', 1))
    if len(e) == 1:
        e = ['-', '-']
    return [d[0], e[0], e[1]]


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    serialization_asnames()
