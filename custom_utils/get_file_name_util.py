import os


def get_file_name(path):
    if not os.path.isdir(path):
        return os.path.splitext(os.path.basename(path))[0].split(".")[0]
