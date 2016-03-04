# -*- coding: utf-8 -*-

import sys
import re

# TODO: look at __future__ for handling input between py27 and py35
# try:
#     input = raw_input
# except NameError:
#     pass


# DONOR_DICT = {}

# Below Dictionary is for testing, pre-seeds some data
DONOR_DICT = {
    "Paul Rubens": {"donation_total": 100, "donation_ave": 100, "donation_count": 1},
    "Peter Paul": {"donation_total": 50000, "donation_ave": 10000, "donation_count": 5},
    "Jeremy Edwards": {"donation_total": 1000, "donation_ave": 1000, "donation_count": 1},
    "Michael Jackson": {"donation_total": 100000, "donation_ave": 1000, "donation_count": 100},
}

DEFAULT_TY_EMAIL = "\nThanks dooder {name},\n You are the best donor we have.\n\nSrsly,\n\nMr. Nice Guy\n"
DEFAULT_DONATION_EMAIL = "\nThanks dooder {name},\n Your donation was critical to our success.\n\nSrsly,\n\nMr. Nice Guy\n"
DEFAULT_MENU = "'send a thank you’ or ‘create a report’ or 'list' (type 'q' to quit)"


##########
#   Getters and Setters
##########
def add_donor_to_report(donor):
    DONOR_DICT.update({donor: {"donation_total": 0, "donation_ave": 0, "donation_count": 0}})
    print DONOR_DICT


def get_donation_total(donor):
    return DONOR_DICT.get(donor).get("donation_total")


def set_donation_total(donor, dollars):
    # TODO: try and extract the dollar amount from a string with numbers
    # str_dollars = re.findall(r"\d+", dollars)

    total_dollars = DONOR_DICT.get(donor).get("donation_total") + int(dollars)
    DONOR_DICT.update({donor: {"donation_total": total_dollars}})

    set_donor_count(donor)
    set_donation_ave(donor)


def set_donor_count(donor):
    total_donation_count = DONOR_DICT.get(donor).get("donation_count") + 1
    DONOR_DICT.update({donor: {"donation_count": total_donation_count}})


def get_donation_ave(donor):
    return DONOR_DICT.get(donor).get("donation_ave")


def set_donation_ave(donor):
    donation_average = DONOR_DICT.get(donor).get("donation_ave") / DONOR_DICT.get(donor).get("donation_count")
    DONOR_DICT.update({donor: {"donation_ave": donation_average}})


####################
#   Outputs
####################
def send_reply_email(donor_name):
    # TODO: Review Formatter
    print DEFAULT_TY_EMAIL.format(name=donor_name)


def send_donor_email(donor_name):
    # TODO: Review Formatter
    print DEFAULT_DONATION_EMAIL.format(name=donor_name)


def print_donors_names():
    for donor in DONOR_DICT.keys():
        print donor


def print_sorted_donors_list():
    # Sort the DONOR_DICT to temp list sorted_list[]
    sorted_list = []

    '''
    sorted(iterable, key) a built in Python function, takes an iterable and a key
    so we're going to interate over each key in our DONOR_DICT and sort by the 'donation_count' from our donor of values

    DONOR_DICT.iteritems() returns a (key, value) tuple, that gets passed to lambda (key, val)
    'val' is the dictionary of values we tracked in our DONOR_DICT for the values {key: {val:values}}
    'donation_total' is the value in the nested dictionary that we wanted to sort by
    '''
    for sorted_donation_count in sorted(DONOR_DICT.iteritems(), key=lambda (key, val): val['donation_total']):
        sorted_list.append(sorted_donation_count)
        # print(sorted_donation_count)   # used for debugging

    # Include Donor Name, total donated, number of donations and average donation amount as values in each row.
    print("\n")
    print "{:<15} {:<15} {:<20} {:<15}".format('Donor Name', 'Donations', 'Average Donation', 'Total Donated')
    print "{:<15} {:<15} {:<20} {:<15}".format('----------', '----------', '-----------------', '---------------')
    for k, v in sorted_list:
        print "{:<15} {:<15} {:<20} {:<15}".format(k, v.get("donation_count"), v.get("donation_ave"), v.get("donation_total"))
    print("\n")


####################
#   Get Input
####################
def ask_for_input(question, validator=True):
    usr_input = raw_input("\n" + question + "\n>>> ")
    if validator:
        return validate_input(usr_input)
    else:
        return usr_input


def check_name(fullname):
    in_the_report = validate_the_fullname(fullname)
    if not in_the_report:
        yn_name = ask_for_input("{name} is not in the report, would you like to add them? (y/n)".format(name=fullname))
        if yn_name:
            add_donor_to_report(fullname)
            dollars = ask_for_input("How much did this user donate?", False)
            if dollars:
                set_donation_total(fullname, dollars)

            return True
        else:
            return False
    else:
        return True


def send_a_thank_you():
        full_name = ask_for_input('Enter the first and last name of the donor: (First Last)', False)
        valid = check_name(full_name)

        if valid:
            send_reply_email(full_name)



####################
#   Validators
####################
def validate_input(response):
    if response.lower() == 'send a thank you':

        send_a_thank_you()
        ask_for_input(DEFAULT_MENU)
    elif response.lower() == 'create a report':
        print_sorted_donors_list()
    elif response.lower() == 'list':
        print_donors_names()
        ask_for_input(DEFAULT_MENU)
    elif response.lower() == 'y':
        return True
    elif response.lower() == 'n':
        return False
    elif response.lower() == 'q':
        sys.exit(1)
    else:
        ask_for_input("Oops, didn't understand your input.\n " + DEFAULT_MENU)


def validate_the_fullname(full_name):
    # is the user in the donor_dict
    if full_name not in DONOR_DICT:
        return False
    else:
        return True


def main():
    """handle the args from user input and call the appropriate functions"""
    ask_for_input(DEFAULT_MENU)


if __name__ == "__main__":
    sys.exit(main())

'''
DONE: The script should have a data structure that holds a list of your donors and a history of the amounts they have donated.
DONE: When run, the script should prompt the user to choose from a menu of 2 actions: ‘Send a Thank You’ or ‘Create a Report’.
DONE: If the user selects ‘Send a Thank You’, prompt for a Full Name.

DONE: If the user types ‘list’, show them a list of the donor names and re-prompt
DONE: If the user types a name not in the list, add that name to the data structure and use it.
DONE: If the user types a name in the list, use it.

DONE: Once a name has been selected, prompt for a donation amount.

TODO: Verify that the amount is in fact a number, and re-prompt if it isn’t.
DONE: Once an amount has been given, add that amount to the donation history of the selected user.
TODO: Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.

DONE: You need not persist the new donors when the script quits running.

DONE: If the user (you) selected ‘Create a Report’ Print a list of your donors, sorted by total historical donation amount.
DONE: Include Donor Name, total donated, number of donations and average donation amount as values in each row.
DONE: Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below)
TODO: After printing this report, return to the original prompt.

TODO: At any point, the user should be able to quit their current task and return to the original prompt.
DONE: From the original prompt, the user should be able to quit the script cleanly.
'''