import re


def validate_phone_and_name(name, phone):
    name_pattern = r"^[A-Za-z]{2,50}$"
    phone_pattern = r"^\+?[0-9]{10,15}$"
    if re.match(name_pattern, name) and re.match(phone_pattern, phone):
        return
    raise ValueError()


def ensure_contact_exists(name, contacts):
    if name not in contacts:
        raise KeyError()