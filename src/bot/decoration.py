INVALID_FORMAT_MESSAGE = (
    "Please provide name and a phone number CORRECTLY.\n"
    "Name: 2–50 English letters only\n"
    "Phone: 10–15 digits, may start with +"
)


def input_error(func):
    def inner(*args, **kwargs):
        current_func = func.__name__
        try:
            return func(*args, **kwargs)

        except ValueError:
            if current_func in ('add_contact', 'change_contact'):
                return INVALID_FORMAT_MESSAGE
            return "Invalid input."

        except IndexError:
            if current_func in ('add_contact', 'change_contact'):
                return "Please provide both a name and a phone number."
            if current_func == 'get_phone':
                return "Please provide a name after a command <phone>."
            return "Not enough arguments."

        except KeyError:
            if current_func in ('change_contact', 'get_phone'):
                return "Contact not found."
            return "Key not found."

    return inner
