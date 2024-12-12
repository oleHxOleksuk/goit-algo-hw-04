def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def show_all(contacts:dict):
    if contacts:
        all_contact = "Contcts:"
        for name,phone in contacts.items():
            all_contact += f"\n{name}:{phone}"
        return all_contact
    else:
        return "Is not contacts"
    
def show_phone(args:list, contacts:dict):
    name = args[0]
    if name not in contacts:
        return "Contact does not exist"
    else:
        return contacts[name]


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

