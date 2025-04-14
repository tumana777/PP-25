from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
# print(client.list_database_names())

db = client["PP-25"]

students = db["students"]

# print(students.find_one())

# for student in students.find():
#     print(student)

# for student in students.find():
#     print(student.get("first_name", "default"))

# student = {
#     "name": "Levan",
#     "age": 23
# }
#
# students.insert_one(student)

# student_list = [
#     {
#         "name": "Nikoloz",
#         "age": 32
#     },
#     {
#         "name": "Anano",
#         "age": 33
#     },
#     {
#         "name": "Alex",
#         "age": 23
#     }
# ]
#
# students.insert_many(student_list)

# students1 = students.find({"age": 23})
#
# for student in students1:
#     print(student)


# s1 = students.find({"age": {"$lt": 26}})
#
# for st in s1:
#     print(st)


# s1 = students.find({"age": {"$lte": 26}})
#
# for st in s1:
#     print(st)


# s1 = students.find({"age": {"$gt": 23, "$lt": 26}})
#
# for st in s1:
#     print(st)


# s1 = students.find({"$or": [{"name": "Anano"}, {"name": "Levan"}]})
#
# for st in s1:
#     print(st)


# s1 = students.find({"$and": [{"name": "Anano"}, {"age": 33}]})
#
# for st in s1:
#     print(st)


# s1 = students.find({"name": "Anano", "age": 33})
#
# for st in s1:
#     print(st)


# students.update_one({"first_name": "Davit"}, {"$set": {"age": 27}})

# students.update_many({"age": {"$gte": 23, "$lte": 28}}, {"$set": {"age": 20}})



# students.delete_one({"name": "Anano"})

# students.delete_many({"age": 20})

students.delete_many({})