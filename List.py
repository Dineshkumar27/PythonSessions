#collection of different datatypes
#elements inside the list can be changed(mutable)
#we can create list in 2 ways
# 1. list()
# 2. using square brackets()
# lst=list()
# print(len(lst))
#
# empty_list=[]
# print(len(empty_list))
#
#
# fruits=['Apple','Mango','Banana','Strawberry']
# vegetable=['Onion','Drumstick','Tomato','Beans','Okra']
# milkProducts=['Milk','Yogurt','ButterMilk','Ghee','Cheese']
# print('Fruits {} and its length is {}'.format(fruits,len(fruits)))
# print('Vegetable',vegetable)
# print("Milk Products",milkProducts)
#
# #list can have mixed datatype
#
# student=['Kaavin',9,{'city':'Chennai','place':'NageswariGuruswamy st'},(78,72,69,92)]
#           # 0     1          2                                               3
# print("Length of the student",len(student))
# print("zeroth element ",student[0])
# print("1st element",student[1])
# print("2nd element",student[2])
# print("last element",student[3])#student[-1]
#
# for i in range(0,10):
#     print(i,end=' ')
# for i in student:
#     print(i)

# lst=['item1','item2','item3']
# first_item,second_item,third_item=lst
# print(first_item)#item1
# print(second_item)#item2
# print(third_item)#item3

milkProducts=['Milk','Yogurt','ButterMilk','Ghee','Cheese','Paneer']
# firstProduct,secondProduct,thirdProduct,*rest,lastproduct=milkProducts
#
# print('firstProduct',firstProduct)
# print('secondProduct',secondProduct)
# print('thirtProduct',thirdProduct)
# print('remaining',*rest)
# print('Last Product',lastproduct)

# print('Slicing one',milkProducts[1:4])#Yogurt, Buttermilk, Ghee
# print("from beginning",milkProducts[1:])
# print("from beginning",milkProducts[:4])
# print('double slicing',milkProducts[5:1:-2])

#Negative Indexing

# milkProducts=['Milk','Yogurt','ButterMilk','Ghee','Cheese','Paneer']
#                   -6     -5           -4      -3        -2       -1
# print()
# print('Negative Indexing')
# print(milkProducts[::-1])#print in reverse
# print(milkProducts[-3:])#moves right side
# print(milkProducts[-3::1])#last value -1 moves the list from right to left direction
# print(milkProducts[-3:-1])#Ghee and Cheese
#
# #list are mutable, elements are changeable
#
fruits=['Apple','Mango','Banana','Strawberry']
# print("Before changing the fruits",fruits)
# fruits[1]='Avacado'
# print("After changing the fruits",fruits)
#
# #to change the last element
# lastIndex=len(fruits)-1
# secondLastIndex=len(fruits)-2
# print('Last Fruit',fruits[lastIndex])#fruits[4-1]
# print('Second Last Fruit',fruits[secondLastIndex])#fruits[4-2]
#
# #checking the element is present or not
#
# print('papaya' in fruits)#false
# print('papaya' not in fruits)#true

#Adding into list

# fruitsList=list()
# fruitsList.append('Apple')
# fruitsList.append('Banana')
# fruitsList.append('Orange')
# print(fruitsList)
#
# #inserting into list using index number
# fruitsList.insert(1,'Lemon')
# print(fruitsList)
# #removing element from list
#
# fruitsList.remove('Banana')
# print('After removing',fruitsList)

#removing element from list using index number-> pop

# removedElement=fruitsList.pop()# removes last element
# print(removedElement, 'has been removed')
# print("removing last fruit",fruitsList)

# removedAtindex1=fruitsList.pop(1)#removes Lemon
# print(removedAtindex1)
# print("Afterremoving index 1",fruitsList)


# removing using del

tiffin=['Dosa','Idly','Pongal','Vada','Idiyappam']
# del tiffin[1]
# print(tiffin)
# del tiffin[2:]
# print(tiffin)
# del tiffin#deletes full list
# print(tiffin)

#clear will delete all the time but not the list
# tiffin.clear()
# print(tiffin)

#copying a list-change in one will not reflect another

# tiffin2=tiffin.copy()
# print(tiffin2)
# print(tiffin2[1])#idly
# tiffin2[1]='Rava Dosa'
# print('tiffin2',tiffin2)
# print('tiffin',tiffin)

#aliasing-change in one list will reflect in another list
# tiffin3=tiffin# like a alias
# print('tiffin',tiffin)
# print('tiffin3',tiffin3)
# tiffin3[1]='Rava Dosa'
# print('tiffin',tiffin)
# print('tiffin3',tiffin3)


#Joining the list
# fruits=['Apple','Orange','Apple','Apple','Orange']
#           # 0         1       2       3       4
#           #  -5     -4      -3       -2      -1
# veggies=['Onion','Tomato']
# fruits_and_veggies=fruits+veggies
# print('fruits_and_veggies',fruits_and_veggies)

#count
# print(fruits.count('Apple'))
# print(fruits.count('Orange'))
#
#
# #find the index
# print('Apple Index',fruits.index('Apple'))#0 look from 0th index
# print('Apple Index',fruits.index('Apple',2))#0 look from 2nd index
# print('Apple Index',fruits.index('Apple',-2))#0 look from -2th index


#reversing a list
#
# nums=[34,56,71,22,12,13,14,8]
# print(nums)
# nums.reverse()#modifies the original list
# print(nums)

#sorting

# fruits=['Apple','Mango','Banana','Strawberry']
# fruits.sort()#sort in ascending order
# print(fruits)
# fruits.sort(reverse=True)
# print(fruits)

# Sorted it will not modify the original list
# print(sorted(fruits))#sort and print without modifying the original list
# print(fruits)
# print(sorted(fruits,reverse=True))



#list comprehension

#usual way
# ls=[1,2,3,4,5]
# for i in ls:
#     print(i)

#using List Comprehension

# print([i for i in ls])#output is list
#
# squares=[i*i for i in ls]
# print(squares)
#
# cubes=[i*i*i for i in ls]
# print(cubes)
#
# tuple_sq=[(i,i*i) for i in ls]
# print(tuple_sq)

#adding if condition with tuples
# even_number=[i for i in range(21) if i%2==0]
# print(even_number)
#
# odd_number=[i for i in range(21) if i%2==1]
# print(odd_number)