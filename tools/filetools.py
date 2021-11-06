from os import listdir
from os.path import isfile, join


class FileTools(object):

    @staticmethod
    def get_files_from_dir(path):
        return [(path + f) for f in listdir(path) if isfile(join(path, f))]
