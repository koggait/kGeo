from core.file_util import gen_data_path_extension
from core.json_util import aggregate_by_cc
from core.json_util import read_from_jsonfile
from core.json_util import save_to_jsonfile
from core.root import Root


def aggregation_data():
    asn = gen_data_path_extension(Root.EVALUATION, Root.AS_EXTENDED, Root.JSON)
    output_file = gen_data_path_extension(Root.EVALUATION, Root.AS_EXTENDED_BY_CC, Root.JSON)
    data = read_from_jsonfile(asn)
    aggregated_data = aggregate_by_cc(data, Root.CC)
    save_to_jsonfile(aggregated_data, output_file)


#####################################################################


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    aggregation_data()
    exit()