#compact way of creating  a list from sequence
#short way to create list
#fast processing

#one way of creating a list
wish="Good Morning"
# lst=list(wish)
# print(lst)
#
# #second way of creating a list
# lst=[i for i in wish]
# print(type(lst))
# print(lst)

# Example2
#Generate  a numbers
#
# numbers=[i for i in range(11)]
# print(numbers)
#
# squarenumbers=[i*i for i in range(11)]
# print(squarenumbers)
#
# cubenumbers=[i*i*i for i in range(11)]
# print(cubenumbers)

#using if condition in List comprehension
# evenNumbers=[i for i in range(11) if i%2==0]
# print("Even numbers",evenNumbers)
# #
# oddNumbers=[i for i in range(11) if i%2==1]
# print("Odd numbers",oddNumbers)
#
# numbers=[-4,-5,-6,-8,-10,0,2,4,6,8]
# positiveEvennumbers=[i for i in numbers if i%2==0 and i>0]
# print("positive numbers",positiveEvennumbers)

#


#lambda function
#Lambda function is an unnamed function, it can take any number of arguments
#but have only one expression

#creating a lambda function
# use keyword 'lamba' followed by expression
#lambda function doesnot return any value, but explicitly return a value
# x=lambda para1,para2,para3:para1+para2+para3
# print(x(arg1,arg2,arg3))

#Named function
def add_two_numbers(a,b):
    return a+b
print(add_two_numbers(4,5))

#converting the above function using lambda expression

add_numbers=lambda a,b:a+b
print(add_numbers(3,4))

square=lambda x:x*x
print("Square",square(8))

cube=lambda x:x*x*x  #x is parameter
print("Cube",cube(8))# 8 is argument


def power(x):
    return lambda n:x**n

print("Lamba function inside function",power(2)(3))


