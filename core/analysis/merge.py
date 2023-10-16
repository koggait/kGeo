from core.file_util import gen_data_path_extension
from core.json_util import read_from_jsonfile
from core.json_util import save_to_jsonfile
from core.root import Root
from core.root_util import percent_done


def merging_data():
    asnames = gen_data_path_extension(Root.SERIALIZED, Root.ASNAMES, Root.JSON)         # as-names-sebastian
    asnames_json_data = read_from_jsonfile(asnames)

    asnreg = gen_data_path_extension(Root.PREPROCESSED, Root.NROASN, Root.JSON)         # asn-registered-sebastian
    nroasn_json_data = read_from_jsonfile(asnreg)

    bgpaspath4 = gen_data_path_extension(Root.SERIALIZED, Root.BGPASPATH4, Root.JSON)       # extracted list of active as in ipv4 routing table during serialization of bgptable
    in_global_ipv4_routing_table_list = list(read_from_jsonfile(bgpaspath4))
    bgpaspath6 = gen_data_path_extension(Root.SERIALIZED, Root.BGPASPATH6, Root.JSON)       # extracted list of active as in ipv6 routing table during serialization of bgptable
    in_global_ipv6_routing_table_list = list(read_from_jsonfile(bgpaspath6))

    merged = merge_by_keys(asnames_json_data, nroasn_json_data, in_global_ipv4_routing_table_list, in_global_ipv6_routing_table_list)

    asn_extended = gen_data_path_extension(Root.EVALUATION, Root.AS_EXTENDED, Root.JSON)

    save_to_jsonfile(merged, asn_extended)

    print('data merged: asnames X rir_asn X bgppath')


#####################################################################


def merge_by_keys(js1, js2, js4, js6):
    merged_list = []  # Initialisierung der Ausgabeliste

    matching = True

    while matching:
        if len(js1) == 0:
            break
        if int(js2[0]['value']) > 1000000:
            break
        k = js1[0]
        j = js2[0]

        merged_dict = k.copy()  # Kopieren des aktuellen Dictionaries aus js1
        merged_dict['asnumber'] = int(merged_dict['asnumber'])  # Änderung des Schlüssels 'asnumber' zu 'asn'

        if int(k['asnumber']) >= int(j['start']) and int(k['asnumber']) <= int(j['start']) + int(j['value']) - 1:
            if k['cc'] != j['cc']:
                merged_dict['cc'] = k['cc']  # Erstellung eines neuen 'cc'-Werts
                merged_dict['cc_conflict'] = j['cc']    # js1 [as-names-sebasitan] merged as primary cc

        # Prüfung der Mitgliedschaft in js4 und js6
        if int(k['asnumber']) in js4:
            merged_dict['inpath4'] = True
        else:
            merged_dict['inpath4'] = False

        if int(k['asnumber']) in js6:
            merged_dict['inpath6'] = True
        else:
            merged_dict['inpath6'] = False

        percent_done(int(merged_dict['asnumber']), 401308)

        itras = int(merged_dict['asnumber'])

        if int(k['asnumber']) == itras:
            js1.remove(k)
        if int(j['start']) + int(j['value']) - 1 <= itras:
            js2.remove(j)

        merged_list.append(merged_dict)  # Hinzufügen des fusionierten Dictionaries zur Ausgabeliste

    return merged_list  # Rückgabe der fusionierten Liste


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    merging_data()
    exit()
