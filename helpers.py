import os
from os.path import join


def get_path(dir_name, filename) -> str:
    current_path = os.path.dirname(__file__)
    return join(current_path, dir_name, filename)
