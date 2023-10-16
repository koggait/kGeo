import json

from core.file_util import gen_data_dir
from core.ip_util import ipv4_cidr_to_integer_count
from core.ip_util import networks_intersect
from core.root import Root
from core.root_util import percent_done


def split_line(line, delimiter):
    return list(line.strip().split(delimiter))


def line_to_dict(description, fields):
    # intermediate dictionary
    dict_object = {}
    for key, value in zip(fields, description):
        # creating dictionary for each entry
        dict_object[key] = value
    return dict_object


def jsonfiles_2_dicts(json1, json2, dir):
    with open(dir + json1) as f:
        data = f.read()
    js1 = json.loads(data)
    with open(dir + json2) as f:
        data = f.read()
    js2 = json.loads(data)
    return js1, js2


def json_to_dict(jsn, dir):
    with open(dir + jsn) as f:
        data = f.read()
    js = json.loads(data)
    return js


def read_from_jsonfile(json_file):
    print(json_file)
    with open(json_file) as f:
        data = f.read()
    return json.loads(data)

def save_to_jsonfile(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=1)
    print('Saved File: ' + output_file)


def load_multiple_from_jsonfile(json_file):
    data = []
    with open(json_file, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    print('Loaded File: ' + json_file)
    return data


def delete_specific_key(data, key_to_delete):
    data.pop(key_to_delete, None)  # Remove the specified key if it exists
    return data


def delete_specific_keys(data, keys_to_delete):
    for obj in data:  # Process each JSON object in the list
        for key in keys_to_delete:  # Process each key in the key list
            obj.pop(key, None)  # Remove the specified key if it exists)
    return data


def keep_specific_keys(data, keys_to_keep):
    for obj in data:  # Process each JSON object in the list
        keys = obj.keys()
        keys_to_delete = []
        for k in keys:
            if k not in keys_to_keep:
                keys_to_delete.append(k)
        for key in keys_to_delete:  # Process each key in the key list
            obj.pop(key, None)  # Remove the specified key if it exists)
    return data


def delete_specific_objects(data, key, value, removedData):
    i = 0
    removedData = []
    while i < len(data):
        obj = data[i]
        if obj[key] == value:
            data.remove(obj)  # Remove the specified object if key-value pair match
            removedData.append(obj)
        else:
            i = i + 1
    return data, removedData


def transfer_specific_objects(data_src, key, value):
    data_dst = []
    i = 0
    j = 0
    jj = len(data_src)
    while i < len(data_src):
        obj = data_src[i]
        if obj[key] == value:
            data_dst.append(obj)
            data_src.remove(obj)  # Remove the specified key if it exists
        else:
            i = i + 1
        j = j + 1
        percent_done(j, jj)

    return data_src, data_dst


# key_mapping = {"old_key": "new_key", ...}
def transform_json_keys(input_file, key_mapping):
    data = read_from_jsonfile(input_file)
    output_list = []

    for item in data:
        transformed_item = {}

        for input_key, output_key in key_mapping.items():
            # Überprüfung, ob der Schlüssel im Eingabe-Dictionary vorhanden ist.
            if input_key in item:
                transformed_item[output_key] = item[input_key]

        output_list.append(transformed_item)

    return output_list


def transform_key_to_primary(data, primary_key):
    json_dic = {}

    for json_object in data:

        dic = {}
        for key in json_object:

            if key != primary_key:
                dic[key] = json_object[key]

        if json_object[primary_key] in json_dic.keys():
            json_dic[primary_key] = [json_object[primary_key], dic]
        else:
            json_dic[json_object[primary_key]] = dic

    return json_dic


def transform_key_to_primary_int(data, primary_key):
    json_dic = {}

    for json_object in data['data']:

        dic = {}
        for key in json_object:

            if key != primary_key:
                dic[key] = json_object[key]

        json_dic[int(json_object[primary_key])] = dic

    return json_dic


def aggregate_by_cc(data, cc_key):
    output_dict = {}  # Initialisierung des Ausgabe-Dictionaries

    for item in data:  # Durchlauf der Eingabeliste

        cc = item.get(cc_key, None)  # Extraktion des Wertes für den Schlüssel 'cc'
        if cc is not None:  # Überprüfung, ob 'cc' vorhanden ist
            if cc not in output_dict:
                output_dict[cc] = []  # Initialisierung einer neuen Liste, falls 'cc' noch nicht im Ausgabe-Dictionary vorhanden ist
            output_dict[cc].append(item)  # Hinzufügen des aktuellen Dictionary zur Liste unter dem entsprechenden 'cc'-Schlüssel

    sorted_dict = dict(sorted(output_dict.items()))
    return sorted_dict  # Rückgabe des Ausgabe-Dictionaries


def merge_asn_ip4(json1, net_name1, json2, net_name2, output):
    import json

    js1 = read_from_jsonfile(json1)
    js2 = read_from_jsonfile(json2)

    dic = []
    unmatched = []

    i = 0
    ii = len(js1)
    j = 0
    while i < len(js1):
        percent_done(i, ii)
        json_object1 = js1[i]
        ip1, count1 = ipv4_cidr_to_integer_count(json_object1.get(net_name1))
        ip1end = ip1 + count1

        while j < len(js2):
            json_object2 = js2[j]
            ip2, count2 = ipv4_cidr_to_integer_count(json_object2.get(net_name2))
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
        js1[i][net_name1 + 's'] = dic
        dic = []
        i = i + 1
    if len(js2) > 0:
        unmatched.append(js2.pop())

    output_file = gen_data_dir(Root.ACCUMULATED) + output
    # Write the modified JSON objects to the output file
    with open(gen_data_dir(Root.ACCUMULATED) + net_name2 + '_unmatched_IPv4', 'w') as f:
        json.dump(unmatched, f, indent=2)

    print('Saved File: ' + 'Subnets_unmatched')

    with open(output_file, 'w') as f:
        json.dump(js1, f, indent=2)

    print('Saved File: ' + output_file)


def filter_keys(input_data, keys_to_delete, output_file):
    data = keep_specific_keys(input_data, keys_to_delete)
    save_to_jsonfile(data, output_file)

def reduce_keys(input_data, keys_to_delete, output_file):
    data = delete_specific_keys(input_data, keys_to_delete)
    save_to_jsonfile(data, output_file)

def aggregate_key(input_data, key, output_file):
    data = aggregate_by_cc(input_data, key)
    save_to_jsonfile(data, output_file)

def order_key(input_data, key, output_file):
    data = transform_key_to_primary(input_data,key)
    save_to_jsonfile(data, output_file)



