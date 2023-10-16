from core.file_util import gen_data_dir
from core.json_util import json_to_dict
from core.json_util import save_to_jsonfile
from core.root import Root
from core.root_util import percent_done


def aggregation_maxmind():
    js1 = json_to_dict(Root.MAXMIND_MERG_NAME_LIST[2], gen_data_dir(Root.ACCUMULATED))
    aggregate_as_data(js1, Root.MAXMIND_AGGREGATED[0])
    js2 = json_to_dict(Root.MAXMIND_MERG_NAME_LIST[3], gen_data_dir(Root.ACCUMULATED))
    aggregate_as_data(js2, Root.MAXMIND_AGGREGATED[1])

    print('data aggregated by AS')


#####################################################################

def aggregate_as_data(data, output_file):
    NETWORKS = 'networks'
    SUBNETS = 'subnets'

    json_list = {}
    i = 0
    ii = len(data)
    for json_object in data:
        percent_done(i, ii)
        i = i + 1
        for key in json_object:
            if key == Root.MAXASNFIELDS[1]:
                if int(json_object[key]) not in json_list:
                    dic = {}

                    # autonomous_system_number = NUMBER
                    dic[Root.MAXASNFIELDS[1]] = json_object[key]
                    # autonomous_system_organization = NAME
                    dic[Root.MAXASNFIELDS[2]] = json_object[Root.MAXASNFIELDS[2]]
                    dic[NETWORKS] = []

                    net_dic = {}
                    # network = NETWORK
                    net_dic[Root.MAXASNFIELDS[0]] = json_object[Root.MAXASNFIELDS[0]]
                    # subnets = [{subnets}]
                    net_dic[SUBNETS] = json_object[SUBNETS]

                    dic[NETWORKS].append(net_dic)

                    json_list[int(json_object[key])] = dic

                else:
                    net_dic = {}
                    # network = NETWORK
                    net_dic[Root.MAXASNFIELDS[0]] = json_object[Root.MAXASNFIELDS[0]]
                    # subnets = [{subnets}]
                    net_dic[SUBNETS] = json_object[SUBNETS]
                    json_list[int(json_object[key])][NETWORKS].append(net_dic)

    sorted_json_list = dict(sorted(json_list.items()))
    output_file = gen_data_dir(Root.AGGREGATED) + output_file
    save_to_jsonfile(sorted_json_list, output_file)
    print('Saved File: ' + output_file)


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    aggregation_maxmind()
    exit()
