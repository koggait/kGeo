from core.file_util import gen_data_path_extension
from core.root import Root


def any_item_in_pool(check_pool, items):
    for item in items:
        if item in check_pool:
            return True
        else:
            return False
    else:
        return 'IF-RETURN-ERROR'


def percent_done(loop_number, loops):
    p = round(loop_number * 100 / loops, 2)
    print(str(p) + ' %')
    return int(p)


def print_state(phase, state, text):
    print(phase + ' ' + state + ' ' + str(text))


def log_begin(action, entity):
    print('START {}: {}'.format(action, entity))


def log_end(action, entity):
    print('COMPLETED {}: {}'.format(action, entity))


def log_action(action, entity):
    print('{}: {}'.format(action, entity))


def copy_serialized_mirror(filename):
    import shutil
    origin_file = gen_data_path_extension(Root.MIRRORED, filename, Root.JSON)
    destination_file = gen_data_path_extension(Root.SERIALIZED, filename, Root.JSON)
    shutil.copy(origin_file, destination_file)
