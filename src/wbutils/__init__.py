import os
import logging

from wbutils.version import __version__

_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_path(partial_path=''):
    return os.path.join(_ROOT, partial_path)
