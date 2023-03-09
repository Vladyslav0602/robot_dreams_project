# Exercise 1 variant a
i = 1
while i < 42:
    print("I love Python")
    i += 1
print("Phrase \"I love python\" displayed %s times" % i)

# Exercise 1 variant b
phrase = "I love Python"
for i in range(43):
    print(phrase)
print("Phrase \"I love python\" displayed %s times" % i)

# Exercise 2 variant a
age_in_month = 28 * 12
print("My age in months: %s months" % age_in_month)

# Exercise 2 variant b
years = int(input("Please enter your age in years "))
age_in_month = years * 12
print("My age in months: %s" % age_in_month)

# Exercise 2 variant c
days = int(input("Please enter your age in days "))
age_in_years = days // (365-5)
age_in_month = days // 30
print("My age in years: %s" % age_in_years)
print("My age in month: %s" % age_in_month)
print("My age in days: %s" % days)

# Exercise 2 variant d
age_in_month = int(input("Please enter your age in years "))
if age_in_month >= 1 and age_in_month <= 100:
    age_in_month *= 12
    print("My age in months: %s months" % age_in_month)
else:
    print("Incorrect number of years entered")

# Exercise 3 variant a
age_in_years = age_in_month // 12 or (age_in_month * 30) // 360
print(age_in_years)

# Exercise 3 variant b
age_in_years_a = age_in_month // 12
age_in_years_b = (age_in_month * 30) // 360
if age_in_years_a == age_in_years_b:
    age_in_years = age_in_years_a = age_in_years_b
    print("My age in years: %s" % age_in_years)
else:
    print("Calculation error")

# Exercise 4
my_name = "Vlad"
my_age = f"Му name is {my_name} . I’m {age_in_years} years old"
print(my_age)

# Exercise 5
value = 1
print(value == phrase)
print(value > age_in_years)
print(value < age_in_month)
print(value >= i)
print(value != my_name)
print(value <= age_in_years_a)

# Exercise 6
a = 2
b = 5
c = 6
d = str(a) + str(b) + str(c)
print(d)