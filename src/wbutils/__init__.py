import os
import logging

from wbutils.version import __version__
from wbutils.framework import set_framework, get_framework, PYTORCH_FRAMEWORK, TENSORFLOW_FRAMEWORK, DEFAULT_FRAMEWORK
from wbutils.include import include_files, TRAIN_SPLIT, VAL_SPLIT, TEST_SPLIT, SPLITS, INCLUDE_STUBS, EXCLUDE_STUBS
from wbutils.directory import set_wb_directory, set_artifacts_directory, get_wb_directory, get_artifacts_directory
import wbutils.parsing as parsing
import wbutils.parsing.pytorch

_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_path(partial_path=''):
    return os.path.join(_ROOT, partial_path)
