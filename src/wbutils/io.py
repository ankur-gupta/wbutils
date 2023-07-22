import os
import ujson
import tempfile
from .directory import get_temp_directory


def get_temp_path_to_file(filename: str):
    path_to_tempdir = tempfile.mktemp(dir=get_temp_directory())
    os.makedirs(path_to_tempdir, exist_ok=True)
    return os.path.join(path_to_tempdir, filename)


def read_json(path_to_file: str):
    with open(path_to_file, 'r') as f:
        data = ujson.load(f)
    return data


def write_json(x, path_to_file: str, indent=2):
    with open(path_to_file, 'w') as f:
        ujson.dump(x, f, indent=indent)


def read_text(path_to_file: str) -> str:
    with open(path_to_file, 'r') as f:
        lines = f.readlines()
    text = ''.join(lines)
    return text


def write_text(text, path_to_file: str):
    with open(path_to_file, 'w') as f:
        f.writelines(text)
