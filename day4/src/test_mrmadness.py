# -*- coding: utf-8 -*-

import pytest

##########
#   Getters and Setters
##########
def test_add_donor_to_report(fn="New Guy", result=None):
    from mrmadness import add_donor_to_report
    assert add_donor_to_report(fn) == result


def test_get_donation_total(fn="Michael Jackson", result=100000):
    from mrmadness import get_donation_total
    assert get_donation_total(fn) == result


# TODO: need to add regex to select numbers first before all test here will pass
TEST_set_donation_total = {
    # ("Paul Rubens", "$10000", None),
    # ("Paul Rubens", "10,000", None),
    # ("Paul Rubens", "$10000.00", None),
    ("Paul Rubens", "10000", None),

}

@pytest.mark.parametrize("donor, fn, result", TEST_set_donation_total)
def test_set_donation_total(donor, fn, result):
    from mrmadness import update_donation_total
    assert update_donation_total(donor, fn) == result


def test_update_donor_count(fn="Paul Rubens", result=None):
    from mrmadness import update_donor_count
    assert update_donor_count(fn) == result


def test_get_donation_ave(fn="Peter Paul", result=10000):
    from mrmadness import get_donation_ave
    assert get_donation_ave(fn) == result


def test_update_donation_ave(fn="Michael Jackson", result=None):
    from mrmadness import update_donation_ave
    assert update_donation_ave(fn) == result





####################
#   Outputs
####################
def test_send_reply_email(fn="Paul Rubens", result=None):
    from mrmadness import send_reply_email
    assert send_reply_email(fn) == result


def test_send_donor_email(fn="Paul Rubens", result=None):
    from mrmadness import send_donor_email
    assert send_donor_email(fn) == result


def test_print_donors_names(result=None):
    from mrmadness import print_donors_names
    assert print_donors_names() == result


def test_print_sorted_donors_list(result=None):
    from mrmadness import print_sorted_donors_list
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
    from mrmadness import validate_input
    assert validate_input(fn) == result


TEST_validate_the_fullname = {
    ("Paul Rubens", True),
    ("Old Guy", False),
}

@pytest.mark.parametrize("fn, result", TEST_validate_the_fullname)
def test_validate_the_fullname(fn, result):
    from mrmadness import validate_the_fullname
    assert validate_the_fullname(fn) == result
