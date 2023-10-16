from core.file_util import gen_data_dir
from core.file_util import gen_specific_filename
from core.file_util import gen_data_path_extension
from core.json_util import delete_specific_keys
from core.json_util import load_multiple_from_jsonfile
from core.json_util import read_from_jsonfile
from core.json_util import save_to_jsonfile
from core.json_util import aggregate_key
from core.json_util import order_key
from core.json_util import reduce_keys
from core.root import Root


def processing_ipinfo():
    json_file = gen_data_path_extension(Root.SERIALIZED, Root.IPINFO_COUNTRY_ASN, Root.JSON)
    data = read_from_jsonfile(json_file)
    output_file = gen_data_path_extension(Root.PREPROCESSED, Root.IPINFO_COUNTRY_ASN, Root.JSON)
    reduce_keys(data, Root.IPINFO_REDUCE_FIELDS, output_file)
    output_file = gen_data_path_extension(Root.AGGREGATED, Root.IPINFO_COUNTRY_ASN, Root.JSON)
    aggregate_key(data, Root.COUNTRY, output_file)
    name = gen_specific_filename(Root.IPINFO_COUNTRY_ASN, 'byAS')
    output_file = gen_data_path_extension(Root.ORDERED, name, Root.JSON)
    aggregate_key(data, Root.ASN, output_file)
    name = gen_specific_filename(Root.IPINFO_COUNTRY_ASN, 'byIP')
    output_file = gen_data_path_extension(Root.ORDERED, name, Root.JSON)
    order_key(data, Root.STARTIP, output_file)
    print('data preprocessed')


def sort_json_value_list(dic):
    for key in dic:
        tmp = list(dic[key])
        tmp.sort()
        dic[key] = tmp
    return dic


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    processing_ipinfo()
    exit()

