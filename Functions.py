#Function is a reusable block(write once and call manytimes)
#code size will be reduced
#reusability

#function must be defined first using def keyword
#after defining a function call the function

# def function_name():#defining a function
#     statements
#     statements
# function_name()#calling a function


# def printKavin():#no parameter
#     print('Kavin')
# printKavin()
# printKavin()
# printKavin()
#
# def sayGoodMorning(name):#function with one Parameter
#     print("Good Morning", name);#Good Morning Kavin
# #
# sayGoodMorning("Kavin")
# sayGoodMorning("Dinesh")
#
# def joinName(firstName,lastName):#non returning function
#     print(firstName+" "+lastName)
# joinName("Ranjith","Kumar")
#
#
# #parameters can be string, boolean, int, float, list, tubple,dictionary , set
#
# #function returns a value
#
# def joinName(firstName,lastName):#non returning function
#     return firstName+" "+lastName
# #
# joinedName=joinName("Ranjith","Kumar")
# print(joinedName)
#
#
# def squ(num):
#     return num*num
# #
# sq_answer=squ(8)
# print(sq_answer)
#
# #bill amount 100 apply 5% tax
# def calculateTax(billamount,taxpercentage):
#     print("Bill amount",billamount)
#     print("tax",taxpercentage)
#     total=billamount+((taxpercentage/100)*billamount)
#     return total
# #
# billWithTax=calculateTax(100,5)
# print("Total bill with tax",billWithTax)
#
#
# def areaOfCircle(radius):
#     PI=3.14
#     area=PI*radius*radius
#     return area
#
# print(areaOfCircle(5))

# def calculateAge(birthyear,currentyear=2022):
#       print("BirthYear",birthyear)
#       print("Current Year",currentyear)
#       return currentyear-birthyear
# print(calculateAge(2008,2028))
# print(calculateAge(2008))

#default value, if value for the parameter is not passed while calling a function,
#then default value will be taken
# def calculateAge(birthyear,currentyear=2022):#2022 is default value
#     return currentyear-birthyear
# print(calculateAge(2008,2024))

#Error condition in default
# def calculateAge(birthyear=2008,currentyear=2009):#2022 and 2008 is default value
#     return currentyear-birthyear
# print(calculateAge())

# #defining a function with key and value(order can be changed)
#
# def calculateAge(birthyear,currentyear):#2022 and 2008 is default value
#     return currentyear-birthyear
# print(calculateAge(currentyear=2022,birthyear=2008))#paramater is the key and value is the value of the parameter

#scope
b=11#globl
def hello(a):#local variable
    print(a)
    print(b)
hello(10)
print(b)

#global variable cannot be update inside a function

# b=11#globl
# def hello(a):#local variable
#     global b
#     b=b+8
#     print(a)
#     print(b)
# hello(10)
# print(b)


def cube(a):
    return a**3;

def calc(f,val):
    return f(val)#cube(7)

print(calc(cube,7))