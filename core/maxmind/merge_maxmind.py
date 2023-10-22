from core.file_util import gen_data_dir
from core.ip_util import ipv4_cidr_to_integer_count
from core.ip_util import ipv6_cidr_to_integer_count
from core.ip_util import networks_intersect
from core.json_util import json_to_dict
from core.json_util import jsonfiles_2_dicts
from core.json_util import save_to_jsonfile
from core.root import Root
from core.root_util import percent_done


def merging_maxmind():
    merge_ip_location(Root.MAXMIND_NAME_LIST[2], Root.MAXMIND_NAME_LIST[4], Root.MAXMIND_MERG_NAME_LIST[0])
    merge_ip_location(Root.MAXMIND_NAME_LIST[3], Root.MAXMIND_NAME_LIST[4], Root.MAXMIND_MERG_NAME_LIST[1])
    merge_asn_ip4(Root.MAXMIND_NAME_LIST[0], Root.MAXMIND_MERG_NAME_LIST[0], Root.MAXMIND_MERG_NAME_LIST[2])
    merge_asn_ip6(Root.MAXMIND_NAME_LIST[1], Root.MAXMIND_MERG_NAME_LIST[1], Root.MAXMIND_MERG_NAME_LIST[3])


def merge_asn_ip4(json1, json2, output):
    import json

    js1 = json_to_dict(json1, gen_data_dir(Root.PREPROCESSED))
    js2 = json_to_dict(json2, gen_data_dir(Root.PROCESSED))

    dic = []
    unmatched = []

    i = 0
    ii = len(js1)
    j = 0
    while i < len(js1):
        percent_done(i, ii)
        json_object1 = js1[i]
        ip1, count1 = ipv4_cidr_to_integer_count(json_object1.get('network'))
        ip1end = ip1 + count1

        while j < len(js2):
            json_object2 = js2[j]
            ip2, count2 = ipv4_cidr_to_integer_count(json_object2.get('network'))
            ip2end = ip2 + count2

            if ip1end < ip2:
                j = 0
                break

            if ip2end < ip1:
                unmatched.append(js2.pop(j))
            elif networks_intersect(network_start=ip1, network_end=ip1end, subnet_start=ip2,
                                    subnet_end=ip2end) or networks_intersect(network_start=ip2, network_end=ip2end,
                                                                             subnet_start=ip1, subnet_end=ip1end):
                dic.append(js2.pop(j))
            else:
                j = j + 1

        j = 0
        js1[i]['subnets'] = dic
        dic = []
        i = i + 1

    if len(js2) > 0:
        unmatched.append(js2.pop())
    output_file = gen_data_dir(Root.ACCUMULATED) + output

    # Write the modified JSON objects to the output file
    with open(gen_data_dir(Root.ACCUMULATED) + 'Subnets_unmatched_IPv4', 'w') as f:
        json.dump(unmatched, f, indent=2)

    print('Saved File: ' + 'Subnets_unmatched')

    with open(output_file, 'w') as f:
        json.dump(js1, f, indent=2)

    print('Saved File: ' + output_file)


def merge_asn_ip6(json1, json2, output):
    import json

    js1 = json_to_dict(json1, gen_data_dir(Root.PREPROCESSED))
    js2 = json_to_dict(json2, gen_data_dir(Root.PROCESSED))

    dic = []
    unmatched = []

    i = 0
    ii = len(js1)
    j = 0
    while i < len(js1):
        percent_done(i, ii)

        json_object1 = js1[i]
        ip1, count1 = ipv6_cidr_to_integer_count(json_object1.get('network'))
        ip1end = ip1 + count1

        while j < len(js2):
            json_object2 = js2[j]
            ip2, count2 = ipv6_cidr_to_integer_count(json_object2.get('network'))
            ip2end = ip2 + count2

            if ip1end < ip2:
                j = 0
                break

            if ip2end < ip1:
                unmatched.append(js2.pop(j))
            elif networks_intersect(network_start=ip1, network_end=ip1end, subnet_start=ip2,
                                    subnet_end=ip2end) or networks_intersect(network_start=ip2, network_end=ip2end,
                                                                             subnet_start=ip1, subnet_end=ip1end):
                dic.append(js2.pop(j))
            else:
                j = j + 1

        j = 0
        js1[i]['subnets'] = dic
        dic = []
        i = i + 1

    if len(js2) > 0:
        unmatched.append(js2.pop())
    output_file = gen_data_dir(Root.ACCUMULATED) + output

    # Write the modified JSON objects to the output file
    with open(gen_data_dir(Root.ACCUMULATED) + 'Subnets_unmatched_IPv6', 'w') as f:
        json.dump(unmatched, f, indent=2)

    print('Saved File: ' + 'Subnets_unmatched')

    with open(output_file, 'w') as f:
        json.dump(js1, f, indent=2)

    print('Saved File: ' + output_file)


def merge_ip_location(json1, json2, output):
    import json

    js1, js2 = jsonfiles_2_dicts(json1, json2, gen_data_dir(Root.PREPROCESSED))

    i = 0
    ii = len(js1)
    for json_object1 in js1:
        percent_done(i, ii)
        i = i + 1
        json_object1['cc'] = json_object1['geoname_id']
        del json_object1['geoname_id']
        json_object1['reg_cc'] = json_object1['registered_country_geoname_id']
        del json_object1['registered_country_geoname_id']
        json_object1['rep_cc'] = json_object1['represented_country_geoname_id']
        del json_object1['represented_country_geoname_id']

        for json_object2 in js2:
            if (json_object1.get('cc') == json_object2.get('geoname_id')):
                json_object1['cc'] = json_object2.get('country_iso_code')
                check = False
                continue

        for json_object2 in js2:
            if (json_object1.get('reg_cc') == json_object2.get('geoname_id')):
                json_object1['reg_cc'] = json_object2.get('country_iso_code')
                check = False
                continue

        for json_object2 in js2:
            if (json_object1.get('rep_cc') == json_object2.get('geoname_id')):
                json_object1['rep_cc'] = json_object2.get('country_iso_code')
                check = False
                continue

    output_file = gen_data_dir(Root.PROCESSED) + output

    # Write the modified JSON objects to the output file
    with open(output_file, 'w') as f:
        json.dump(js1, f, indent=2)

    print('Saved File: ' + output_file)


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    merging_maxmind()
    exit()


