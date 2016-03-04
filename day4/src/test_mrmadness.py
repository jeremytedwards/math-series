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


TEST_validate_the_fullname = {
    ("Jeremy Edwards", False),
    ("Jeremy", False)
}

@pytest.mark.parametrize("fn, result", TEST_validate_the_fullname)
def test_validate_the_fullname(fn, result):
    from mrmadness import validate_the_fullname
    assert validate_the_fullname(fn) == result


DONOR_DICT = {
    "Paul Rubens": {"donation_total": 0, "donation_ave": 0, "donation_count": 0},
    "Peter Paul": {"donation_total": 0, "donation_ave": 0, "donation_count": 0}
}

TEST_set_donation_total = {
    ("Paul Rubens", "$10000", 10000),
    ("Paul Rubens", "10,000", 10000),
    ("Paul Rubens", "$10000.00", 10000),
    ("Paul Rubens", "10000", 10000)
}

@pytest.mark.parametrize("donor, fn, result", TEST_set_donation_total)
def test_set_donation_total(donor, fn, result):
    from mrmadness import set_donation_total
    assert set_donation_total(donor, fn) == result
