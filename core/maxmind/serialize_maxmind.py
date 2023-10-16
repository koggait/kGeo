from core.file_util import gen_data_dir
from core.file_util import getname
from core.root import Root
from core.root_runtime import RootRuntime
from core.root_util import print_state


def serialization_maxmind():
    serialize_data(RootRuntime.MAXASNLIST, Root.MAXASNFIELDS)
    serialize_data(RootRuntime.MAXCOUNTRYLOCLIST, Root.MAXCOUNTRYLOCFIELDS)
    serialize_data(RootRuntime.MAXCOUNTRYLIST, Root.MAXCOUNTRYFIELDS)
    print_state(Root.SERIALIZE, Root.END, Root.MAXMIND)


#####################################################################

def serialize_data(mmList, mmFields):
    for m in mmList:
        name = gen_data_dir(Root.MIRRORED) + m
        getData(name, getname(m), mmFields)


def getData(csvFile, name, fields):
    import json

    # resultant dictionaries 
    dictSet = []

    # read file
    with open(csvFile, 'r', encoding='utf-8') as cFile:
        # read and store all lines into list
        x = 0
        # iterate each line
        for line in cFile:
            x = x + 1
            if x > 1:

                description = list(line.strip().split(','))

                if (description[len(fields) - 1].startswith('\"') or description[len(fields) - 1].endswith('\"')):
                    description[len(fields) - 1] = description[len(fields) - 1].replace('"', '')

                i = 0
                # intermediate dictionary
                dictObject = {}
                while i < len(fields):
                    # creating dictionary for each entry

                    dictObject[fields[i]] = description[i]
                    i = i + 1

                dictSet.append(dictObject)

    # creating json file
    pathJson = gen_data_dir(Root.SERIALIZED) + str(name)
    print('Creating JSON File: ' + pathJson)
    out_file = open(pathJson, "w", encoding='utf-8')
    json.dump(dictSet, out_file, indent=4)
    out_file.close()
    print('Saved File: ' + pathJson)


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    serialization_maxmind()
    exit()

