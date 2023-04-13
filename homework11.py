# MyCustomException
class MyCustomException(Exception):
    def __init__(self, text):
        self.txt = text


# My phone book
contacts = []

FORMAT_STR = '{:<15} {:>12}'


def stats(contacts):
    count = len(contacts)
    print(f"There are {count} entries in the phone book")


# Function add with construction try/except MyCustomException variant a
# def add(contacts):
#     print("Enter contact name:")
#     name = input("> ")
#     print("Enter contact phone number:")
#     try:
#         phone = input("> ")
#         if len(phone) < 9:
#             raise MyCustomException("Phone number is too short")
#     except MyCustomException:
#         print("Custom exception is occurred")
#     if len(phone) >= 9:
#         new_contact = {
#             "name": name,
#             "phone": phone
#         }
#         contacts.append(new_contact)
#         print("Contact added")


# Function add with construction try/except MyCustomException variant b
def add(contacts):
    print("Enter contact name:")
    name = input("> ")
    print("Enter contact phone number:")
    phone = input("> ")
    try:
        if len(phone) >= 9:
            new_contact = {
                "name": name,
                "phone": phone
            }
            contacts.append(new_contact)
            print("Contact added")
        else:
            raise MyCustomException("Phone number is too short")
    except MyCustomException:
        print("Custom exception is occurred")


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


# Function show with construction try/except NameError variant a
# def show(contacts):
#     print("Enter contact name:")
#     try:
#         name = input("> ")
#         contact['name']is None
#     except NameError:
#         print("The specified name does not exist")
#
#     for contact in contacts:
#         if contact['name'] == name:
#             print(FORMAT_STR.format("Name", "Phone"))
#             print(FORMAT_STR.format(
#                 contact['name'],
#                 contact['phone']
#             ))
#             break
# else:
#     print("Contact not found")


# Function show with construction try/except NameError variant b
def show(contacts):
    print("Enter contact name:")
    name = input("> ")
    try:
        for contact in contacts:
            if contact['name'] == name:
                print(FORMAT_STR.format("Name", "Phone"))
                print(FORMAT_STR.format(
                    contact['name'],
                    contact['phone']
                ))
                break
        else:
            raise NameError("Non-existent name")
    except NameError:
        print("The specified name does not exist")


print("Welcome to the phone book.")
print("""Please enter command:
* stats     - To see the number of records
* add       - Add contact
* delete    - Delete contact(by name)
* list      - List of all names in the book
* show      - Detailed information (by name)
* exit      - Exiting the program""")

# Construction try/except KeyboardInterrupt
while True:
    try:
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
    except KeyboardInterrupt:
        print("Interrupted")
