#import maths#ModuleNotFoundError: No module named 'maths'
import math
# print(math.PI)#AttributeError: module 'math' has no attribute 'PI'
print ('Helloworld')
age=10
print(age)#NameError: name 'age' is not defined

nums=[4,5,6,7]
# print(nums[10])#IndexError: list index out of range

person={
    'firstName':'John',
    'lastName':'Doe',
    'age':20,
    'address':{'street':'3rd st','doorno':3,'place':'Chennai'},
    'skills':['python','java','HTML','CSS']
        }

# print(person['Weight'])#KeyError: 'Weight'

# 4+'3'#TypeError: unsupported operand type(s) for +: 'int' and 'str'

# from math import power#ImportError: cannot import name 'power' from 'math' (unknown location)

# int('3a')#ValueError: invalid literal for int() with base 10: '3a'

100/0#ZeroDivisionError: division by zero