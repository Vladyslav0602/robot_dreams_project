# Exercise 1 RegEx
import re
import json

# My phone book


FORMAT_STR = '{:<15} {:>12}'


def stats():
    with open('homework15/phone.txt') as file:
        file_content = file.read()
        if len(file_content) == "":
            print("Phone book is empty")
        else:
            contacts = json.loads(file_content)
            count = len(contacts)
            print(f"There are {count} entries in the phone book")


def add():
    with open('homework15/phone.txt') as file:
        file_content = file.read()
        if file_content == "":
            print("Enter contact name:")
            name = input("> ")
            print("Enter contact phone number:")
            phone = input("> ")
            valid = re.search("(^[+]380.{9}$)|(^380.{9}$)|(^0.{9}$)", phone)
            if valid:
                new_contact = {
                    "name": name,
                    "phone": phone
                }
                contacts = [new_contact]
                print("Contact added")
                with open('homework15/phone.txt', 'w') as file:
                    file.write(json.dumps(contacts))
            else:
                print("Invalid number format entered")
        else:
            contacts = json.loads(file_content)
            print("Enter contact name:")
            name = input("> ")
            print("Enter contact phone number:")
            phone = input("> ")
            valid = re.search("(^[+]380.{9}$)|(^380.{9}$)|(^0.{9}$)", phone)
            if valid:
                new_contact = {
                    "name": name,
                    "phone": phone
                }
                contacts.append(new_contact)
                print("Contact added")
                with open('homework15/phone.txt', '+r') as file:
                    file.write(json.dumps(contacts))
            else:
                print("Invalid number format entered")


def delete():
    with open('homework15/phone.txt') as file:
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
                        with open('homework15/phone.txt', 'w') as file:
                            file.write(json.dumps(contacts))
                else:
                    print("Specified contact not found")


def list():
    with open('homework15/phone.txt') as file:
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
    with open('homework15/phone.txt') as file:
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
print("Please enter a file name: ")
name = input("> ")
if name == "inform":
    with open("homework15/inform.txt") as file:
        file_content = file.read()
        # content = json.loads(file_content)
        valid = re.sub(r"[\w.-]+@[A-Za-z-]+\.[\w.]+", r"*@*", file_content)
        print(valid)
    with open('homework15/result.txt', 'w') as file:
        file.write(valid)
else:
    print("The filename you entered does not exist")

# Exercise 3
def change(match_obj):
    s = match_obj.group(0)
    if s:
        return str(s).replace(s[1:-1], "***@***")


print("Please enter a file name: ")
name = input("> ")
if name == "inform":
    with open("homework15/inform.txt") as file:
        file_content = file.read()
        valid = re.sub(r"[\w.-]+@[A-Za-z-]+\.[\w.]+", change, file_content)
        print(str(valid))
    with open('homework15/result.txt', 'w') as file:
        file.write(valid)
else:
    print("The filename you entered does not exist")
