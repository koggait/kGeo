import sys
import pathlib

from core.root import Root


def gen_specific_filename(filename, specific):
    return '{}_{}'.format(filename, specific)


def getfilename(url):
    return pathlib.PurePosixPath(url).name


def getname(url):
    return pathlib.PurePosixPath(url).stem


# generate directory path to data type
def gen_file_extension(filename, extension):
    return '{}_{}'.format(filename, extension)


# generate directory path to data type
def gendir(path, directory):
    return '{}/{}/'.format(path, directory)


# generate directory path to data type
def gen_data_dir(directory_type):
    return gendir(Root.DATADIR, directory_type)


def gen_data_path_file(directory_type, filename):
    return gen_data_dir(directory_type) + filename


# generate file path to file with file ending
def gen_path_extension(directory_type, filename, extension):
    return Root.DATADIR + directory_type + '/' + filename + '.' + extension


# generate file path to file
def gen_history_path(directory_type, filename):
    return Root.HISTORYDIR + directory_type + '/' + filename


# generate file path to file
def gen_history_path_extension(directory_type, filename, extension):
    return Root.HISTORYDIR + directory_type + '/' + filename + '.' + extension


# generate file path to file with file ending
def gen_data_path_extension(directory_type, filename, extension):
    return Root.DATADIR + directory_type + '/' + filename + '.' + extension


def gen_input_output_path_files(name, input_directory, output_directory):
    input_file = gen_data_path_file(input_directory, name)
    output_file = gen_data_path_file(output_directory, name)
    return input_file, output_file


def gen_good_bad_path_extension(name, directory, filetype):
    good_file = gen_data_path_extension(directory, gen_specific_filename('good', name), filetype)
    bad_file = gen_data_path_extension(directory, gen_specific_filename('bad', name), filetype)
    return good_file, bad_file


def gen_input_output_path_extension(name, input_directory, output_directory, filetype):
    input_file = gen_data_path_extension(input_directory, name, filetype)
    output_file = gen_data_path_extension(output_directory, name, filetype)
    return input_file, output_file
