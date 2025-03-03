# import json
import json
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"Person({self.name}, {self.age})"

# def serialize_person(obj):
#     return {"name": obj.name, "age": obj.age}
#
# p = Person("John", 36)

# print(serialize_person(p))

# with open("person.json", "w") as f:
#     json.dump(p, f, default=serialize_person, indent=4)

# def deserialize(data):
#     return Person(data["name"], data["age"])
#
# with open("person.json") as f:
#     person = json.load(f, object_hook=deserialize)
#
# print(person)


import pickle

# fruits = ['Apple', 'Banana', 'Kiwi']
#
# serialized_fruits = pickle.dumps(fruits)
#
# print(serialized_fruits)

# print(type(serialized_fruits))

# deserialized_fruits = pickle.loads(serialized_fruits)
#
# print(deserialized_fruits)

# data = {
#     'name': 'John',
#     'age': 22,
#     'city': 'New York'
# }
#
# with open('data.pkl', 'wb') as binary_file:
#     pickle.dump(data, binary_file)

# with open("data.pkl", "rb") as f:
#     data = pickle.load(f)
#
# print(type(data))


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f'Person({self.name}, {self.age})'

# p = Person('John', 18)
#
# with open('person.pkl', 'wb') as f:
#     pickle.dump(p, f)

# with open('person.pkl', 'rb') as f:
#     data = pickle.load(f)
#
# print(data)


# import requests
#
# url = "https://jsonplaceholder.typicode.com/posts"
#
# response = requests.get(url)
#
# posts = response.json()
#
# for post in posts:
#     print(post)

# data = [
#     {
#         "userId": 1,
#         "name": "oto"
#     },
#     {
#         "userId": 2,
#         "name": "Beqa"
#     }
# ]
#
# response = requests.post(url, json=data)
#
# if response.status_code == 201:
#     print("Created")
# else:
#     print("Not Created")

# if response.status_code == 200:
#     posts = response.json()
#
#
# for post in posts:
#     print(post)