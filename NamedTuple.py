# Python code to demonstrate namedtuple()

# from collections import namedtuple
#
# # Declaring namedtuple()
# Student = namedtuple('Student', ['name', 'age', 'DOB'])
#
# # Adding values
# S = Student('Nandini', '19', '2541997')
#
# # Access using index
# print("The Student age using index is : ", end="")
# print(S[1])
#
# # Access using name
# print("The Student name using keyname is : ", end="")
# print(S.name)


# Python code to demonstrate namedtuple() and
# # Access by name, index and getattr()
# #
# # # importing "collections" for namedtuple()
# import collections
#
# # Declaring namedtuple()
# Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])
#
# # Adding values
# S = Student('Nandini', '19', '2541997')
#
# # Access using index
# print("The Student age using index is : ", end="")
# print(S[1])
#
# # Access using name
# print("The Student name using keyname is : ", end="")
# print(S.name)
#
# # Access using getattr()
# print("The Student DOB using getattr() is : ", end="")
# print(getattr(S, 'DOB'))


# Python code to demonstrate namedtuple() and
# _make(), _asdict() and "**" operator

# importing "collections" for namedtuple()
# import collections
#
# # Declaring namedtuple()
# Student = collections.namedtuple('Student',
# 								['name', 'age', 'DOB'])
#
# # Adding values
# S = Student('Nandini', '19', '2541997')
#
# # initializing iterable
# li = ['Manjeet', '19', '411997']
#
# # initializing dict
# di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}
#
# # using _make() to return namedtuple()
# print("The namedtuple instance using iterable is : ")
# print(Student._make(li))
#
# # using _asdict() to return an OrderedDict()
# print("The OrderedDict instance using namedtuple is : ")
# print(S._asdict())
#
# # using ** operator to return namedtuple from dictionary
# print("The namedtuple instance from dict is : ")
# print(Student(**di))
