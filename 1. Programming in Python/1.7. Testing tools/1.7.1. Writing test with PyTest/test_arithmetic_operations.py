"""_test code for arithmetic operations_"""

import arithmetic_operations


def test_add():
    """_Function test code for add()_"""
    assert arithmetic_operations.add(4, 5) == 9


def test_sub():
    """_Function test code for sub()_"""
    assert arithmetic_operations.sub(4, 5) == -1


def test_mul():
    """_Function test code for mul()_"""
    assert arithmetic_operations.mul(4, 5) == 20


def test_div():
    """_Function test code for div()_"""
    assert arithmetic_operations.div(4, 5) == 0.8
