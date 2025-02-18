# nums = [1, 2, 3, 4, 5]
#
# # print(len(nums))
# #
# print(type(nums[2]))
# print(nums[2])
# # print(nums[4])
# # print(nums[5])
#
#
# nums[2] = "6"
#
# print(nums[2])
# print(type(nums[2]))

# fruits = ["apple", "orange", "banana", "cherry"]

# user_fruit = input("Enter your favorite fruit: ")

# fruits.append(user_fruit)

# fruits.clear()

# fruits1 = fruits.copy()

# fruits.append("grape")

# fruits2 = fruits
#
# fruits3 = ["apple", "orange", "banana", "cherry"]
#
# print(fruits)
# print(fruits1)
# print(fruits2)
#
# print(fruits == fruits1)
# print(fruits == fruits2)
# print(fruits == fruits3)

# print()
#
# print(fruits is fruits1)
# print(fruits is fruits2)
#
# print(id(fruits))
# print(id(fruits1))
# print(id(fruits2))

# fruits = ["apple", "orange", "banana", "cherry", "apple"]

# fruits2 = ["grape", "kiwi"]

# print(fruits.count("applse"))
# print(fruits.count("apple"))
# print(fruits.count("cherry"))

# concatenated_fruits = fruits + fruits2
#
# fruits.extend(fruits2)
#
# print(fruits)
# print(concatenated_fruits)

# fruits_multipled = fruits * 2
#
# print(fruits_multipled)

# fruits = ["apple", "orange", "banana", "apple", "cherry"]

# print(fruits.index("apple"))

# fruits.insert(2, "kiwi")

# fruits[2] = "kiwi"

# fruits.pop()
# popped = fruits.pop()

# popped = fruits.pop(2)

# print(popped)

# print(fruits[-1])

# fruits.remove("apple")

# fruits.reverse()

# print(fruits[::-1])

# print(fruits)

# fruits = ["apple", "orange", "san", "banana", "kiwi", "apple", "cherry"]
#
# fruits.sort(key=len, reverse=True)

# print(fruits)

# nums = [3, 6, 2, 1, 9]
#
# nums.sort(reverse=True)

# print(nums)

# txt = input("Enter your text: ")
#
# word1 = input("Enter your word: ")
#
# word2 = input("Enter your word: ")
#
# txt = txt.replace(word1, word2)
#
# print(txt)

# fruits = ["apple", "orange", "san", "banana", "kiwi", "apple", "cherry"]

# for fruit in fruits:
#     print(fruit)

# for i in range(len(fruits)):
#     print(f"{i} - {fruits[i]}")

# for items in enumerate(fruits):
#     print(items)

# for i, element in enumerate(fruits):
#     print(f"{i} - {element}")

# nums = []
#
# for i in range(10):
#     nums.append(i)
#
# print(nums)

# fruits = ["apple", "orange", "san", "banana", "kiwi", "apple", "cherry"]

# long_fruits = []
#
# for fruit in fruits:
#     if len(fruit) > 5:
#         long_fruits.append(fruit)
#
# print(long_fruits)
#
# long_fruits = [fruit for fruit in fruits if len(fruit) > 5]
#
# long_fruits_upper = [fruit.upper() for fruit in fruits if len(fruit) > 5]
#
# print(long_fruits)
# print(long_fruits_upper)

# nums = [num ** 2 for num in range(1, 11)]
#
# print(nums)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix[1][1])

# for row in matrix:
#     for elem in row:
#         print(elem)

# for row in matrix:
#     for elem in row:
#         print(elem, end=" ")
#     print()