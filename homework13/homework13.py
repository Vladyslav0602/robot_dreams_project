# Exercise 1 phonebook
import json


# MyCustomException
class MyCustomException(Exception):
    def __init__(self, text):
        self.txt = text


# My phone book
# contacts = []

FORMAT_STR = '{:<15} {:>12}'


def stats():
    with open('homework13/phonebook.txt') as file:
        file_content = file.read()
        if len(file_content) == "":
            print("Phone book is empty")
        else:
            contacts = json.loads(file_content)
            count = len(contacts)
            print(f"There are {count} entries in the phone book")


def add():
    with open('homework13/phonebook.txt') as file:
        file_content = file.read()
        if file_content == "":
            print("Enter contact name:")
            name = input("> ")
            try:
                print("Enter contact phone number:")
                phone = input("> ")
                if len(phone) >= 9:
                    new_contact = {
                        "name": name,
                        "phone": phone
                    }
                    contacts = [new_contact]
                    print("Contact added")
                    with open('homework13/phonebook.txt', 'w') as file:
                        file.write(json.dumps(contacts))
                else:
                    raise MyCustomException("Phone number is too short")
            except MyCustomException:
                print("Custom exception is occurred")
        else:
            contacts = json.loads(file_content)
            print("Enter contact name:")
            name = input("> ")
            try:
                print("Enter contact phone number:")
                phone = input("> ")
                if len(phone) >= 9:
                    new_contact = {
                        "name": name,
                        "phone": phone
                    }
                    contacts.append(new_contact)
                    print("Contact added")
                    with open('homework13/phonebook.txt', '+r') as file:
                        file.write(json.dumps(contacts))
                else:
                    raise MyCustomException("Phone number is too short")
            except MyCustomException:
                print("Custom exception is occurred")


def delete():
    with open('homework13/phonebook.txt') as file:
        file_content = file.read()
        if file_content == "":
            print("Phone book is empty")
        else:
            contacts = json.loads(file_content)
            print("Enter contact name: ")
            name = input("> ")
            for contact in contacts:
                if contact["name"] == name:
                    print(f"Do you want to delete a contact? {name} (yes/no)?: ")
                    name_del = input("> ")
                    if name_del == "yes":
                        contacts.remove(contact)
                        print(f"The contact has been deleted {name} ")
                        with open('homework13/phonebook.txt', 'w') as file:
                            file.write(json.dumps(contacts))
                else:
                    print("Specified contact not found")


def list():
    with open('homework13/phonebook.txt') as file:
        file_content = file.read()
    if file_content == "":
        print("Phone book is empty")
    else:
        contacts = json.loads(file_content)
        print(FORMAT_STR.format("Name", "Phone"))
        for contact in contacts:
            print(FORMAT_STR.format(
                contact['name'],
                contact['phone']
            ))


def show():
    with open('homework13/phonebook.txt') as file:
        file_content = file.read()
        if len(file_content) == 0:
            print("Phone book is empty")
        else:
            contacts = json.loads(file_content)
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

while True:
    try:
        print("\nEnter command: ")
        command = input("> ")
        if command == "stats":
            stats()
        elif command == "add":
            add()
        elif command == "delete":
            delete()
        elif command == "list":
            list()
        elif command == "show":
            show()
        elif command == "exit":
            break
        else:
            print("Unknown command")
    except KeyboardInterrupt:
        print("Interrupted")


# Exercise 2
def decorator(func):
    from datetime import datetime

    def inner(*args, **kwargs):
        date_start = datetime.now()
        func(*args, **kwargs)
        with open('homework13/inform.txt', 'w') as f:
            f.write(f"function {func.__name__} called: {date_start.strftime('%d-%m-%Y %H:%M')}")

    return inner


@decorator
def hello():
    print("Hello world")


hello()


# Exercise 3
class MyCustomException(Exception):
    def __init__(self, text):
        from datetime import datetime
        date_start = datetime.now()
        self.txt = text
        with open('homework13/inform.txt', 'w') as f:
            f.write(f"Exception {text} called: {date_start.strftime('%d-%m-%Y %H:%M')}")


print("Enter contact phone number:")
phone = input("> ")
try:
    if len(phone) <= 9:
        raise MyCustomException("'Incorrect number format'")
except MyCustomException:
    print("Custom exception is occurred")
else:
    print("Contact added")
