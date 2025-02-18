# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
    # def __str__(self):
    #     return self.name

#     def __repr__(self):
#         return f"Student({self.name}, {self.__age})"
#
# student = Student("John", 18)
#
# print(student)

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, new_age):
#         if new_age > 0:
#             self.__age = new_age
#         else:
#             print("age must be greater than 0")
#
# student1 = Student("John", 18)
# print(student1.age)
#
# student1.age = 20
# print(student1.age)

# def greeting():
#     return "Hello, world!"
#
# greeting.__call__()
# print(greeting.__name__)

# print(callable(greeting))


# class Multiplier:
#
#     def __init__(self, a):
#         self.a = a
#
#     def __call__(self, b):
#         return self.a * b
#
#
# double = Multiplier(2)
# triple = Multiplier(3)
#
# print(double(7))
# print(triple(7))
# print(triple(16))

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         x = args[0] + 2
#         y = args[1] + 5
#         func(x, y)
#     return wrapper
#
#
# @my_decorator
# def print_numbers(a, b):
#     print(f"a: {a}, b: {b}")

# print_numbers(1, 2)
# print_numbers(7, 8)


import time

# def test():
#     for _ in range(3):
#         print("Hello")
#         time.sleep(1)
#
# start = time.time()
# test()
# end = time.time()
#
# print(end - start)


# def time_decorator(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} took {end - start} seconds")
#         return result
#     return wrapper
#
# @time_decorator
# def slow_function():
#     print("Start function")
#     time.sleep(2)
#     print("Finished executing slow_function")
#
# slow_function()

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# s = Student("John", 18)
#
# print(s.__dict__)

# class PositiveNumber:
#     def __init__(self, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         print(f"Getting {self.name}...")
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, int):
#             raise TypeError("Expected int, got {type(value)}")
#         print(f"Setting {self.name} to {value}...")
#         instance.__dict__[self.name] = value
#
#     def __delete__(self, instance):
#         print(f"Deleting {self.name}...")
#         del instance.__dict__[self.name]


# class Person:
#     age = PositiveNumber("age")
#
#
# p = Person()
#
# p.age = 25
# print(p.age)
#
# del p.age
# print(p.age)


# class MyClass:
#     def __new__(cls):
#         print("Creating new instance...")
#         instance = super().__new__(cls)
#         return instance
#
#     def __init__(self):
#         print("Initializing new instance...")
#
# obj = MyClass()

# class MyMeta(type):
#     def __new__(cls, name, bases, class_dict):
#         class_dict['category'] = "General"
#         print(f"Creating new {name}")
#         print(f"Bases: {bases}")
#         print(f"Class dict: {class_dict}")
#         return super().__new__(cls, name, bases, class_dict)
#
# class Product(metaclass=MyMeta):
#     ...
#
# product1 = Product()
#
# print(product1.category)








