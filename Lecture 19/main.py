# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# lst1 = [str(num) for num in nums]
#
# serialized_nums = ','.join(lst1)
import json


# print(type(serialized_nums))

# with open("nums.txt", "w") as f:
#     f.write(serialized_nums)

# with open("nums.txt", "r") as f:
#     data = f.read()

# print(type(data))

# lst = data.split(",")
#
# serialized_data = [int(num) for num in lst]
#
# print(serialized_data)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f'Person({self.name}, {self.age})'
#
# p = Person('John', 18)
#
# serialized_person = f"name={p.name}, age={p.age}"
# print(serialized_person)

# def deserialize_person(person):
#     data = person.split(',')
#     name = data[0].split('=')[1]
#     age = data[1].split('=')[1]
#     return Person(name, int(age))
#
# print(deserialize_person(serialized_person))


import json

# student = {
#     "first_name": "John",
#     "last_name": "Smith",
#     "age": 19,
#     "gender": "male",
#     "grades": [51, 65, 87],
#     "lecturer": {
#         "name": "Marta",
#         "email": "test.example.com",
#     },
#     "test": (1, 7)
# }
#
# student1 = {
#     "first_name": "Bob",
#     "last_name": "White",
#     "age": 19,
#     "gender": "male",
#     "grades": [51, 54, 87],
#     "lecturer": {
#         "name": "Marta",
#         "email": "test.example.com",
#     },
#     "test": (1, 7)
# }

# student_list = [student, student1]

# serialized_student = json.dumps(student, indent=4)
#
# deserialized_student = json.loads(serialized_student)
#
# print(deserialized_student)

# with open("student.json", "w") as file:
#     json.dump(student_list, file, indent=4)

# with open("student.json", "r") as student_file:
#     data = json.load(student_file)
#
# print(data)






















