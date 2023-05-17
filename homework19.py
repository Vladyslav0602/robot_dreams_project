# Exercise 1
class Bot:

    def __init__(self, name):
        self.name = name

    def send_message(self, message):
        print(message)

    def say_name(self):
        print(f"Name: {self.name}")


# some_bot = Bot("Anna")
# some_bot.say_name()
# some_bot.send_message("Hello Anna")


# Exercise 2
class TelegramBot(Bot):
    def __init__(self, name, url=None, chat_id=None):
        super().__init__(name)
        self.url = url
        self.chat_id = chat_id

    def set_url(self, url):
        self.url = url

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

    def send_message(self, message):
        print(f"URL: {self.url},\nSome message:{message},\nId chat_message: {self.chat_id}")


# bot = TelegramBot("Anna")
# bot.set_url("https://my-ua.robotdreams.cc/uk/homework/show/7872")
# bot.set_chat_id("3")
# # print(bot.url)
# # print(bot.chat_id)
# bot.send_message("Hello world")
# bot.say_name()


# Exercise 3 variant a
# class MyStr:
#     def __init__(self, string):
#         self.string = string
#         print(self.string.upper())
#
#
# my_str = MyStr("hello")


# Exercise 3 variant b
class MyStr:
    def __init__(self, some_string):
        self.string = some_string

    def __str__(self):
        return self.string.upper()


# my_str = MyStr("hello")
# print(my_str)


# Exercise 4
class User:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name.casefold() == other.name.casefold()


# first_user = User('OLEKSII')
# second_user = User('Oleksii')
# print(first_user == second_user)


# Exercise 5 variant a
def __init__(self, name, url=None, chat_id=None):
    self.name = name
    self.url = url
    self.chat_id = chat_id


def set_url(self, url):
    self.url = url


def set_chat_id(self, chat_id):
    self.chat_id = chat_id


def send_message(self):
    print(f"Hello world. Send data:\nName - {self.name}\nUrl - {self.url}\nChat_id - {self.chat_id}")


def say_name(self, ):
    print(f"Send name: {self.name}")


Bot = type('Bot', (), {'__init__': __init__,
                       'say_name': say_name,
                       'send_message': send_message,
                       'set_url': set_url,
                       'set_chat_id': set_chat_id})

# some_class = Bot("Vlad")
# some_class.send_message()
# some_class.say_name()

TelegramBot = type('TelegramBot', (Bot,), {})

# second_class = TelegramBot("Anna")
# second_class.set_url("https://www.google.com/")
# second_class.set_chat_id(5)
# second_class.send_message()


# Exercise 5 variant b
new_Bot = type("new_Bot", (Bot,), {})


# some_class = new_Bot("Anna")
# some_class.say_name()
# some_class.send_message("Hello")


new_TelegramBot = type("new_TelegramBot", (TelegramBot,), {})


# second_class = new_TelegramBot("Alex")
# second_class.say_name()
# second_class.set_url("https://www.google.com/")
# second_class.set_chat_id("5")
# second_class.send_message("Hello")


