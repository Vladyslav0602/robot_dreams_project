set_first = {1, 2, 5, 11, 13, 18, 33, "book", "pen"}
set_second = {2, 4, 6, 10, 15, 33, "book", "penсill"}


# Exercise 1
def common_values(a, b):
    return a & b


print(common_values(set_first, set_second))


# Exercise 2
def unique_set(a, b):
    return a | b


print(unique_set(set_first, set_second))


# Exercise 3
def convert(i):
    return i.upper()


list1 = ["python", "hello", "world"]

result = list(map(convert, list1))
print(result)

# Exercise 4
list1 = ["hello", 43, 5, 11, 10, "23", 1, "python"]


def filter_number(i):
    if type(i) == int:
        return i


out_filter = filter(filter_number, list1)
print(list(out_filter))
