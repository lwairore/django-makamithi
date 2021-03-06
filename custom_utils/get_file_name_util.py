import os
from os.path import basename


def get_parent_directory_name_of_current_directory(current_working_directory: str):
    parent_directory_name = basename(current_working_directory)

    return parent_directory_name


def get_file_name(path):
    if not os.path.isdir(path):
        return os.path.splitext(os.path.basename(path))[0].split(".")[0]
