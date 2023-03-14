# Exercise 1
data = input("Please enter data: ")
if data.isdigit():
    print("Type of data entered number")
elif data.isalpha():
    print("Type of data entered string")
else:
    print("Incorrect data entered")

# Exercise 2
data = input("Please enter data: ")
if data.isdigit():
    print("Type of data entered number")
    if int(data) % 2 == 0:
        print("This is an even number")
    else:
        print("This is an odd number")
else:
    print("Incorrect data entered")

# Exercise 3 variant a
data = input("Please enter data: ")
if data.isalpha():
    print("Type of data entered string")
    print(f"The length of the entered string: {len(data)}")
else:
    print("Incorrect data entered")

# Exercise 3 variant b
data = input("Please enter data: ")
if data.isalpha():
    print("Type of data entered string"+f"\nThe length of the entered string: {len(data)}")
else:
    print("Incorrect data entered")

# Three tasks in one program (Exercise 1, 2, 3)
data = input("Please enter data: ")
if data.isdigit():
    print("Type of data entered number")
    if int(data) % 2 == 0:
        print("This is an even number")
    else:
        print("This is an odd number")
elif data.isalpha():
    print("Type of data entered string"+f"\nThe length of the entered string: {len(data)}")
else:
    print("Incorrect data entered")

# Exercise 4
data = input("Please enter data: ")
match data:
    case data if data.isdigit():
        print("The entered data is a number")
    case data if data.isalpha():
        print("The entered data is a string.")
    case _:
        print("Incorrect data entered")