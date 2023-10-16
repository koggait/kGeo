from core.file_util import gen_data_dir
from core.file_util import gen_data_path_file
from core.file_util import gen_file_extension
from core.root import Root
from core.root_util import print_state


def serialization_ip2loc():
    serialize_data(gen_data_path_file(Root.MIRRORED, Root.IP2LOC4CSV), Root.IP2LOC4, Root.IP2LOC_FIELDS, )
    serialize_data(gen_data_path_file(Root.MIRRORED, Root.IP2LOC6CSV), Root.IP2LOC6, Root.IP2LOC_FIELDS, )
    print_state(Root.SERIALIZE, Root.END, Root.IP2LOC)


def serialize_data(csvFile, name, fields):
    import json

    # resultant dictionaries
    dictSet = []

    # read file
    with open(csvFile, 'r', encoding='utf-8') as cFile:
        # read and store all lines into list
        # iterate each line
        for line in cFile:

            description = list(line.strip().split(','))
            if (description[len(fields) - 1].startswith('\"') or description[len(fields) - 1].endswith('\"')):
                description[len(fields) - 1] = description[len(fields) - 1].replace('"', '')

            i = 0
            # intermediate dictionary
            dictObject = {}
            while i < len(fields):
                # creating dictionary for each entry
                description[i] = description[i].replace('"', '')
                dictObject[fields[i]] = description[i].replace('\"', '')
                i = i + 1

            dictSet.append(dictObject)

    # creating json file
    pathJson = gen_data_dir(Root.SERIALIZED) + gen_file_extension(str(name), Root.JSON)
    print('Creating JSON File: ' + pathJson)
    out_file = open(pathJson, "w", encoding='utf-8')
    json.dump(dictSet, out_file, indent=4)
    out_file.close()
    print('Saved File: ' + pathJson)


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    serialization_ip2loc()
