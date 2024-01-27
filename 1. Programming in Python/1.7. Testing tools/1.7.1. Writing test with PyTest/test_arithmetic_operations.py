"""_arithmetic operations_
"""

import arithmetic_operations


def test_add():
    assert arithmetic_operations.add(4, 5) == 9


def test_sub():
    assert arithmetic_operations.sub(4, 5) == -1


def test_mul():
    assert arithmetic_operations.mul(4, 5) == 20


def test_div():
    assert arithmetic_operations.div(4, 5) == 0.8
