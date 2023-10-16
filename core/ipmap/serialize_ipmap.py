from core.file_util import gen_data_dir
from core.root import Root
from core.root_util import print_state


def serialization_ipmap():
    name = gen_data_dir(Root.MIRRORED) + Root.IPMAP
    serialize_data(name, Root.IPMAP)
    print_state(Root.SERIALIZE, Root.END, Root.IPMAP)


def serialize_data(filename, name):
    import json

    dict1 = []

    # fields in the sample file
    originfields = ['ip', 'geolocation_id', 'city_name', 'state_name', 'country_name', 'country_code_alpha2',
                    'country_code_alpha3', 'latitude', 'longitude', 'score']
    fields = ['ip', 'geolocation_id', 'city_name', 'state_name', 'country_name', 'cc',
              'country_code_alpha3', 'latitude', 'longitude', 'score']

    with open(filename, 'rb') as file:
        lines = file.readlines()
    file.close()

    with open(filename, 'rb') as file:

        xLen = len(lines)
        x = 0

        for line in file:

            x = x + 1
            y = xLen - x
            print('Lines Left: ' + str(y))

            description = []
            # reading line by line from core.the text file
            d = list(line.decode('utf8').strip().split(',', 9))
            description = d

            # loop variable
            i = 0
            # intermediate dictionary
            dict2 = {}
            while i < len(fields):
                # creating dictionary for each entry
                dict2[fields[i]] = description[i]
                i = i + 1

            dict1.append(dict2)

    # creating json file
    path = gen_data_dir(Root.SERIALIZED) + str(name) + ".json"
    print('Creating JSON File: ' + path)
    out_file = open(path, "w")
    json.dump(dict1, out_file, indent=4)
    out_file.close()


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    serialization_ipmap()
    exit()

