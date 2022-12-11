#we use two operators
#* for tuples,list
#** for dictionaries


#unpacking

# def sumoffivnums(a,b,c,d,e):
#     print("a=",a,"c=",c)
#     return a+b+c+d+e
#
#
# lst=[1,2,3,4,5]
# print(sumoffivnums(*lst))



# numbers=range(2,7)
# print(list(numbers))#2,3,4,5,6
# args=[3,8]
# print(list(range(*args)))

dct={'name':'ABC','age':89}
def unpackingdct(name,age):
    return f'{name} has age {age}'
print(unpackingdct(**dct))#key and argument name should match