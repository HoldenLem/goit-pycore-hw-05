from src.bot.decoration import input_error
from src.bot.validation import ensure_contact_exists, validate_phone_and_name


@input_error
def add_contact(args, contacts) -> str:
    name, phone = args[0], args[1]
    validate_phone_and_name(name, phone)
    contacts[name] = phone
    return f"Contact {name} added with phone {phone}."


@input_error
def change_contact(args, contacts) -> str:
    name, new_phone = args[0], args[1]
    validate_phone_and_name(name, new_phone)
    ensure_contact_exists(name, contacts)
    contacts[name] = new_phone
    return f"Phone number for {name} updated to {new_phone}."


@input_error
def get_phone(args, contacts) -> str:
    name = args[0]
    ensure_contact_exists(name, contacts)
    return f"{name}: {contacts[name]}"


def show_all(contacts) -> str:
    if not contacts:
        return "No contacts yet."
    return "Contacts list: " + "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
