import pytest
from wbutils import get_wb_directory, get_artifacts_directory, get_temp_directory


def test_get_wb_directory():
    assert isinstance(get_wb_directory(), str)


def test_get_artifacts_directory():
    assert isinstance(get_artifacts_directory(), str)


def test_get_temp_directory():
    assert isinstance(get_temp_directory(), str)
