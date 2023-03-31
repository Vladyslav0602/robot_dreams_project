#My phone book
contacts = []

FORMAT_STR = '{:<15} {:>12}'


def stats(contacts):
    count = len(contacts)
    print(f"There are {count} entries in the phone book")


def add(contacts):
    print("Enter contact name:")
    name = input("> ")
    print("Enter contact phone number:")
    phone = input("> ")
    new_contact = {
        "name": name,
        "phone": phone
    }
    contacts.append(new_contact)
    print("Contact added")


def delete(contacts):
    print("Enter contact name: ")
    name = input("> ")
    for contact in contacts:
        if contact["name"] == name:
            print(f"Do you want to delete a contact? {name} (yes/no)?: ")
            name_del = input("> ")
            if name_del == "yes":
                contacts.remove(contact)
                print(f"The contact has been deleted {name} ")
        else:
            print("Specified contact not found")


def list(contacts):
    if len(contacts) == 0:
        print("Phone book is empty")
    else:
        print(FORMAT_STR.format("Name", "Phone"))
        for contact in contacts:
            print(FORMAT_STR.format(
                contact["name"],
                contact["phone"]
            ))


def show(contacts):
    print("Enter contact name:")
    name = input("> ")

    for contact in contacts:
        if contact['name'] == name:
            print(FORMAT_STR.format("Name", "Phone"))
            print(FORMAT_STR.format(
                contact['name'],
                contact['phone']
            ))
            break
    else:
        print("Contact not found")


print("Welcome to the phone book.")
print("""Please enter command:
* stats     - To see the number of records
* add       - Add contact
* delete    - Delete contact(by name)
* list      - List of all names in the book
* show      - Detailed information (by name)
* exit      - Exiting the program""")

while True:
    print("\nEnter command: ")
    command = input("> ")
    if command == "stats":
        stats(contacts)
    elif command == "add":
        add(contacts)
    elif command == "delete":
        delete(contacts)
    elif command == "list":
        list(contacts)
    elif command == "show":
        show(contacts)
    elif command == "exit":
        break
    else:
        print("Unknown command")