#String is a collection of characters
#String is immutable(unchangeable)
#String are wrapped into single quotes, double quotes and triple quotes

# string1='Kaavin'
# print(string1)
# # string1[0]='A'#throws error string is immutable
# print(string1[-1])#print last letter
# print(string1)
#
#
# "This is string in python"
# '''this is string in python
# lhellosdf
# sdfsdfs
# f'''
# multilineString="""this is string in python
#                     good morning
#                     happy sunday
#                     how are you?"""
#
# print(multilineString)
#
# string2='Python is easy Language'
# print(len(string2))
#
# string3='kaavin\'s laptop'
# print(string3)
# #
# print(string3 *2)
# #
# print(string1+' '+string3)
#
# #to check o in kaaving
# print('o' in "kaavin")#false
# #
# print('a' in "kaavin")#True
# #
# print('o' not in "kaavin")#true
#
# #string slicing
#
myData="Welcome to Python Programming"
#
# print(myData[:])#print full string
# print(myData[3:])#3rd letter to last letter(come to lastletter)
# print(myData[3:6])#print 3rd index to 6-1 index(com)
# print(myData[3:7])#print 3rd index to 7-1 index(come)
# print(myData[:7])#print 0th index to 7-1 index(Welcome)
# print("double slicing", myData[::1])
# print("double slicing", myData[0:8:1])#[startIndex:endIndex:step]
# print("double slicing", myData[8:0:-1])#[startIndex:endIndex:step]


friends=['Raja','Ragu','Mani','Rivakar','John']
# for friend in friends:
#     if(friend.startswith('R')):
#         print(friend)
# print("Ends with n")
# for friend in friends:
#     if(friend.endswith('n')):
#         print(friend)
# print(friends[0].upper())
# print(friends[0].lower())
# print(len('  hello   '.strip()))
# print(len('  hello   '.lstrip()))
# print(len('  hello   '.rstrip()))
# print('hello good morning'.capitalize())#make first letter caps
# print('hello good morning'.title())#make all word's first letter into caps
# print('hello good morning'.count('o'))#gives number of 'o'
print('hello good morning'.find('g'))#search the letter g in the full text
#search the letter g from 1 to 10 index
print('hello good morning'.find('n',1,10))
# # if g not  found returns -1
# print('I am {0} studying {1}strd'.format('kaavin',9))#I am kaavin studying 9strd
# print('hello good morning'.index("good"))#6 if word is not present it will throw error
# words=('Hello', 'good','morning')
# joinedwor='*'.join(words)
# print(joinedwor)
#
# age="32"
# print(age.isdigit())#to check the age is number or not
# emailid="kaaving.321"
# print(emailid.isalnum())#to check string is having alphabet and number
# print('hello'.islower())
# print('HELLO'.isupper())






