from os import listdir
from os.path import isfile, join, isdir
import codecs
import os
import glob
import json


# Read file
def read_file(file_name, utf=None):
    if utf:
        input_file = codecs.open(file_name, 'r', "utf-" + str(utf))
    else:
        input_file = open(file_name, 'r')

    data = []
    for input_line in input_file:
        data.append(input_line.replace("\n", ""))
    return data


# Read file which is a JSON
def read_json(file_path):
    with open(file_path) as json_file:
        return json.load(json_file)


def write_json(file_path, json_data):
    with open(file_path, 'w') as outfile:
        json.dump(json_data, outfile, sort_keys=True, indent=4)


# Write to file
def write_file(file_name, file_text):
    result_file = open(file_name, 'w')
    for result_line in file_text:
        result_file.write(str(result_line) + "\n")
    result_file.close()


# Write to file in utf-8 format
def write_file_utf8(file_name, file_text):
    result_file = codecs.open(file_name, 'w', "utf-8")
    for result_line in file_text:
        result_file.write(str(result_line) + "\n")
    result_file.close()


# Append a list of lines to an already existing file.
# If file does not exist, create it.
def append_to_file(file_name, file_text):
    result_file = codecs.open(file_name, 'a+', "utf-8")
    if isinstance(file_text, list):
        for result_line in file_text:
            result_file.write(str(result_line) + "\n")
    else:
        result_file.write(str(file_text) + "\n")
    result_file.close()


def get_file_name_with_extension(path, name):
    for infile in glob.glob(os.path.join(path, name + '.*')):
        return infile


# Check if file exists
def exists(file_path):
    flag = os.path.isfile(file_path)
    if flag:
        return True
    return False


# Return a list of files from specified path (files inside folders of this path are not checked)
# Format:
#   {
#       "path": path,
#       "filename": filename.extension
#   }
def list_files(path):
    return [{'path': path, 'filename': f} for f in listdir(path) if isfile(join(path, f))]


# Return a list of folders from specified path (folders inside folders of this path are not checked)
def list_dirs(path):
    return [join(path, f) for f in listdir(path) if isdir(join(path, f))]


# Return a list of files from specified path. Files in subdirectories as well.
# Format:
#   {
#       "path": path,
#       "filename": filename.extension
#   }
def list_files_sub(path):
    data = list_files(path)

    for directory in list_dirs(path):
        data += list_files_sub(directory)

    return data
