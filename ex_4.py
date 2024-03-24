def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No users data"
        except IndexError:
            return "Index out of range."

    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name not in contacts:
        raise ValueError(f"Contact '{name}' not found")
    contacts[name] = new_phone
    return f"Contact '{name}' updated successfully"


@input_error
def show_contact(args, contacts):
    name = ' '.join(args)
    return contacts.get(name, "Contact not found")


@input_error
def show_all_contacts(contacts):
    if not contacts:
        return "No contacts found."
    else:
        contacts_str = ""
        for name, phone in contacts.items():
            contacts_str += f"{name}: {phone}\n"
        return contacts_str.strip() 


@input_error
def show_phone(args, contacts):
    name = args[0]
    phone = contacts.get(name)
    if phone is not None:
        return f"{name}'s phone number is: {phone}"
    else:
        return f"Contact '{name}' not found."
    

@input_error
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "show":
            print(show_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all_contacts(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()