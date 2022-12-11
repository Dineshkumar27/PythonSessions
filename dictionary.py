#dictionary elements is a combination of key:value
#dictionary elements are enclosed with curly brackets

dict1={}#method 1
print(type(dict1))#empty dictionary
dict2=dict()#method 2
print(type(dict2))

dict1['name']='Kaavin'
dict1['std']=9
dict1['School']="Bethel"
dict1['Address']="Chennai"
dict1['zipcode']=600008
#
# print(dict1)
# #accessing dictionary elements using key
# #dictionaryname[keyname]
#
# # list1=[4,5,6]
# # print(list1[0])
#
# print(dict1['name'])
# print(dict1['std'])
#
person={
    'firstName':'John',
    'lastName':'Doe',
    'age':20,
    'address':{'street':'3rd st','doorno':3,'place':'Chennai'},
    'skills':['python','java','HTML','CSS']

        }
# print(person['firstName'])
# print(person['address']['place'])#Chennai
# print(person['address']['doorno'])
# print(person['skills'][0])
#
# #find length of the dictionary elements
#
# print('number of elements in person diction',len(person))
#
# #sometime key may throw error if its not found
#
# print(person['School'])#KeyError: 'School'
#
# #to avoid this error use get method
#
# print(person.get('school'))#if key not found it will give None
#
# print(person.get('lastName'))
#
# #add new element into dictionary
#
person['school']="Bethel"
# print(person.get('school'))

#
# #adding another skill into the skill list
#
person['skills'].append('C programming')
# print(person.get('skills'))
#
#
# #updating element in dictionary
#
person['age']=25
#
# print("after updating age",person)
#
# #dictionary will not allow duplicate key
#
# print('age' in person)#true
# print('weight' in person)#false
# #
#removing elements from the dictionary
#pop(key):remove the element of the specified key
#popitem():removes the last item
#del remove the element with specified key
# #
print("Before deleting school",person)
person.pop('school')
print("AFter deleting school",person)
person.popitem()
print("After popitem",person)
# #
del person['age']
print('After removing age',person)
# #
# # #item will convert list key:value pair into list of tuples[(firstname,john),(lastname,doe)]
# #
# # print(person.items())
# #
# # #to delete all element of dictionary
# #
# # # person.clear()
# # # print('After clear',person)
# #
# # # del person
# # # print(person)
# #
# # person2=person.copy()
# # print(person)
# # print(person2)
# #
# # #to get only keys
# #
# # print(person.keys())
# # #to get all values
# # print(person.values())
#
# #accessing dictionary using forloop
#
# # for key in person.keys():
# #     print(key,"-",person[key])
# #
# # for val in person.values():
# #     print(val)
#
# for key,value in person.items(): #[(k1,v1),(k2,v2),()]
#     print(key,value)