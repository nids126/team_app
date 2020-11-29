# coding=utf-8
# Written By: Nidhi Sahu
import re

"""
Function to check if all required fields are present
"""
def check_required_fields(_json, fields):
    missing_fields = []
    for field in fields:
        if field not in _json or not _json.get(field):
            missing_fields.append(field)
    return missing_fields


def is_valid_phone_number(phone_number):
    # 1) Begins with 0 or 91 (This is optional)
    # 2) Then contains 7 or 8 or 9.
    # 3) Then contains 9 digits
    regex = r"^(0/91)?[6-9][0-9]{9}"
    return re.search(regex, phone_number)


def is_valid_email(email):
    # regular expression for validating an Email
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.search(regex, email)
