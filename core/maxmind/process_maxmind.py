from core.file_util import gen_data_dir
from core.file_util import getname
from core.json_util import delete_specific_keys
from core.json_util import read_from_jsonfile
from core.json_util import save_to_jsonfile
from core.root import Root
from core.root_runtime import RootRuntime


def processing_maxmind():
    maxasn = [Root.MAXMIND_NAME_LIST[0], Root.MAXMIND_NAME_LIST[1]]
    reduce_keys(maxasn, [])
    reduce_keys(RootRuntime.MAXCOUNTRYLIST, Root.MAXCOUNTRYP_REDUCE_FIELDS)
    reduce_keys(RootRuntime.MAXCOUNTRYLOCLIST, Root.MAXCOUNTRYLOC_REDUCE_FIELDS)
    print('data preprocessed')


#####################################################################

def reduce_keys(mmList, keys_to_delete):
    for m in mmList:
        name = getname(m)
        json_file = gen_data_dir(Root.SERIALIZED) + name
        output_file = gen_data_dir(Root.PREPROCESSED) + name
        data = read_from_jsonfile(json_file)
        data = delete_specific_keys(data, keys_to_delete)
        save_to_jsonfile(data, output_file)


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    processing_maxmind()
    exit()

