# char = "A"
# char = "a"
# char = "მ"

# print(ord(char))

# name = "Otar"
# print(len(name))

# text = input("Enter text: ")
# text.upper()
#
# text1 = text.upper()
#
#
# print(text)
# print(text1)
# print(text.capitalize())
# print(text.lower())
# print(text.title())

# name = "Otar Tumanishvili"

# print(len(name))
# print(name[3])
# print(name[:3])
# print(name[1:6])
#
# sliced = name[3:6]
# print(sliced)

# print(name[::-1])

# print(name[16])
# print(name[-1])
# print(name[-4])

# word = input("Enter text: ").strip().lower()
# word = word.lower()
# word = word.strip()

# word1 = word[::-1]
#
# if word == word1:
#     print("It is palindrome")
# else:
#     print("It is not palindrome")

# text = input("Enter text: ")
# print(text)
#
# text = text.replace(" ", "_")
# print(text)

# vowels = 'aeiou'
#
# word = input("Enter word: ")
#
# count = 0
#
# for c in word:
#     if c in vowels:
#         count += 1
#
# print(count)

# text = input("Enter text: ").lower()
#
# print(text.count("a"))

# text = input("Enter text: ")
#
# print(text.index("qa"))

# text = input("Enter text: ")
#
# splitted_text = text.split()
# splitted_text1 = text.split("#")
#
# print(splitted_text)
# print(splitted_text1)

# text.isdigit()
# text.isalpha()

# text.startswith("pyth")
# text.endswith("on")

# str1 = "otar"
# print(len(str1))
# print(type(str1))
#
# utf_encoded_str = str1.encode("utf-8")
# print(utf_encoded_str)
# print(type(utf_encoded_str))
# print(len(utf_encoded_str))

# name_ka = "ოთარ"
# print(len(name_ka))
#
# encoded_name_ka = name_ka.encode("utf-8")
# print(encoded_name_ka)
# print(len(encoded_name_ka))
#
# print(encoded_name_ka.decode("utf-8"))

# binary_name = b"Otar"
# print(type(binary_name))

import string
import random

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

# password_length = 20
# password = ''

# print(random.choice(string.ascii_letters + string.digits + string.punctuation))

# for _ in range(password_length):
#     password += random.choice(string.ascii_letters + string.digits)
#
# print(password)

import re

# text = "He my name is Otar and I am 25 years old"
#
# pattern = r"He.?o"
#
# if re.match(pattern, text):
#     print("It is a match")
# else:
#     print("It is not a match")

# email = input("Enter email: ")
#
# pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]{2,}$"
#
# if re.match(pattern, email):
#     print("It is a valid email")
# else:
#     print("It is not a valid email")