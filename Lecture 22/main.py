# Single Responsibility Principle

# Bad Example

# class Report:
#     def __init__(self, data):
#         self.data = data
#
#     def generate_report(self):
#         return f"Report Data: {self.data}"
#
#     def save_report(self, filename):
#         with open(filename, "w") as file:
#             file.write(self.generate_report())

## Good Example

# class Report:
#     def __init__(self, data):
#         self.data = data
#
#     def generate_report(self):
#         return f"Report Data: {self.data}"
#
# class ReportSaver:
#     @staticmethod
#     def save_to_file(report: Report, filename):
#         with open(filename, "w") as file:
#             file.write(report.generate_report())

# Open/Close Principle
## Bad Example

# class Discount:
#     def __init__(self, price):
#         self.price = price
#
#     def get_discount_price(self, discount_type):
#         if discount_type == 'seasonal':
#             return self.price * 0.9
#         elif discount_type == 'seasonal2':
#             return self.price * 0.8
#         else:
#             return self.price

## Good Example

# from abc import ABC, abstractmethod
#
# class Discount(ABC):
#     def __init__(self, price):
#         self.price = price
#
#     @abstractmethod
#     def get_discount(self):
#         pass
#
# class SeasonalDiscount(Discount):
#     def get_discount(self):
#         return self.price * 0.9
#
# class Seasonal2Discount(Discount):
#     def get_discount(self):
#         return self.price * 0.8


# Liskov Substitution Principle
## Bad Example

# class Bird:
#     def fly(self):
#         print("I can fly")
#
# class Penguin(Bird):
#     def fly(self):
#         print("I can't fly")

# Good Example

# class Bird:
#     def move(self):
#         return "I can move"
#
# class FlyingBird(Bird):
#     def fly(self):
#         print("I can fly")
#
# class Penguin(Bird):
#     def swim(self):
#         print("I can swim")


# Interface Segregation Principle
# Bad Example

# class Worker:
#     def work(self):
#         pass
#
#     def eat(self):
#         pass
#
# class Developer(Worker):
#     def work(self):
#         print("I can Work")
#
#     def eat(self):
#         print("I can Eat")
#
#
# class Robot(Worker):
#     def work(self):
#         print("I can Work")
#
#     def eat(self):
#         print("I can't Eat")

# Good Example

# from abc import ABC, abstractmethod
#
# class Workable(ABC):
#     @abstractmethod
#     def work(self):
#         pass
#
# class Eatable(ABC):
#     @abstractmethod
#     def eat(self):
#         pass
#
# class Developer(Workable, Eatable):
#     def work(self):
#         print("I can work")
#
#     def eat(self):
#         print("I can eat")
#
# class Robot(Workable):
#     def work(self):
#         print("I can work")

# Dependency Inversion Principle
# Bad example

# class MySQLDatabase:
#     def connect(self):
#         return "Connected to MySQL"
#
# class Application:
#     def __init__(self):
#         self.database = MySQLDatabase()
#
#     def get_connection(self):
#         return self.database.connect()

# Good Example

# from abc import ABC, abstractmethod
#
# class Database(ABC):
#     @abstractmethod
#     def connect(self):
#         pass
#
# class MySQLDatabase(Database):
#     def connect(self):
#         return "Connected to MySQL"
#
# class PostgreSQLDatabase(Database):
#     def connect(self):
#         return "Connected to PostgreSQL"
#
# class Application:
#     def __init__(self, database: Database):
#         self.database = database
#
#     def get_connection(self):
#         return self.database.connect()
#
# mysql_app = Application(MySQLDatabase())
#
# postgres_app = Application(PostgreSQLDatabase())
#
# print(mysql_app.get_connection())
# print(postgres_app.get_connection())








