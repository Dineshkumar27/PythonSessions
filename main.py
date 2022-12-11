# import mymodule
# print(mymodule.generate_fullName("Kaavin","Vinod"))
#
# mymodule.add(4,5)

#importing a function from mymodule
#
# from mymodule import add
# add(4,6)
#
# #Importing and renaming a module
# from mymodule import generate_fullName as fullname
# print(fullname("Python","Kaavin"))
#
# from math import sqrt,sin #built in module(someone has defined for us)
# print(sqrt(9))
# print(sin(90))
# print(pow(2,3))

#OS Module
#is used to perform some operating systems tasks
#used for creating,changing current directory(folder), fetching its contsnts, chanding and identifying the current folder
#
# import os
# #creating a folder
# # os.mkdir('Kaavin')
# #changing the current directory
# # os.chdir("path")
# #to know the current directory
# print(os.getcwd())
# os.rmdir('Kaavin')


#Sys module provided functions and variable used to manipulate
#different part of runtime environment
# 0th element is filename(name of the script)

import sys
print('Welcome {}. enjoy{} Challenge'.
      format(sys.argv[1],sys.argv[2]))
print("file name is {}".format(sys.argv[0]))

#statistics module
#used to find mean median mode

# from statistics import * #* means import all functions
# ages=[20,20,2,24,25,22,26,23]
# print(mean(ages))
# print(median(ages))
# print(stdev(ages))
# print(mode(ages))

# import math
# print(math.pi)
# print(math.sqrt(9))
# print(math.floor(89.787))
# print(math.ceil(89.789))
# print(math.pow(2,3))


# import random
#
# print(random.randint(1000,9999))
# print(random.random())
# print(random.choice([55,77,34,21,90,87]))
#
import string
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
#
# pwd=str()
# for i in range(8):
#     pwd=pwd+random.choice(string.ascii_letters+string.digits)
#
# print(pwd)


