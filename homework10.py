# Exercise 1 recursion variant a
def recursion(n: int):
    print(n, end=" ")
    if n == 0:
        return ""
    return recursion(n - 1)


print("Enter the number: ")
number = int(input())
print(recursion(number))


# Exercise 1 recursion variant b
def recursion(n: int):
    print(n, end=" ")
    while n != 0:
        return recursion(n - 1)
    return ""


print("Enter the number: ")
number = int(input())
print(recursion(number))


# Exercise 2 fibonacci variant a
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print("Enter the number: ")
number = int(input())
print(fib(number))


# Exercise 3 factorial variant a
def factorial(n: int):
    if n == 0:
        return 1
    return factorial(n - 1) * n


print("Enter the number: ")
number = int(input())
print(factorial(number))

# Exercise 3 factorial variant b
print("Enter the number: ")
number = int(input())

factorial = 1

for i in range(2, number + 1):
    factorial *= i

print(factorial)
