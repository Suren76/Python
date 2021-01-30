from calculator import *


def test_subtraction():
    assert subtraction(9, 5) == 4


def test_addition():
    assert addition(9, 4) == 13


def test_division():
    assert division(27, 3)


def test_multiplication():
    assert multiplication(4, 7) == 28


def test_square_root():
    assert square_root(49) == 7
