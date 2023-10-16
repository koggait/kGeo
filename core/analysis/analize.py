from core.file_util import gen_data_path_extension
from core.json_util import read_from_jsonfile
from core.json_util import save_to_jsonfile
from core.root import Root


def analizing_data():
    input_file = gen_data_path_extension(Root.EVALUATION, Root.AS_EXTENDED_BY_CC, Root.JSON)

    data = read_from_jsonfile(input_file)
    summary_reg, summary_active = count_json_objects(data)
    items = list(summary_reg.items())
    sorted_reg = dict(sorted(items, key=lambda item: item[1], reverse=True))
    output_file = gen_data_path_extension(Root.EVALUATION, Root.AS_BIG_SUM_BY_REG_CC, Root.JSON)
    save_to_jsonfile(sorted_reg, output_file)

    items = list(summary_active.items())
    sorted_active = dict(sorted(items, key=lambda item: item[1], reverse=True))
    output_file = gen_data_path_extension(Root.EVALUATION, Root.AS_BIG_SUM_BY_ACTIV_CC, Root.JSON)
    save_to_jsonfile(sorted_active, output_file)

    as_ratio = join_as_counts(sorted_reg, sorted_active)
    output_file = gen_data_path_extension(Root.EVALUATION, Root.AS_RATIO, Root.JSON)
    save_to_jsonfile(as_ratio, output_file)


def join_as_counts(count1, count2):
    joined_data = []
    for cc_key in count1:
        merged_object = {
            'cc': cc_key,
            'reg-as': count1[cc_key]
        }

        # Check if 'cc' key exists in count2, if so, add 'active-as' field
        if cc_key in count2:
            merged_object['active-as'] = count2[cc_key]
        else:
            merged_object['active-as'] = 0

        joined_data.append(merged_object)

    return joined_data


def count_json_objects(data):
    reg_as_count = {}
    active_as_count = {}
    for key, value in data.items():
        reg_as_count[key] = len(value)
        for obj in value:
            if obj['inpath4']  or obj['inpath6']:
                if key not in active_as_count.keys():
                    active_as_count[key] = 1
                else:
                    active_as_count[key] = active_as_count[key] + 1
    return reg_as_count, active_as_count


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    analizing_data()
    exit()
