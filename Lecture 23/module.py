# def add(a, b):
#     return a + b
#
# def sub(a, b):
#     return a - b
#
# def mul(a, b):
#     return a * b
#
# def div(a, b):
#     if b == 0:
#         raise ValueError("Can not divide by zero")
#     return a / b
#
#
# def is_sorted(numbers):
#     return sorted(numbers)
#
# def is_even(number):
#     return number % 2 == 0

class Student:
    discount = 0.9

    pay = 2500

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@gmail.com"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def apply_discount(self):
        self.pay *= self.discount

    @classmethod
    def apply_pay(cls):
        print(cls.pay)

# student1 = Student("John", "Johnson", 2000)
#
# student1.apply_pay()

def is_palindrome(text):
    return text == text[::-1]

def is_upper(text):
    return text.title()

print("oto tumanishvili".title())