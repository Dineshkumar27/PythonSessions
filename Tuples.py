#tuple is like list but immutable(not changeable)
# () used to store the elements
# we cannot add,remove like list
empty_tuple=tuple()
# or
empty_tuple=()
fruits=('Apple','Mango','Banana','Strawberry')
print(len(fruits))

#accessing tuple elements

print(fruits[0])
print(fruits[-1])
last_index=len(fruits)-1
print(fruits[last_index])
print(fruits[-2])#Banana


#slicing

print(fruits[:])
print(fruits[2:])
print(fruits[:3])
print(fruits[-4:-2])

#chaning a tuple into list
# tuple->list->added Avacado->tuple
print(type(fruits))
fruitsList=list(fruits)
print(type(fruitsList))
fruitsList.append('Avacado')
print(fruitsList)
fruits=tuple(fruitsList)#converting list to tuple
print(fruits)
print(fruits.count('Avacado'))
print(fruits.index('Avacado'))

rollNo=(1,2)
rollNo=rollNo+(3,)#to add element to tuple
print(rollNo)
del rollNo
print(rollNo)