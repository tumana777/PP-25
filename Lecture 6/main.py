# names = ["John", "Mary", "Bob", "Alice"]
#
# ages = [23, 19, 22, 29]
#
# for i in range(len(names)):
#     print(names[i], "is", ages[i], "years old.")

# my_dict = {}

# print(type(my_dict))

# student_ages = {
#     "John": 23,
#     "Mary": 19,
#     "Bob": 22,
#     "Alice": 29
# }
#
# student = dict(name="John", age=23)
#
# print(student)
# print(student_ages)

# student = {
#     "name": "John",
#     "age": 23,
#     "profession": "software developer",
#     "is_active": True,
#     "scores": [80, 90, 100]
# }
#
# student["scores"][1] = 85
#
# for grade in student["scores"]:
#     print(grade)

# for elem in student:
#     print(elem)
#
# print()
#
# for elem in student:
#     print(student[elem])

# for elem in student:
#     print(elem, "->", student[elem])

# del student["scores"]

# print(student)

# student["age"] = 24

# student["last_name"] = "Smith"

# print(student)

# print(student["name"])
# print(student["age"])

# students = {
#     "John": 23,
#     "Mary": 19,
#     "Alice": 29,
#     "Bob": 22
# }

# test_dict = {i: i * 2 for i in range(1, 11) if i % 2 == 0}
#
# print(test_dict)

# student = {
#     "name": "John",
#     "age": 23,
#     "profession": "software developer",
#     "is_active": True,
#     "scores": [80, 90, 100]
# }

# print(student["Age"])

# print(student.get("age", "Key not found"))

# keys = list(student.keys())
# values = list(student.values())
#
# print(keys)
# print(values)

# for key, value in student.items():
#     print(key, "->", value)

# student = {
#     "name": "John",
#     "age": 23,
#     "profession": "software developer",
#     "is_active": True,
#     "scores": [80, 90, 100],
#     "city": "London"
# }

# student.update({"city": "New York"})

# student["age"] = 25

# student.setdefault("city", "New York")
#
# print(student)

# new_student = student.copy()
# student.clear()

# popped = student.pop("age")
#
# print(student)
# print(popped)
#
# new_popped = student.popitem()
# student.popitem()

# print(new_popped)
# print(student)

# fruits = ["apple", "orange", "banana", "cherry"]
#
# xatia = 5
#
# my_dict = dict.fromkeys(fruits, xatia)
#
# print(my_dict)