from core.typing import List, Dict

from core.json_util import delete_specific_key
from core.root import Root


def expand_as(data):
    dic = []
    for d in data:
        for a in as_range_to_list(d):
            dic.append(a)
    return dic


def as_range_to_list(data):
    i = 1
    value = int(data[Root.VALUE])
    data = delete_specific_key(data, Root.VALUE)
    datas = []
    if i == value:
        datas.append(data)
        return datas
    else:
        while i < value:
            data2 = data.copy()
            data2[Root.START] = int(data[Root.START]) + i
            i = i + 1
            datas.append(data2)
    return datas


def aggregated_by_cc(json_list: List[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
    aggregated_dict = {}
    for item in json_list:
        as_list = as_range_to_list(item)
        for asn in as_list:
            cc = asn[Root.CC]
            start = asn[Root.START]
            value = asn[Root.VALUE]
        if cc not in aggregated_dict:
            aggregated_dict[cc] = []
        aggregated_dict[cc].append({Root.START: start, Root.VALUE: value})
    return aggregated_dict


# Python-Code zur Verschmelzung von zwei Listen von JSON-Objekten anhand eines bereitgestellten Schlüssels
def advanced_merge_and_modify(json_list1, json_list2, key):
    # Ein Wörterbuch erstellen, um Elemente aus json_list2, indiziert durch den Schlüssel, zu speichern
    json_dict2 = {}
    for item in json_list2:
        if key in item:
            if item[key] not in json_dict2:
                json_dict2[item[key]] = []
            json_dict2[item[key]].append(item)

    # Durch json_list1 iterieren und Elemente anhand des Schlüssels verschmelzen
    for item1 in json_list1:
        if key in item1:
            if item1[key] in json_dict2:
                for item2 in json_dict2[item1[key]]:
                    for k, v in item2.items():
                        if k != key:
                            if k in item1:
                                if not isinstance(item1[k], list):
                                    item1[k] = [item1[k]]
                                item1[k].append(v)
                            else:
                                item1[k] = v

    # Elemente aus json_list2 hinzufügen, die keinen passenden Schlüssel in json_list1 haben
    for k, items in json_dict2.items():
        if k not in [item[key] for item in json_list1 if key in item]:
            json_list1.extend(items)

    return json_list1
