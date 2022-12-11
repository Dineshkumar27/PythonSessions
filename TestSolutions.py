# 1. Write a Python program to get the largest number from a list

# lst=[23,567,908]
# print(max(lst))

#2. concatenate two dicts
# dict1={'a':1,'b':2}
# dict2={'c':3,'d':4}
# dict3={}
# dict3.update(dict1)
# dict3.update((dict2))
# print(dict3)


# Given the list [a,b,a,b,f,d,f,d,s,d,e,r,d]
# expected result:{a:2,b:2,d:3,f:2,s:1,e:1,r:1}
# list1=['a','b','a','b','f','d','f','d','s','d','e','r','d']
# dict1={}
# for letter in list1:
#     dict1[letter]=list1.count(letter)#a:2
#
# print(dict1)

# write a program to print the names ending with vowels ['Raja','Ragu','Anil','Kamni','Kavin','Vinith']
# names=['Raja', 'Ragu', 'Anil', 'Kamni', 'Kavin', 'Vinith']
# vowels='aeiou'
# for name in names:
#     if(name[-1] in vowels):
#         print(name)
# Write a program to generate numbers from 110 to 130 and convert into list

# lst=list(range(110,131))
# print(lst)


# Write a Python program to find the repeated items of a tuple
# tup=('a','b','a','b','f','d','f','d','s','d','e','r','d')
# duplicate=[]
# for i in tup:
#     if (tup.count(i) > 1):
#         duplicate.append(i) if (i not in duplicate) else 'Hello'
# print(duplicate)

# [(1,2),(3,5),(9,0),(45,67)] expected output should be [0,1,2,3,5,9,45,67]
# mylst=[(1,2),(3,5),(9,0),(45,67)]
# flattenedlist=[i for lst in mylst for i in lst]
# print(flattenedlist)

# Write a program to find the given day is weekday or weekend
import random

# weekdays=['MOnday','Tuesday','Wed']
# # weekends=['Saturday','Sunday']
# day=input('Enter a day')
# print("Weekdays")if(day in weekdays) else print("Weekends")

# Write a program to remove the duplicates from the given list [a,b,a,b,f,d,f,d,s,d,e,r,d]

lst=['a','b','a','b','f','d','f','d','s','d','e','r','d']
unique=[]
for letter in lst:
    if letter not in unique:
        unique.append(letter)
print(unique)


# Write a program find get how many emails from fita domain. [xyz@gmail.com, mnp@yahoo.com, knkkjk@fita.com,nhmkk@fita.com, juiuyh@fita.com,cvbvbn@gmail.com]
emails=['xyz@gmail.com', 'mnp@yahoo.com', 'knkkjk@fita.com','nhmkk@fita.com', 'juiuyh@fita.com','cvbvbn@gmail.com']
gmails=[email for email in emails if 'gmail' in email]
print(gmails)