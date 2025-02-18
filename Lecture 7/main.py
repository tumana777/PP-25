# my_tuple = ()
#
# print(type(my_tuple))

# my_tuple = (1, 2, 3)
#
# print(my_tuple[0])

# test = ("Hello")
#
# test1 = ("Hello", )
#
# print(type(test))
# print(type(test1))

# my_tuple = 1, 2, 3, [23]

# print(type(my_tuple))

# for item in my_tuple:
#     print(item)

# my_tuple = (3, True, "Hello", [4, 3, 5], "Hi", (2, 4))

# print(my_tuple[1:4])

# my_tuple[3][0] = 6
# print(my_tuple)

# my_tuple[5][1] = 3
# print(my_tuple)

# my_tuple = (1, 2, 3)
# my_tuple1 = (3, True, "Hello", [4, 3, 5], "Hi", (2, 4))

# lst = list(my_tuple1)
#
# lst.remove([4, 3, 5])
#
# my_tuple1 = tuple(lst)

# print(my_tuple1)
#
# my_dict = {
#     my_tuple: "Test",
#     my_tuple1: "Satesto",
# }
#
# print(my_dict)

# my_tuple = (1, 2, 4, 5)
#
# n1, n2, *n3, n4 = my_tuple
#
# print(n1, n2, n3, n4, sep='\n')

# my_dict = {
#     "name": "Otar",
#     "age": 18,
#     "City": "Telavi"
# }
#
# for key, value in my_dict.items():
#     print(key, value)

# my_tuple = (1, 2, 3, 4, 5)

# my_tuple1 = (6, 7, 8, 9)

# print(my_tuple + my_tuple1)

# print(my_tuple * 3)

# print(my_tuple.count(3))

# print(my_tuple.index(5))

# my_set1 = set()

# my_set = {1, 2, 3, 2}
# my_set1 = {2, 3, 4}


# print(my_set)

# for x in my_set:
#     print(x)

# lst = [2, 4, "Hello", 3, 5]
#
# lst_to_set = set(lst)
#
# lst_to_set.add(0)
# lst_to_set.remove(0)
#
# # lst_to_set.clear()
#
# # lst_to_set.update([0, 3])
#
# print(lst_to_set)

# my_set = {1, 2, 3, 2}
# my_set1 = {2, 3, 4}

# print(my_set + my_set1) returns error

# print(my_set.union(my_set1))
# print(my_set | my_set1)

# print(my_set.intersection(my_set1))
# print(my_set & my_set1)

# print(my_set.difference(my_set1))
# print(my_set - my_set1)

# print(my_set1.difference(my_set))
# print(my_set1 - my_set)

# print(my_set.symmetric_difference(my_set1))
# print(my_set ^ my_set1)

# my_set = {1, 2, 3}

# my_frozenset = frozenset(my_set)
#
# my_dict = {
#     my_frozenset: "Test"
# }
#
# print(my_dict)

# my_set1 = {1, 2, 3, [2]}
#
# print(my_set1)

# lst = [True, False, [1, 2]]
#
# my_set = set(lst)