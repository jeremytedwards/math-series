# -*- coding: utf-8 -*-

"""The script should have a data structure that holds a list of your donors and a history of the amounts they have donated.
When run, the script should prompt the user to choose from a menu of 2 actions: ‘Send a Thank You’ or ‘Create a Report’.
If the user selects ‘Send a Thank You’, prompt for a Full Name.

If the user types ‘list’, show them a list of the donor names and re-prompt
If the user types a name not in the list, add that name to the data structure and use it.
If the user types a name in the list, use it.

Once a name has been selected, prompt for a donation amount.
Verify that the amount is in fact a number, and re-prompt if it isn’t.
Once an amount has been given, add that amount to the donation history of the selected user.
Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.
You need not persist the new donors when the script quits running.

If the user (you) selected ‘Create a Report’ Print a list of your donors, sorted by total historical donation amount.
Include Donor Name, total donated, number of donations and average donation amount as values in each row.
Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below)
After printing this report, return to the original prompt.
At any point, the user should be able to quit their current task and return to the original prompt.
From the original prompt, the user should be able to quit the script cleanly.
"""



import sys

default_ty_email = "\nThanks dooder {name},\n You are the best donor we have.\n\nSrsly,\n\nMr. Nice Guy\n"
default_menu = "'send a thank you’ or ‘create a report’ or 'list' (type 'q' to quit)"

# Total amount donors have donated (firstName: { total: 0, num_donations: 0, ave_donations: 0})
donor_dict = {"firstName": {
    "total": 0,
    "num_donations": 0,
    "ave_donations": 0
}}


# look at __future__
# try:
#     input = raw_input
# except NameError:
#     pass



##########
#   Getters and Setters
##########
def add_donor_to_report(donor):
    donor_dict.update({donor: {}})
    print donor_dict


def get_total_donations(donor):
    return donor_dict.get(donor).__getitem__("total")


def set_total_donations(donor, dollars):
    holder = donor_dict.get(donor)
    total_dollars = holder.__getitem__("total") + dollars
    donor_dict.update({donor: {"total": total_dollars}})


# def get_donation_total():
#     pass
#
# def set_donation_total(donation_value):
#     pass
#
#
# def get_ave_donations():
#     pass
#
# def set_ave_donations(donation_value):
#     pass



##########
#   Outputs
##########
def send_reply_email(donor_name):
    # TODO: Review Formatter
    print default_ty_email.format(name=donor_name)

# def print_sorted_donors_list(donor_list, sort):
#     # sort by donation amount desc
#     sorted_donor_dollars = donor_list.sort(donor_list.values(), sort)
#
#     #Include Donor Name, total donated, number of donations and average donation amount as values in each row.
#     #Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below)
#
#     print(sorted_donor_dollars)
#     return None
#
#
# def print_donors_names(donor_list):
#     print(donor_list.keys)
#     return None



##########
#   Get Input
##########
def ask_for_input(question, validator=True):
    usr_input = raw_input("\n" + question + "\n>>> ")

    if validator:
        return validate_input(usr_input)
    else:
        return usr_input



def check_name(fullname):
    in_the_report = validate_the_fullname(fullname)
    if not in_the_report:
        yn = ask_for_input("{name} is not in the report, would you like to add them? (y/n)".format(name=fullname))
        if yn:
            add_donor_to_report(fullname)
            return True
        else:
            return False
    else:
        return True


def send_a_thank_you():
        full_name = raw_input('Enter the first and last name of the donor: (First Last)')
        valid = check_name(full_name)

        if valid:
            send_reply_email(full_name)
            ask_for_input(default_menu)
        else:
            ask_for_input(default_menu)


    # #Create a Report
    #
    #    print_sorted_donors_list(donor_dollars, "desc")
    #    ask_for_input(menu)
    #
    # #Print a list of donors with total amounts
    #
    #     print_donors_names(donor_dollars)
    #     ask_for_input("", False)
    #
    # #Get the dollars donation in +/- dollars
    # elif usr_input.lower() == '$':
    #     answer = validate_the_donation(usr_input)
    #     return answer




##########
#   Validators
##########
def validate_input(response):
    if response.lower() == 'send a thank you':
        send_a_thank_you()
    # elif response.lower() == 'create a report':
    #      create_a_report()
    # elif response.lower() == 'list':
    elif response.lower() == 'y':
        return True
    elif response.lower() == 'n':
        return False
    elif response.lower() == 'q':
        sys.exit(1)
    else:
        ask_for_input("Oops, didn't understand your input.\n " + default_menu)

def validate_the_fullname(full_name):
    # is the user in the donor_dict
    if full_name not in donor_dict:
        return False
    else:
        return True


def main():
    """handle the args from user input and call the appropriate functions"""
    ask_for_input(default_menu)


if __name__ == "__main__":
    sys.exit(main())
