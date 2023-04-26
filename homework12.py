# Exercise 1 Decorator
def decorator(func):
    from datetime import datetime

    def inner(*args, **kwargs):
        date_start = datetime.now()
        print(f"function {func.__name__} called: {date_start.strftime('%d-%m-%Y %H:%M')}")
        func(*args, **kwargs)

    return inner


@decorator
def summ(a, b):
    print(a + b)


summ(2, 4)

# Exercise 2 ContextManager variant a
from contextlib import contextmanager


@contextmanager
def my_context_manager():
    try:
        print("==========")
        yield
    except Exception:
        print("An unexpected error has occurred")
    print("==========")


with my_context_manager():
    def func(a, b):
        print(a / b)


    func(4, 0)


# Exercise 2 ContextManager variant b
class MyContextManager(object):
    def __init__(self):
        print("==========")

    def __enter__(self):

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("An unexpected error has occurred")
        print("==========")
        return True


with MyContextManager():
    def func(a, b):
        print(a * b)


    func(2, 4)


# Exercise 3 Decorator with times variant a
# def decorator(func):
#     from datetime import datetime
#
#     def inner(*args, **kwargs):
#         date_start = datetime.now()
#         print("Please enter an integer")
#         times = int(input())
#         i = 0
#         while i <= times:
#             print(f"function {func.__name__} called: {date_start.strftime('%d-%m-%Y %H:%M')}")
#             i += 1
#         func(*args, **kwargs)
#
#     return inner
#
#
# @decorator
# def func():
#     print("Helo world")
#
#
# func()
#

# Exercise 3 Decorator with times variant b
# def decorator(func):
#     from datetime import datetime
#
#     def inner(*args, **kwargs):
#         date_start = datetime.now()
#         print("Please enter an integer")
#         times = int(input())
#         print(f"function {func.__name__} called: {date_start.strftime('%d-%m-%Y %H:%M')}\n" * times, end=" ")
#
#         func(*args, **kwargs)
#
#     return inner
#
#
# @decorator
# def func():
#     print("Helo world")
#
#
# func()


# Exercise 3 Decorator with times variant c
# def decorator(func):
#     from datetime import datetime
#
#     def inner(*args, **kwargs):
#         date_start = datetime.now()
#         print("Please enter an integer")
#         times = int(input())
#         for _ in range(times):
#             print(f"function {func.__name__} called: {date_start.strftime('%d-%m-%Y %H:%M')}")
#
#         func(*args, **kwargs)
#
#     return inner
#
#
# @decorator
# def func():
#     print("Helo world")
#
#
# func()


# Exercise 3 Decorator with time. Worked on bugs
import functools

def repeater(times=4):
    def decorator(func):
        from datetime import datetime
        @functools.wraps(func)
        def inner(*args, **kwargs):
            date_start = datetime.now()
            for i in range(times):
                print(f"function {func.__name__} called: {date_start.strftime('%d-%m-%Y %H:%M')}")
            lav = func(*args, **kwargs)
            return lav
        return inner
    return decorator


@repeater(4)
def hello():
    print("Hello world")

hello()