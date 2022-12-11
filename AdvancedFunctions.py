# function performs following operation
# can take parameter
# function can take another function as a parameter
# function can be modified
# function can be assigned to a variable


'''
1.how to handle function as a parameter
2. returning a function as a return value
3. python closures and decorators

'''

#function as a parameter


def sum_number(nums):
    return sum(nums)


def higher_order_function(f,lst):
    summation=f(lst)#sum_number([1,2,3]) this will call sum_number in line no 18
    return summation
result=higher_order_function(sum_number,[78,2,100])
print("answer",result)

def square(x):
    return x**2
def cube(x):
    return x**3
def absolute(x):
    if(x>0):
        return x
    else:
        return -(x)

def higher_order_demo2(type):
    if type=="square":
        return square
    elif type=="cube":
        return cube
    elif type=='absolute':
        return absolute
result=higher_order_demo2('square')
print(result(9))
result=higher_order_demo2('cube')
print(result(6))
result=higher_order_demo2('absolute')
print(result(-6))
print(result)#<function absolute at 0x000002108E078790>


def sub(a,b):
    return a-b