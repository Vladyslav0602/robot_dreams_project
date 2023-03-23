from functools import reduce

# Exercise 1 variant a


def degree_of_number(a, b):
    return a ** b


print(degree_of_number(3, 3))

# Exercise 1 variant b


def degree_of_number(a, b):
    return a ** b


result = degree_of_number(4, 4)
print(result)

# Exercise 2 variant a


def sum_of_numbers(*nums):
    amount = 0
    for n in nums:
        amount += n
    print("Sum: ", amount)


sum_of_numbers(2, 4, 5, 6)

# Exercise 2 variant b


def sum_of_numbers(**nums):
    amount = 0
    for k, n in nums.items():
        amount += n
    print("Sum: ", amount)


sum_of_numbers(a=4, b=6, c=5, d=5)

# Exercise 3 variant a
data_set = [2, 5, 6, 7, 8, 23, 11]
max_number = max(data_set)
print(max_number)

# Exercise 3 variant b


def largest(list1):
    max_ = list1[0]
    for i in list1:
        if i > max_:
            max_ = i
    return max_


data_set = [2, 5, 6, 7, 8, 23, 11]
result = largest(data_set)
print(result)

# Exercise 3 variant c
data_set = [2, 5, 6, 7, 8, 23, 11]
print(reduce(max, data_set))

# Exercise 3 variant d
data_set = [2, 5, 6, 7, 8, 23, 11]
print(reduce(lambda x, y: x if x > y else y, data_set))