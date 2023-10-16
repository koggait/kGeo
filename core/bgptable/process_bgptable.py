from core.file_util import gen_data_path_extension
from core.json_util import delete_specific_keys
from core.json_util import read_from_jsonfile
from core.json_util import save_to_jsonfile
from core.root import Root


def processing_bgptable():
    bgptable4in = gen_data_path_extension(Root.SERIALIZED, Root.BGPTABLE4, Root.JSON)
    bgptable4out = gen_data_path_extension(Root.PREPROCESSED, Root.BGPTABLE4, Root.JSON)
    bgptable6in = gen_data_path_extension(Root.SERIALIZED, Root.BGPTABLE6, Root.JSON)
    bgptable6out = gen_data_path_extension(Root.PREPROCESSED, Root.BGPTABLE6, Root.JSON)
    aggregated4 = gen_data_path_extension(Root.PROCESSED, Root.BGPTABLE4, Root.JSON)
    aggregated6 = gen_data_path_extension(Root.PROCESSED, Root.BGPTABLE6, Root.JSON)

    bgptable4 = read_from_jsonfile(bgptable4in)
    bgptable4v2 = delete_specific_keys(bgptable4, [Root.FULLPATH])
    save_to_jsonfile(bgptable4v2, bgptable4out)

    bgptable6 = read_from_jsonfile(bgptable6in)
    bgptable6v2 = delete_specific_keys(bgptable6, [Root.FULLPATH])
    save_to_jsonfile(bgptable6v2, bgptable6out)

    bgptable4v2 = read_from_jsonfile(bgptable4out)
    bgptable4v3 = aggregated_by_origin_as(bgptable4v2)
    save_to_jsonfile(bgptable4v3, aggregated4)

    bgptable6v2 = read_from_jsonfile(bgptable6out)
    bgptable6v3 = aggregated_by_origin_as(bgptable6v2)
    save_to_jsonfile(bgptable6v3, aggregated6)

    print('bgp data process')


#####################################################################


def aggregated_by_cc(input_list):
    output_dict = {}  # Initialisierung des Ausgabe-Dictionaries

    for item in input_list:  # Durchlauf der Eingabeliste
        cc = item.get('cc', None)  # Extraktion des Wertes für den Schlüssel 'cc'
        if cc is not None:  # Überprüfung, ob 'cc' vorhanden ist
            if cc not in output_dict:
                output_dict[
                    cc] = []  # Initialisierung einer neuen Liste, falls 'cc' noch nicht im Ausgabe-Dictionary vorhanden ist
            output_dict[cc].append(
                item)  # Hinzufügen des aktuellen Dictionary zur Liste unter dem entsprechenden 'cc'-Schlüssel

    return output_dict  # Rückgabe des Ausgabe-Dictionaries


def aggregated_by_origin_as(input_list):
    aggregated_dict = {}  # Initialisierung des gruppierten Dictionaries

    for item in input_list:  # Durchlauf der Eingabeliste
        origin_as = item.get('origin-as', None)  # Extraktion des Wertes für den Schlüssel 'origin-as'

        if origin_as is not None:  # Überprüfung, ob 'origin-as' vorhanden ist
            if origin_as not in aggregated_dict:
                aggregated_dict[
                    origin_as] = []  # Initialisierung einer neuen Liste, falls 'origin-as' noch nicht im gruppierten Dictionary vorhanden ist

            # Erstellung eines neuen Dictionarys ohne den 'origin-as'-Schlüssel
            new_item = {k: v for k, v in item.items() if k != 'origin-as'}

            aggregated_dict[origin_as].append(
                new_item)  # Hinzufügen des neuen Dictionarys zur Liste unter dem entsprechenden 'origin-as'-Schlüssel

    # Umwandlung des Dictionaries in eine Liste von Dictionaries
    output_list = [{k: v} for k, v in aggregated_dict.items()]

    return output_list  # Rückgabe der Ausgabeliste


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    processing_bgptable()
    exit()
