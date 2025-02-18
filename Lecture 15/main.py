# class Editor:
#     def __init__(self, name):
#         self.name = name
#
#     def execute(self):
#         print("Compiling...")
#         print("Executing...")
#
# class Pycharm:
#     def __init__(self, name):
#         self.name = name
#
#     def execute(self):
#         print("Check spelling...")
#         print("Debugging")
#         print("Compiling...")
#         print("Executing...")
#
# ide1 = Editor("Ide1")
# ide2 = Pycharm("Pycharm")
#
# class Laptop:
#     def coding(self, editor):
#         if hasattr(editor, "execute"):
#             editor.execute()
#         else:
#             print(f"{editor.name} can not execute code")
#
# laptop = Laptop()
# laptop.coding(ide1)
# laptop.coding(ide2)
from dateutil.rrule import weekday


# from abc import ABC, abstractmethod
#
# class Vehicle(ABC):
#
#     @abstractmethod
#     def max_speed(self):
#         pass
#
# class Car(Vehicle):
#
#     def info(self):
#         print("My car is BMW")
#
#     def max_speed(self):
#         print("Car's max speed is 220km/h")
#
#
# class Motorcycle(Vehicle):
#
#     def max_speed(self):
#         print("Motorcycle's max speed is 250km/h")
#
#
# car = Car()
# bike = Motorcycle()
#
# car.info()
# car.max_speed()
# bike.max_speed()


# class Player:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#
#     def __repr__(self):
#         return f"Player({self.name}, {self.position})"
#
#     def __str__(self):
#         return f"Player: {self.name}, position: {self.position}"
#
# player = Player("John", "GK")

# print(player)
# print(repr(player))
# print(str(player))


# class Player:
#     def __init__(self, name, goals):
#         self.name = name
#         self.goals = goals
#
#     def __add__(self, other):
#         if isinstance(other, Player):
#             return Player(f"{self.name} & {other.name}", self.goals + other.goals)
#         return f"second player should be Player object"
#
#     def __repr__(self):
#         return f"Player(names={self.name}, goals={self.goals})"
#
# p1 = Player("Ronaldo", 20)
# p2 = Player("Messi", 18)

# print(p1 + p2)

# print(isinstance(p1, Player))

#
# class Student:
#
#     pay = 1000
#     discount = 0.8
#
#     def __init__(self, name, age, pay, discount):
#         self.name = name
#         self.age = age
#         self.pay = pay
#         self.discount = discount
#
#     @classmethod
#     def real_pay(self):
#         return round(self.pay * self.discount)
#
#     @staticmethod
#     def resting():
#         day = input("Weekday: ")
#
#         if day == "saturday" or day == "sunday":
#             return "You can rest today"
#         return "You can't rest today"
#
# st1 = Student("John", 20, 700, 0.7)
#
# # print(st1.real_pay())
# print(st1.resting())


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age
#
#     def display_info(self):
#         return f"Name: {self.name}, Age: {self._age}"
#
#     def _calculate_pay(self):
#         return 1000 if self._age >= 18 else 500
#
# class CollageStudent(Student):
#     def get_pay(self):
#         return self._calculate_pay()
#
# student = CollageStudent("John", 18)
#
#
# print(student.get_pay())
# print(student._calculate_pay())


# class Bankaccount:
#     def __init__(self, account_name, balance):
#         self.account_name = account_name
#         self.__balance = balance
# 
#     def deposit(self, amount):
#         self.__balance += amount
#         return self.__balance
#
#     def __apply_bank_fees(self):
#         self.__balance -= 50
#         return "Bank fees applied"
#
#
# account = Bankaccount("Bob", 1000)

#print(account.__balance)

# account.__balance = 500
#
# print(account.__balance)

# print(account.deposit(700))

# print(account.__apply_bank_fees())

# print(account._Bankaccount__apply_bank_fees())








