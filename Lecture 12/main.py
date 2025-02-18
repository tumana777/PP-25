import os

# file_path = 'test/satesto.txt'

# print(os.path.exists(file_path))

# if os.path.exists(file_path):
#     os.remove(file_path)
# else:
#     print("File doesn't exist")

# os.remove('test.txt')

# print(os.getcwd())

# os.mkdir('test1')

# os.rmdir('test1')

# os.rmdir('test')

# print(os.path.isfile('test/main.txt'))

# import shutil
#
# shutil.rmtree('test')

# txt = b"Hello World!"
#
# name = "ოთარ"

# encoded_txt = txt.encode()

# encoded_name = name.encode('utf-8')

# print(type(encoded_name))

# with open('test.txt', 'w') as file:
#     file.write(txt)

# with open('test.bin', 'wb') as f:
#     f.write(encoded_name)

# with open('test.bin', 'rb') as f:
#     data = f.read()
#
#     print(data)

# with open('test.png', 'rb') as f:
#     data = f.read()

    # print(len(data))

# with open('copy.png', 'wb') as file:
#     file.write(data)


import csv

# with open('students.csv', 'r', newline='') as csvfile:

    # headers = csvfile.readline()

    # data = csv.reader(csvfile)

    # print(next(data))
    # print(next(data))
    # print(next(data))

    # print(headers)

    # reader = csv.reader(csvfile)
    #
    # for row in reader:
    #     print(row)


# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# new_lst = iter(lst)
#
# print(next(new_lst))
# print(next(new_lst))
# print(next(new_lst))
# print(next(new_lst))
# print(next(new_lst))
# print(next(new_lst))
# print(next(new_lst))
# print(next(new_lst))
# print(next(new_lst))
# print(next(new_lst))

# headers = ['name', 'last_name', 'age']
#
# data = [
#     ['Bob', 'Walker', 25],
#     ['Walter', 'White', 30],
#     ['Soul', 'Goodman', 30]
# ]
#
# with open('data.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(headers)
#     writer.writerows(data)


# with open('companies.csv') as csvfile, open('tech_companies.csv', 'w', newline='') as csvfile2:
#     reader = csv.DictReader(csvfile)

    # for company in reader:
    #     print(company)
    #
    # headers = reader.fieldnames

    # headers = ['Company ID','Company Name','Industry','Employees','Company Price (in billions)']

    # data = []
    #
    # for row in reader:
    #     if row['Industry'] == 'Technology':
    #         data.append(row)

    # data = [company for company in reader if company['Industry'] == 'Technology']
    #
    # writer = csv.DictWriter(csvfile2, fieldnames=headers)
    # writer.writeheader()
    # writer.writerows(data)


from faker import Faker

fake = Faker()

# print(fake.first_name(), fake.last_name(), fake.city(), fake.email(), sep=',')

persons = []

for i in range(10):
    persons.append({'name': fake.name(),
                    'email': fake.email(),
                    'city': fake.city()
                    })

for person in persons:
    print(person)

person = {
    'ID': 1,
    'name': "test",
    'email': "test@gmai.com",
    'age': 20 - 60
}