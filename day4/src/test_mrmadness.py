# -*- coding: utf-8 -*-

import pytest

TEST_validate_input = {
    # ("send a thank you", "Enter the first and last name of the donor: (First Last)"),
    ("y", True),
    ("n", False)
    #("p", )
    # ("q", "SystemExit: 1")
}

@pytest.mark.parametrize("fn, result", TEST_validate_input)
def test_validate_input(fn, result):
    from mrmadness import validate_input
    assert validate_input(fn) == result


# TODO: see the dicitonary before test

TEST_validate_the_fullname = {
    ("Jeremy Edwards", False),
    ("Jeremy", False)
}

@pytest.mark.parametrize("fn, result", TEST_validate_the_fullname)
def test_validate_the_fullname(fn, result):
    from mrmadness import validate_the_fullname
    assert validate_the_fullname(fn) == result
