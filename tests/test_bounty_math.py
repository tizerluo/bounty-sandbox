import doctest

import pytest

import bounty_math
from bounty_math import add, subtract


def test_add_returns_sum():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(0, 0) == 0


def test_add_rejects_non_integers():
    with pytest.raises(TypeError):
        add(1.5, 2)


def test_docstring_examples():
    assert doctest.testmod(bounty_math).failed == 0


def test_subtract_returns_difference():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(-4, 1) == -5
    assert subtract(0, 0) == 0


def test_subtract_rejects_non_integers():
    with pytest.raises(TypeError):
        subtract(1.5, 2)
    with pytest.raises(TypeError):
        subtract(1, True)
