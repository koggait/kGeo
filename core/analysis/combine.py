from core.file_util import gen_data_dir
from core.file_util import gen_data_path_file
from core.file_util import gen_data_path_extension
from core.ip_util import ipv4_cidr_to_integer_count
from core.ip_util import ipv4_to_integer
from core.ip_util import ipv6_cidr_to_integer_count
from core.ip_util import networks_intersect
from core.json_util import read_from_jsonfile
from core.json_util import save_to_jsonfile
from core.root import Root
from core.root_util import percent_done


def combining_data():
    rir4 = gen_data_path_extension(Root.PREPROCESSED, Root.NRO4, Root.JSON)
    rir6 = gen_data_path_extension(Root.PREPROCESSED, Root.NRO6, Root.JSON)
    max4 = gen_data_path_file(Root.PROCESSED, Root.MAXMIND_MERG_NAME_LIST[0])
    max6 = gen_data_path_file(Root.PROCESSED, Root.MAXMIND_MERG_NAME_LIST[1])

    rir4 = read_from_jsonfile(rir4)
    rir6 = read_from_jsonfile(rir6)
    max4 = read_from_jsonfile(max4)
    max6 = read_from_jsonfile(max6)

    output4 = gen_data_path_extension(Root.EVALUATION, 'rir_x_max_4', Root.JSON)
    output6 = gen_data_path_extension(Root.EVALUATION, 'rir_x_max_6', Root.JSON)

    merge_asn_ip4(rir4, max4, output4)
    merge_asn_ip6(rir6, max6, output6)

    print('data merged: asnames X rir_asn X bgppath')


#####################################################################


def merge_asn_ip4(js1, js2, output):
    import json

    merged = {}

    unmatched = []

    i = 0
    ii = len(js1)
    j = 0
    k = 0

    while i < len(js1):
        percent_done(i, ii)

        json_object1 = js1[i]
        ip4 = json_object1['start']
        if ip4 == '57.231.0.0':
            print('s')
        ip1 = ipv4_to_integer(ip4)
        count1 = json_object1['value']
        ip1end = ip1 + int(count1)-1

        while j < len(js2):
            json_object2 = js2[j]
            ip2, count2 = ipv4_cidr_to_integer_count(json_object2.get('network'))
            ip2end = ip2 + int(count2) -1

            if ip1end < ip2:
                j = 0
                break
            if ip2end < ip1:
                unmatched.append(js2.pop(j))

            if networks_match(ip1, ip1end, ip2, ip2end):

                jobj = js2.pop(j)
                if 'geonets' in merged.keys():
                    merged['geonets'].append(jobj['network'])
                else:
                    merged['geonets'] = []
                    merged['geonets'].append(jobj['network'])
                merged['real-cc'] = jobj['cc']
                merged['reg-cc'] = jobj['reg_cc']
                merged['repcc'] = jobj['rep_cc']
            else:
                j = j + 1

        j = 0
        js1[i].update(merged)
        merged = {}
        i = i + 1
    if len(js2) > 0:
        unmatched.append(js2.pop())

    # Write the modified JSON objects to the output file
    with open(gen_data_dir(Root.EVALUATION) + 'Subnets_unmatched_IPv4', 'w') as f:
        json.dump(unmatched, f, indent=2)

    print('Saved File: ' + 'Subnets_unmatched')

    with open(output, 'w') as f:
        json.dump(js1, f, indent=2)

    print('Saved File: ' + output)


def networks_match(ip1, ip1end, ip2, ip2end):
    return networks_intersect(network_start=ip1, network_end=ip1end, subnet_start=ip2,
                              subnet_end=ip2end) or networks_intersect(network_start=ip2, network_end=ip2end,
                                                                       subnet_start=ip1, subnet_end=ip1end)


def merge_asn_ip6(js1, js2, output):
    import json

    merged = {}

    unmatched = []

    i = 0
    ii = len(js1)
    j = 0
    while i < len(js1):
        percent_done(i, ii)

        json_object1 = js1[i]
        ip1, count1 = ipv6_cidr_to_integer_count(json_object1.get('start') + '/' + json_object1.get('value'))
        ip1end = ip1 + int(count1) - 1

        while j < len(js2):
            json_object2 = js2[j]
            ip2, count2 = ipv6_cidr_to_integer_count(json_object2.get('network'))
            ip2end = ip2 + int(count2) - 1

            if ip1end < ip2:
                j = 0
                break

            if ip2end < ip1:
                unmatched.append(js2.pop(j))
            elif networks_intersect(network_start=ip1, network_end=ip1end, subnet_start=ip2,
                                    subnet_end=ip2end) or networks_intersect(network_start=ip2, network_end=ip2end,
                                                                             subnet_start=ip1, subnet_end=ip1end):
                jobj = js2.pop(j)

                if 'geonets' in merged.keys():
                    merged['geonets'].append(jobj['network'])
                else:
                    merged['geonets'] = []
                    merged['geonets'].append(jobj['network'])
                merged['real-cc'] = jobj['cc']
                merged['reg-cc'] = jobj['reg_cc']
                merged['repcc'] = jobj['rep_cc']
            else:
                j = j + 1

        j = 0
        js1[i].update(merged)
        merged = {}
        i = i + 1
    if len(js2) > 0:
        unmatched.append(js2.pop())

    # Write the modified JSON objects to the output file
    with open(gen_data_dir(Root.EVALUATION) + 'Subnets_unmatched_IPv6', 'w') as f:
        json.dump(unmatched, f, indent=2)

    print('Saved File: ' + 'Subnets_unmatched')

    with open(output, 'w') as f:
        json.dump(js1, f, indent=2)

    print('Saved File: ' + output)


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    combining_data()
    exit()
