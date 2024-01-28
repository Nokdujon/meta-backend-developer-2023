import find_string
import pytest


def test_is_present():
    assert find_string.is_present("Al")


def test_is_alphabet():
    assert find_string.is_alphabet("N7")
