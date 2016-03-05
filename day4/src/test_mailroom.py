# -*- coding: utf-8 -*-

import pytest

##########
#   Getters and Setters
##########
TEST_add_donor_to_report = {
    ("Sally Struthers"),
    ("Samsonite"),
    ("New Guy"),
}
@pytest.mark.parametrize("donor", TEST_add_donor_to_report)
def test_add_donor_to_report(donor):
    from mailroom import add_donor_to_report
    from mailroom import DONOR_DICT
    add_donor_to_report(donor)
    assert donor in DONOR_DICT.keys()


TEST_get_donation_total = {
    ("Michael Jackson", 100000),
    ("Jeremy Edwards", 1000),
    ("Peter Paul", 50000),
    ("Paul Rubens", 100),
}
@pytest.mark.parametrize("donor, result", TEST_get_donation_total)
def test_get_donation_total(donor, result):
    from mailroom import get_donation_total
    assert get_donation_total(donor) == result


# TODO: need to add regex to select numbers first before all test here will pass
TEST_set_donation_total = {
    # ("Paul Rubens", "$10000", None),
    # ("Paul Rubens", "10,000", None),
    # ("Paul Rubens", "$10000.00", None),
    ("Paul Rubens", "100", 200),
    ("Michael Jackson", "100000", 200000),
    ("Jeremy Edwards", "1000", 2000),
}
@pytest.mark.parametrize("donor, fn, result", TEST_set_donation_total)
def test_set_donation_total(donor, fn, result):
    from mailroom import update_donation_total
    from mailroom import DONOR_DICT
    update_donation_total(donor, fn)
    assert DONOR_DICT.get(donor).get("donation_total") == result


# TODO: there is a problem here since the global variable is being used the other tests are updating the values
# before hitting this test. need to look at how to use a local copy of the global then removing after each test
TEST_update_donor_count = {
    ("Paul Rubens", 3),
    ("Peter Paul", 6),
    ("Jeremy Edwards", 3),
}
@pytest.mark.parametrize("donor, result", TEST_update_donor_count)
def test_update_donor_count(donor, result):
    from mailroom import update_donor_count
    from mailroom import DONOR_DICT
    update_donor_count(donor)
    assert DONOR_DICT.get(donor).get("donation_count") == result


# TODO: there is a problem here since the global variable is being used the other tests are updating the values
# before hitting this test. need to look at how to use a local copy of the global then removing after each test
TEST_get_donation_ave = {
    ("Paul Rubens", 50.0),
    ("Michael Jackson", 10),
    ("Jeremy Edwards", 500),
}
@pytest.mark.parametrize("donor, result", TEST_get_donation_ave)
def test_get_donation_ave(donor, result):
    from mailroom import get_donation_ave
    from mailroom import DONOR_DICT
    assert round(DONOR_DICT.get(donor).get("donation_ave")) == result


TEST_update_donation_ave = {
    ("Paul Rubens",  50),
    ("Peter Paul", 10000),
    ("Jeremy Edwards", 500),
}
@pytest.mark.parametrize("donor, result", TEST_update_donation_ave)
def test_update_donation_ave(donor, result):
    from mailroom import update_donation_ave
    from mailroom import DONOR_DICT
    assert round(DONOR_DICT.get(donor).get("donation_ave")) == result



####################
#   Outputs
####################
def test_send_reply_email(fn="Paul Rubens", result=None):
    from mailroom import send_reply_email
    assert send_reply_email(fn) == result


def test_send_donor_email(fn="Paul Rubens", result=None):
    from mailroom import send_donor_email
    assert send_donor_email(fn) == result


def test_print_donors_names(result=None):
    from mailroom import print_donors_names
    assert print_donors_names() == result


def test_print_sorted_donors_list(result=None):
    from mailroom import print_sorted_donors_list
    assert print_sorted_donors_list() == result


####################
#   Get Input
####################
# Can't test since function waits for input
# def test_ask_for_input(fn="Paul Rubens", val=True, result=None):
#     from mrmadness import ask_for_input
#     assert ask_for_input(fn, val) == result


# Can't test since function waits for input
# TEST_check_name = {
#     ("Jeremy Edwards", False),
#     ("Jeremy", False),
# }
#
# @pytest.mark.parametrize("fn, result", TEST_check_name)
# def test_check_name(fn, result):
#     from mrmadness import check_name
#     assert check_name(fn) == result


# Can't test since function waits for input
# def test_send_a_thank_you(result=None):
#     from mrmadness import send_a_thank_you
#     assert send_a_thank_you() == result



####################
#   Validators
####################
TEST_validate_input = {
    # ("send a thank you", "Enter the first and last name of the donor: (First Last)"),
    ("y", True),
    ("n", False),
    #("p", ),
    # ("q", "SystemExit: 1"),
}
@pytest.mark.parametrize("fn, result", TEST_validate_input)
def test_validate_input(fn, result):
    from mailroom import validate_input
    assert validate_input(fn) == result


TEST_validate_the_fullname = {
    ("Paul Rubens", True),
    ("Old Guy", False),
}

@pytest.mark.parametrize("fn, result", TEST_validate_the_fullname)
def test_validate_the_fullname(fn, result):
    from mailroom import validate_the_fullname
    assert validate_the_fullname(fn) == result
