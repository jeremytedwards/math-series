# -*- coding: utf-8 -*-

import pytest

FIB_TABLE = [
    (1, 0),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 3),
    (6, 5)
]

@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_fibonacci(n, result):
    from series import fibonacci
    assert fibonacci(n) == result

LUCAS_TABLE = [
    (1, 2),
    (2, 1),
    (3, 3),
    (4, 4),
    (5, 7),
    (6, 11)
]

@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_lucas(n, result):
    from series import lucas
    assert lucas(n) == result


 # A fibonacci, a Lucas, and 3 tests on an Alt series
SEQ_TABLE = [
    (1, 0, 1, 0),
    (1, 2, 1, 2),
    (1, 10, 11, 10),
    (2, 10, 11, 11),
    (3, 10, 11, 21)
]

@pytest.mark.parametrize('n, a, b, result', SEQ_TABLE)
def test_series(n, a, b, result):
    from series import sum_series
    assert sum_series(n, a, b) == result