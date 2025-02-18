# a = 5
# a = a + 1
# b = a
# a += 1
# print(a, b)

# a = 4
# a *= 2
# print(a)
#
# a -= 1
# a /= 2
# a //= 5
# a %= 4
# a **= 3

# a = 5
# b = 7
# c = 9
# d = 12
#
# print(a < b and c > d)
# print(a < b or c > d)

# print(False or False)
# print(True or False)
# print(False or True)
# print(True or True)

# print(False and False)
# print(True and False)
# print(False and True)
# print(True and True and True and False)

# print(not True)

# print(not(True and True))

# print(True or (False and False))

# a = 1000
# b = 1000

# print(id(a))
# print(id(b))

# print(a == b)
# print(a is b)

# x = [4, 6]
# y = x
# z = [4, 6]
#
# print(id(x))
# print(id(y))
# print(id(z))
#
# print(x is z)
# print(x == z)

# full_name = "Otar Tumanishvili"
#
# char = input("Enter character: ")

# print(char in full_name)
# print(char not in full_name)

# number = 5689
#
# print(5 in number)
#
# a = 5
# b = 6
#
# if a < b:
#     print("a is greater than b")
#
# print("Done")

# a, b, c = 5, 6, 7

# username = input("Enter username: ")
# email = input("Enter email: ")
# password = input("Enter password: ")
#
# if username == "admin" or email == "example@email.com" and password == "admin123":
#     print("Welcome admin")

# grade = int(input("Enter your grade: "))
#
# if grade > 100 or grade < 0:
#     print("Invalid grade")
# elif grade >= 91:
#     print("A")
# elif grade >= 81:
#     print("B")
# elif grade >= 71:
#     print("C")
# elif grade >= 61:
#     print("D")
# elif grade >= 51:
#     print("E")
# elif grade >= 0:
#     print("F")

# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == "admin" and password == "admin123":
#     print("You are logged in")
# else:
#     print("Invalid username or password")

# username = input("Enter username: ")
#
# if username == "admin":
#     password = input("Enter password: ")
#     if password == "admin123":
#         two_factor_auth = input("Enter two factor authentication code: ")
#         if two_factor_auth == "123456":
#             print("You are logged in")
#         else:
#             print("Wrong two factor authentication code")
#     else:
#         print("Wrong password")
# else:
#     print("Wrong username")

# day = input("Enter day: ")

# match day:
#     case "Monday":
#         print("Go to school")
#     case "Tuesday":
#         print("Go to work")
#     case "Wednesday":
#         print("Go to gym")
#     case "Thursday":
#         print("Go to dinner")
#     case "Friday":
#         print("Go to sleep")
#     case _:
#         print("Weekend")

# match day:
#     case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#         print("It's weekday")
#     case "Saturday" | "Sunday":
#         print("It's weekend")
#     case _:
#         print("Invalid day")

# is_power = 1
#
# if is_power:
#     print("Power is on")
# else:
#     print("Power is off")