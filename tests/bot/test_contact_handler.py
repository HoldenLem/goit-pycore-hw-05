import pytest
from src.bot import contact_handler as ch

INVALID_FORMAT_MESSAGE = (
    "Please provide name and a phone number CORRECTLY.\n"
    "Name: 2–50 English letters only\n"
    "Phone: 10–15 digits, may start with +"
)


@pytest.fixture()
def contacts():
    return {}

def test_valid_add_contact(contacts):
    result = ch.add_contact(["Alice", "+12345678901"], contacts)
    assert result == "Contact Alice added with phone +12345678901."
    assert contacts == {"Alice": "+12345678901"}


def test_add_contact_invalid_format(contacts):
    res1 = ch.add_contact(["John Doe", "12345"], contacts)
    assert res1 == INVALID_FORMAT_MESSAGE
    assert contacts == {}

    res2 = ch.add_contact(["A", "+1234567890"], contacts)
    assert res2 == INVALID_FORMAT_MESSAGE
    assert contacts == {}


def test_add_contact_usage_when_args_missing(contacts):
    res = ch.add_contact(["OnlyName"], contacts)
    assert res == "Please provide both a name and a phone number."
    assert contacts == {}


def test_change_contact_not_found(contacts):
    res = ch.change_contact(["Bob", "+12345678901"], contacts)
    assert res == "Contact not found."


def test_change_contact_invalid_phone(contacts):
    ch.add_contact(["Eve", "+12345678901"], contacts)
    res = ch.change_contact(["Eve", "abcd123"], contacts)
    assert res == INVALID_FORMAT_MESSAGE
    assert contacts["Eve"] == "+12345678901"


def test_change_contact_success(contacts):
    ch.add_contact(["Mike", "+11111111111"], contacts)
    res = ch.change_contact(["Mike", "+22222222222"], contacts)
    assert res == "Phone number for Mike updated to +22222222222."
    assert contacts["Mike"] == "+22222222222"


def test_change_contact_usage_when_args_missing(contacts):
    res = ch.change_contact(["Mike"], contacts)
    assert res == "Please provide both a name and a phone number."


def test_get_phone_found_and_not_found(contacts):
    ch.add_contact(["Lara", "+33333333333"], contacts)
    found = ch.get_phone(["Lara"], contacts)
    assert found == "Lara: +33333333333"

    not_found = ch.get_phone(["Someone"], contacts)
    assert not_found == "Contact not found."

    usage = ch.get_phone([], contacts)
    assert usage == 'Please provide a name after a command <phone>.'


def test_show_all_empty_and_non_empty(contacts):
    empty = ch.show_all(contacts)
    assert empty == "No contacts yet."

    ch.add_contact(["Ann", "+44444444444"], contacts)
    out = ch.show_all(contacts)
    assert out.startswith("Contacts list:")
    assert "Ann: +44444444444" in out
