a=10
b=3

# 1.Arithmetic Operators
# print('a+b',a+b)
# print('a-b',a-b)
# print('a*b',a*b)
# print('a/b',a/b)#quotient-3
# print('a//b',a//b)#quotient-3
# print('a%b',a%b)#reminder-1


# 2. Comparison or Relational Operator(always returns True or False)
# print("a=",a," b=",b)
# print("a>b",a>b)
# print("a<b",a<b)
# print("a<=b",a<=b)
# print("a>=b",a>=b)
# print("a==b",a==b)
# print("a!=b",a!=b)

#3. logical operators(and, or, not(return True or False, used to compare more than one condition)
# c=15
# print("a=",a," b=",b,"c=",c)
# print("a>b and a>c",(a>b)and(a>c))#and both condition must be True,output will be True,otherwise False
# print("a>b or a>c",(a>b)or(a>c))#if any condition is True,output will be True,otherwise False
# print("not(a>b or a>c)",not((a>b)or(a>c)))#if any condition is True,output will be True,otherwise False
#
# #4 Bitwise operator(&,|,>>,<<)
# print("a|b",a|b)
# print("a&b",a&b)
# print(5>>1)
# print(5<<1)

# 5|3
#
# 421
# 101
# 011
# --- (or)        and
# 111  - 7        001-1
# 8421
# 1010
# 0011
# ------
  # 1011
  # 0010

#5 Membership operator(in, not in)
# print(5 in [3,4,5,6,7])#True
# print(11 not in [9,8,7,6])#True
# #False condtion
#
# print(5 not in [3,4,5,6,7])#False
# print(11 in [3,4,5,6,7])#False

#6 Identity Operator
# id() gives address of the variable
# num1=8
# num2=8
# print(id(num1))
# print(id(num2))
# print(num1 is num2)#False
# print(num1 is not num2)#True

#7 Assignment Operator(=,+=,-=,*=)
val1=10
print("val1 is ",val1)
# val1=val1+20;#30
val1+=20;#30
val1-=2;#28
print("updated val1 is",val1)
