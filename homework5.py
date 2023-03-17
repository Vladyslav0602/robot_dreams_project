import time
# Exercise 1
data = input("Please enter data: ")
for letter in data:
    if letter.isdigit():
        if int(letter) % 2 == 0:
            print(f"The entered character '{letter}' is a pair number")
        else:
            print(f"The entered character '{letter}' is not a pair number")
    elif letter.isalpha():
        if letter.isupper():
            print(f"The character entered '{letter}' is an uppercase letter")
        else:
            print(f"The entered character '{letter}' is a lowercase letter")
    elif letter != letter.isdigit() and letter != letter.isalpha():
        print(f"The entered character '{letter}' is a character")
    else:
        print("Incorrect data entered")

# Exercise 2 variant a
while True:
    print("I love Python")
    time.sleep(4.2)

# Exercise 3 variant a
rows = 5
for row in range(1, rows+1):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")

# Exercise 3 variant b
rows = 6
for row in range(1, rows):
    for column in range(row, 0, -1):
        print(column, end=' ')
    print("")
