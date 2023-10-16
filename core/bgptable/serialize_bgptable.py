import json

from lib.mrtparse import Reader

from core.file_util import gen_data_path_extension
from core.file_util import gen_data_path_file
from core.json_util import save_to_jsonfile
from core.root_util import percent_done
from core.root import Root


def serialization_bgptable():
    input_file = gen_data_path_file(Root.MIRRORED, Root.BGPTABLE)
    serialize_data(input_file)
    print('bgp table data serialized')


#####################################################################

def serialize_data(filename):
    bgptable = gen_data_path_extension(Root.SERIALIZED, Root.BGPTABLE, Root.JSON)
    bgptable4 = gen_data_path_extension(Root.SERIALIZED, Root.BGPTABLE4, Root.JSON)
    bgptable6 = gen_data_path_extension(Root.SERIALIZED, Root.BGPTABLE6, Root.JSON)
    aspath4 = gen_data_path_extension(Root.SERIALIZED, Root.BGPASPATH4, Root.JSON)
    aspath6 = gen_data_path_extension(Root.SERIALIZED, Root.BGPASPATH6, Root.JSON)

    bgptable = open(bgptable, 'w')
    bgptable4 = open(bgptable4, 'w')
    bgptable6 = open(bgptable6, 'w')

    bgptable.write('[\n')
    bgptable4.write('[\n')
    bgptable6.write('[\n')

    path4 = set()
    path6 = set()
    i = 0
    for entry in Reader(filename):
        if i > 1:
            bgptable.write(',\n')
        ipv4 = entry.data.get('subtype').get(2)  # 2: ipv4 |4: ipv6
        ipv6 = entry.data.get('subtype').get(4)  # 2: ipv4 |4: ipv6
        prefix = entry.data.get('prefix')
        length = entry.data.get('length')
        if ipv4 == 'RIB_IPV4_UNICAST' or ipv6 == 'RIB_IPV6_UNICAST':
            as_path = entry.data.get('rib_entries', [])[0].get('path_attributes')[1].get('value')[0].get('value')
            originas = as_path[-1]
            full_path = as_path
            while as_path[-1] == originas:
                as_path = as_path[:-1]
                if len(as_path) == 0:
                    break
            dic = {'prefix': prefix + '/' + str(length), Root.FULLPATH: full_path, Root.ASPATH: as_path,
                   'origin-as': originas}  # path prepending eliminated
            if ipv4 == 'RIB_IPV4_UNICAST':
                if len(path4) != 0:
                    bgptable4.write(',\n')
                bgptable4.write(json.dumps(dic))
                path4.update(as_path)
            if ipv6 == 'RIB_IPV6_UNICAST':
                if len(path6) != 0:
                    bgptable6.write(',\n')
                bgptable6.write(json.dumps(dic))
                path6.update(as_path)
            bgptable.write(json.dumps([entry.data], indent=2)[2:-2])
        i += 1
        percent_done(i, 1100000)

    bgptable.write('\n]\n')
    bgptable4.write('\n]\n')
    bgptable6.write('\n]\n')

    bgptable.close()
    bgptable4.close()
    bgptable6.close()

    path4 = [int(i) for i in path4]
    path4.sort()
    path6 = [int(i) for i in path6]
    path6.sort()
    save_to_jsonfile(path4, aspath4)
    save_to_jsonfile(path6, aspath6)


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    serialization_bgptable()
    exit()
