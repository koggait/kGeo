from core.file_util import gen_data_dir
from core.json_util import json_to_dict
from core.json_util import save_to_jsonfile
from core.maxmind.process_maxmind import delete_specific_keys
from core.root import Root
from core.root_util import percent_done


def finalization_maxmind():
    finalize_by_cc(Root.MAXMIND_AGGREGATED[0], Root.MAXMIND_FINAL_IP4)
    finalize_by_cc(Root.MAXMIND_AGGREGATED[1], Root.MAXMIND_FINAL_IP6)
    finalize_by_asn(Root.MAXMIND_AGGREGATED[0], Root.MAXMIND_FINAL_AS[0])
    finalize_by_asn(Root.MAXMIND_AGGREGATED[1], Root.MAXMIND_FINAL_AS[1])
    finalize_merge_by_cc(Root.MAXMIND_NAME_LIST[5], Root.MAXMIND_FINAL_IP4[0], Root.MAXMIND_FINAL_IP6[0])
    finalize_merge_by_cc(Root.MAXMIND_NAME_LIST[6], Root.MAXMIND_FINAL_IP4[1], Root.MAXMIND_FINAL_IP6[1])
    finalize_merge_by_cc(Root.MAXMIND_NAME_LIST[7], Root.MAXMIND_FINAL_IP4[2], Root.MAXMIND_FINAL_IP6[2])
    print('Saved Final Maxmind Files!')


def finalize_merge_by_cc(output_file, json1, json2):
    dict1 = json_to_dict(json1, gen_data_dir(Root.FINAL))
    dict2 = json_to_dict(json2, gen_data_dir(Root.FINAL))
    merged_dict = {}
    for key in set(dict1.keys()).union(dict2.keys()):
        merged_dict[key] = dict1.get(key, []) + dict2.get(key, [])
    sorted_dict = dict(sorted(merged_dict.items()))
    output = gen_data_dir(Root.FINAL) + output_file
    save_to_jsonfile(sorted_dict, output)
    return merged_dict


def finalize_by_cc(filename, output):
    real_cc = get_location_keys()
    reg_cc = get_location_keys()
    rep_cc = get_location_keys()
    json_data = json_to_dict(jsn=filename, dir=gen_data_dir(Root.AGGREGATED))
    ii = len(json_data)
    i = 0
    for asn, json_object in json_data.items():
        percent_done(i, ii)
        i = i + 1

        json_object_network = json_object['networks']
        for json_networks in json_object_network:

            json_subnets = json_networks['subnets']

            for subnet in json_subnets:

                if subnet['cc'] != "":
                    real_cc[subnet['cc']].add(int(json_object[Root.MAXASNFIELDS[1]]))
                if subnet['reg_cc'] != "":
                    reg_cc[subnet['reg_cc']].add(int(json_object[Root.MAXASNFIELDS[1]]))
                if subnet['rep_cc'] != "":
                    rep_cc[subnet['rep_cc']].add(int(json_object[Root.MAXASNFIELDS[1]]))
    for key in real_cc:
        tmp = list(real_cc[key])
        tmp.sort()
        real_cc[key] = tmp
    for key in reg_cc:
        tmp = list(reg_cc[key])
        tmp.sort()
        reg_cc[key] = tmp
    for key in rep_cc:
        tmp = list(rep_cc[key])
        tmp.sort()
        rep_cc[key] = tmp
    save_to_jsonfile(real_cc, gen_data_dir(Root.FINAL) + output[0])
    save_to_jsonfile(reg_cc, gen_data_dir(Root.FINAL) + output[1])
    save_to_jsonfile(rep_cc, gen_data_dir(Root.FINAL) + output[2])


def finalize_by_asn(filename, output):
    dic = {}

    json_data = json_to_dict(jsn=filename, dir=gen_data_dir(Root.AGGREGATED))
    ii = len(json_data)
    i = 0
    for asn, json_object in json_data.items():
        percent_done(i, ii)
        i = i + 1

        real_cc = set()
        reg_cc = set()
        rep_cc = set()

        json_object_network = json_object['networks']
        for json_networks in json_object_network:

            json_subnets = json_networks['subnets']

            for subnet in json_subnets:

                if subnet['cc'] != "":
                    real_cc.add(subnet['cc'])
                if subnet['reg_cc'] != "":
                    reg_cc.add(subnet['reg_cc'])
                if subnet['rep_cc'] != "":
                    rep_cc.add(subnet['rep_cc'])

        real_cc_list = list(real_cc)
        real_cc_list.sort()
        reg_cc_list = list(reg_cc)
        reg_cc_list.sort()
        rep_cc_list = list(rep_cc)
        rep_cc_list.sort()

        dic[asn] = {'cc': real_cc_list, 'reg_cc': reg_cc_list, 'rep_cc': rep_cc_list}

    save_to_jsonfile(dic, gen_data_dir(Root.ORDERED) + output)


def get_location_keys():
    json_loc_data = json_to_dict(jsn=Root.MAXMIND_NAME_LIST[4], dir=gen_data_dir(Root.PREPROCESSED))
    json_loc_data = delete_specific_keys(json_loc_data, ['geoname_id'])

    json_list = {}
    for json_object in json_loc_data:
        dic = {}
        dic[Root.MAXCOUNTRYLOCFIELDS[4]] = json_object[Root.MAXCOUNTRYLOCFIELDS[4]]
        json_list[json_object[Root.MAXCOUNTRYLOCFIELDS[4]]] = set()

    sorted_json_loc_data = dict(sorted(json_list.items()))
    return sorted_json_loc_data


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    finalization_maxmind()
    exit()
