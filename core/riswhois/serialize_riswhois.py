from core.file_util import gen_data_dir
from core.json_util import line_to_dict
from core.json_util import save_to_jsonfile
from core.json_util import split_line
from core.root import Root
from core.root_util import print_state


def serialization_riswhois():
    serialization_ris(Root.RISWHO4, Root.RISWHO_STARTLINE)
    serialization_ris(Root.RISWHO6, Root.RISWHO_STARTLINE)
    print_state(Root.SERIALIZE, Root.END, Root.RISWHO)


def serialization_ris(filename, start_at):
    input_file = gen_data_dir(Root.MIRRORED) + filename
    output_file = gen_data_dir(Root.SERIALIZED) + filename
    fields = Root.RISWHO_FIELDS
    delimiter = Root.RISWHO_DELIMITER
    get_data(input_file, output_file, start_at, fields, delimiter)


#####################################################################

def get_data(input_file, output_file, start_at, fields, delimiter):
    # resultant dictionary
    dic = []

    # Write files
    with open(input_file, 'r', encoding='utf8') as file:
        # iterate each line
        for x, line in enumerate(file):

            if x >= start_at - 1:

                description = split_line(line.strip(), delimiter)

                dict_object = line_to_dict(description, fields)

                # for checking type
                # appending the record line to type
                if dict_object[fields[0]] == '% End of dump':
                    break
                dic.append(dict_object)

    # creating json files
    output_file = output_file + ".json"
    save_to_jsonfile(dic, output_file)


def gen_specific_filename(filename, specific):
    return filename + '_' + specific


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    serialization_riswhois()
    exit()

