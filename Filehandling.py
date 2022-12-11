#file handling is an important part of programming which allows us to create, update,read,delete
# Modes in file
#r-> read
#w->write
#a->append
#x-creates a file and return error if file exist
#t-> text mode
#b->binary mode

# f=open("file1.txt",'r')
# data=f.read()
# print(type(data))
# print(data)
# f.close()


#read first 5 letters
# f=open("file1.txt")
# data=f.read(5)#read 5 letters
# print(type(data))
# print(data)
# f.close()

#readline()

# f=open("file1.txt")
# data=f.readline()#read 1st line
# print(type(data))
# print(data)
# f.close()

#get all lines in the form of list
# f=open("file1.txt")
# data=f.read().splitlines()#read 1st line
# print(type(data))
# print(data)
# print(len(data))
# f.close()
# for line in data:
#         print(line)


# f=open("file1.txt")
# data=f.read().splitlines()#read 1st line
# print(type(data))
# print(data)
# print(len(data))
# print(f.closed)
# f.close()
# print(f.closed)


# using with-> this will easily close the file once the work is done

# with open("file1.txt","r") as f:
#     data=f.read()
#     print(data)
#     print(f.closed)
# print(f.closed)
#create a file and update a file

#write() to create a file, if file already exist it will overwrite the file, if not exist
# it will create
# with open("file1.txt","w") as f:
#     f.write("This is a new content in file1.txt")
#
# print(f.closed)
# #
# with open("file2.txt","w") as f:
#     f.write("This is a new content in file2.txt")
#
# print(f.closed)

# with open("file1.txt","a") as f:
#     f.write("This is an appended content in file1.txt")
#
# print(f.closed)

# import os
# os.remove('C:\\Users\\Admin\\PycharmProjects\\kavinproject\\file2.txt')

#ensure the file exist before using os.remove()

# import os
# if(os.path.exists("C:\\Users\\Admin\\PycharmProjects\\kavinproject\\file1.txt")):
#     os.remove("C:\\Users\\Admin\\PycharmProjects\\kavinproject\\file1.txt")
# else:
#     print("file not found")


#converting json into dictionary
# import json
#
# person_json='''
# {"firstName":"John",
#         "lastName":"Fernandas",
#         "age":23,"Country":"USA",
#         "skills":["Python","HTML","C"]
#     }
#         '''
# print(type(person_json))#string
# person_dict=json.loads(person_json)#convert json to dictionary
# print(type(person_dict))
# print(person_dict.get('firstName'))
# import json
# #convert dictionary into json
# person={'firstName':'John',
#         'lastName':'Fernandas',
#         'age':23,'Country':'USA',
#         'isMarried':True,
#         'skills':['Python','HTML','C'],
#         'address':{'stree':'3rd','city':'New Jersy','zip':7979879}
#         }
# per_json=json.dumps(person)#convert dictionary into json
# print(per_json)
# print(type(per_json))


# #writing into json
# import json
# person={'firstName':'John',
#         'lastName':'Fernandas',
#         'age':23,'Country':'USA',
#         'isMarried':True,
#         'skills':['Python','HTML','C'],
#         'address':{'stree':'3rd','city':'New Jersy','zip':7979879}
#         }
# with open("myjsonfile.json",'w',encoding='utf-8') as f:
#     json.dump(person,f,ensure_ascii=False, indent=4)



lst=[66,67,68]
myarray=bytearray(lst)
with open("myfile","wb") as f:
    f.write(myarray)
