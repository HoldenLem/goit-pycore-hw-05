from src.bot.contact_handler import add_contact, change_contact, get_phone, show_all


def parse_input(user_input: str) -> tuple[str, list[str]]:
    parts = user_input.strip().split()
    if not parts:
        return "", []
    command = parts[0].lower()
    args = parts[1:]
    return command, *args


def print_help():
    return (
        " Available commands:\n"
        "  add <name> <phone>   — add a new contact\n"
        "  change <name> <phone> — update an existing contact\n"
        "  phone <name>        — show phone number of a contact\n"
        "  all                 — show all saved contacts\n"
        "  help                — show this help\n"
        "  exit / close        — quit the bot\n"
    )


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print("Type 'help' to see available commands.\n")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "help":
            print(print_help())
        elif command == "all":
            print(show_all(contacts))
        elif command == "":
            continue
        else:
            print("Unknown command. Type 'help' to see what I can do.")


if __name__ == "__main__":
    main()
