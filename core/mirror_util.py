from core.file_util import gen_data_path_file
from core.file_util import gen_history_path_extension
from core.file_util import gen_specific_filename
from core.file_util import getfilename
from core.root import Root
from core.root_util import print_state


def mirror_file(filename):
    getfile(Root.MIRROR_URLS[filename], gen_data_path_file(Root.MIRRORED, filename))
    return gen_data_path_file(Root.MIRRORED, filename)


def mirror_file_history(filename, history_directory):
    mirrored_file = gen_data_path_file(Root.MIRRORED, filename)
    getfile(Root.MIRROR_URLS[filename], mirrored_file)
    copy_to_history(mirrored_file, history_directory, filename)


def mirror_decompress_file(filename, function):
    mirrored_file = gen_data_path_file(Root.MIRRORED, filename)
    getfile(Root.MIRROR_URLS[filename], mirrored_file)
    function(mirrored_file)


def mirror_backup_file(filename):
    mirrored_file = gen_data_path_file(Root.MIRRORED, filename)
    getfile(Root.MIRROR_URLS[filename], mirrored_file)
    copy_to_history(mirrored_file, filename, filename)


def mirror_decode_file(filename, decode_function):
    mirrored_file = gen_data_path_file(Root.MIRRORED, filename)
    getfile(Root.MIRROR_URLS[filename], mirrored_file)
    return decode_function(mirrored_file)


def copy_to_evaluation(filename, origin_file):
    import shutil
    evaluation_filename = gen_data_path_file(Root.EVALUATION, filename)
    shutil.copy(origin_file, evaluation_filename)
    print_state(Root.EVALUATION, 'COPY2EVAL', origin_file)


def copy_to_history(origin_file, directory, history_file_name):
    import shutil
    import datetime
    history_filename = gen_specific_filename(history_file_name, datetime.date.today())
    history_file_name = gen_history_path_extension(directory, history_filename, Root.JSON)
    shutil.copy(origin_file, history_file_name)
    print_state(Root.BACKUP, Root.END, history_file_name)
    return history_file_name


def getfile(url, output_file):
    import requests
    print_state(Root.MIRROR, Root.BEGIN, url)
    r = requests.get(url, allow_redirects=True)
    open(output_file, 'wb').write(r.content)
    print_state(Root.MIRROR, Root.END, url)
    return output_file

def decompress_bz2(filename):
    import bz2
    return decompress(filename, bz2)


def decompress_gz(filename):
    import gzip
    return decompress(filename, gzip)


def decompress(filename, compression):
    with compression.open(filename, 'rb') as f:
        content = f.read()
    with open(filename, 'wb') as k:
        k.write(content)
    return filename
