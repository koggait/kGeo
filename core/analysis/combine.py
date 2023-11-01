from core.file_util import gen_data_path_file
from core.file_util import gen_data_path_extension
from core.json_util import read_from_jsonfile
from core.json_util import merge_rir_max_ip
from core.file_util import gen_merge_filename
from core.file_util import gen_specific_filename
from core.root import Root
from core.root_util import print_state
from core.root import MAXMIND_PATH

VER = 'version'
NAME = 'name'

IPV4 = {
    VER: 4,
    NAME: 'IPv4'
}

IPV6 = {
    VER: 6,
    NAME: 'IPv6'
}


def combining_data():
    relate_rir_maxmind_by_ip(rir_name=Root.NRO4, ipv=IPV4)
    relate_rir_maxmind_by_ip(rir_name=Root.NRO6, ipv=IPV6)
    print_state(phase=Root.RELATE, state=Root.COMPLETE, text=gen_specific_filename(Root.NRO, Root.MAXMIND[Root.NAME]))


def relate_rir_maxmind_by_ip(rir_name, ipv):
    rir = gen_data_path_extension(directory_type=Root.PREPROCESSED, filename=rir_name, extension=Root.JSON)
    rir = read_from_jsonfile(rir)
    maxmind = gen_data_path_extension(directory_type=Root.PROCESSED, filename=MAXMIND_PATH(DB=Root.MAXMIND[Root.VER], DATASET=Root.MAXMIND_DB[Root.MAXCOUNTRYLOC], IPVER=ipv[NAME]), extension=Root.JSON)
    maxmind = read_from_jsonfile(maxmind)
    merge_name = gen_merge_filename(rir_name, Root.MAXMIND[Root.NAME], ipv[NAME])
    output = gen_data_path_extension(directory_type=Root.EVALUATION, filename=merge_name, extension=Root.JSON)
    merge_rir_max_ip(rir, maxmind, output, ipv[VER])
    print_state(phase=Root.RELATE, state=Root.END, text=output)


#####################################################################


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    combining_data()
    exit()



'''def merge_asn_ip6(js1, js2, output, ipv):
    import json

    merged = {}

    unmatched = []

    i = 0
    ii = len(js1)
    j = 0

    while i < len(js1):
        percent_done(i, ii)

        json_object1 = js1[i]
        ip1, count1 = cidr_to_integer_count(json_object1.get('start') + '/' + json_object1.get('value'), ipv)
        ip1end = ip1 + int(count1) - 1

        while j < len(js2):
            json_object2 = js2[j]
            ip2, count2 = cidr_to_integer_count(json_object2.get('network'), Root.IPV6)
            ip2end = ip2 + int(count2) - 1
            
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
    unmatched_output = gen_specific_filename(output, Root.UNMATCHED)
    with open(gen_data_dir(Root.EVALUATION) + unmatched_output, 'w') as f:
        json.dump(unmatched_list, f, indent=2)

    print('Saved File: ' + unmatched_output)

    with open(output, 'w') as f:
        json.dump(js1, f, indent=2)

    print('Saved File: ' + output)
'''
'''
    rir6 = gen_data_path_extension(Root.PREPROCESSED, Root.NRO6, Root.JSON)
    rir6 = read_from_jsonfile(rir6)
    max6 = gen_data_path_file(Root.PROCESSED, Root.MAXMIND_MERG_NAME_LIST[1])
    max6 = read_from_jsonfile(max6)
    merg_name = gen_merge_filename(Root.NRO4, Root.MAXMIND[Root.NAME], Root.IP6)
    output6 = gen_data_path_extension(directory_type=Root.EVALUATION, filename=merg_name, extension=Root.JSON)
    merge_rir_ip_max_ip(rir6, max6, output6, Root.IPV6)
    print_state(phase=Root.RELATE, state=Root.END, text=output6)
'''

'''
    ip4reg = gen_data_path_extension(Root.PREPROCESSED, Root.NRO4, Root.JSON)         # asn-registered-sebastian
    nroip4_json_data = read_from_jsonfile(ip4reg)

    max4 = gen_data_path_file(Root.PROCESSED, Root.MAXMIND_MERG_NAME_LIST[0])
    max4_json_data = read_from_jsonfile(max4)

    merg_name = gen_merge_filename(Root.NRO4,Root.MAXMIND[Root.NAME], Root.IP4)
    merge_rir_ip_max_ip(nroip4_json_data, max4_json_data, merg_name, Root.IPV4)

    print('data merged: ' + merg_name)
'''
