# def add(a, b):
#     return a + b
#
# added = add(1, 3)
#
# print(added)

# def add_nums(*args):
    # for num in args:
    #     print(num)
    # return sum(args)

# print(add_nums(1, 2, 3, 6, 4))

# def greeting(name, message):
#     return f"Name: {name}\nMessage: {message}"


# print(greeting("John", "Hello"))
# print(greeting("Hello", "John"))
# print(greeting(name = "John", message = "Hello"))
# print(greeting(message = "Hello", name = "John"))
#
# def greeting(name, message, age):
#     return f"{message} {name}, you are {age} years old"
#
# print(greeting( "John", age = 24, message = "Welcome to Python!"))

# def display_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# display_info(name = "Alice", age = 25)

# def test(*args, **kwargs):
#     print(f"Positional arguments: {args}")
#     print(f"Keyword arguments: {kwargs}")
#
# test("Hello", "World", name = "Otar", age = 25)

# def person(name, age):
#     return f"Hello, {name}! You are {age} years old."
#
# person_lst = ["Otar", 30]
#
# print(person(*person_lst))

# person = {
#     "name": "Otar",
#     "age": 22,
#     "city": "San Jose"
# }
#
# def person_details(name, age, city):
#     return f"Hello, {name}! You are {age} years old and you live in {city}."
#
# print(person_details(**person))

# def calc_area(width = 1, height = 1):
#     return width * height

# print(calc_area())
# print(calc_area(5))
# print(calc_area(5, 6))

# x = 10
#
# def outer():
#     # x = 5
#
#     def inner():
#         # x = 2
#         print(x)
#     inner()
#
# outer()


# x = 10
#
# def test():
#     global x
#     x = x + 1
#     print(x)
#
# test()

# def outer():
#     x = "Enclosing"
#
#     def inner():
#         nonlocal x
#         x = "Modifying"
#         print(x)
#
#     inner()
#     print(x)
#
# outer()

# def add(a, b):
#     return a + b
#
# # added = add(1, 2)
#
# added = add
#
# print(added(2, 3))

# def calc(asd, a, b):
#     return asd(a, b)
#
# def add(a, b):
#     return a + b
#
# def sub(a, b):
#     return a - b
#
# def mul(a, b):
#     return a * b
#
# print(calc(add, 3, 2))
# print(calc(sub, 3, 2))
# print(calc(mul, 3, 2))

# def get_multiplier(a):
#     def multiplier(b):
#         return a * b
#     return multiplier
#
# multiplier_by_5 = get_multiplier(5)
# multiplier_by_7 = get_multiplier(7)

# print(multiplier_by_5(10))
# print(multiplier_by_5(6))

# print(multiplier_by_7(8))
# print(multiplier_by_7(11))
#
# def add(a, b):
#     return a + b
#
# def multiply(a, b):
#     return a * b
#
# def divide(a, b):
#     return a / b
#
# lst = [add, multiply, divide]
#
# for func in lst:
#     print(func(5, 8))


# 5! = 5 X 4 X 3 X 2 X 1

# def factorial(number):
#     print(number)
#     if number == 0:
#         return 1
#     return number * factorial(number - 1)
#
# print(factorial(5))

# from module import add
#
# print(add(1, 2))