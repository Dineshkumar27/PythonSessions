#will not allow duplicates
#no index number
#can be access only by for loop
# empty_set=set()
# # or
# empty_set={}
#
# set1={1,1,1,3,4,5,6,7,3,4,5}
# print(set1)
# # print(set1[1])#error
#
# for i in set1:
#     print(i)
# print(11 in set1)#false
#
# #adding element into set
#
# set1.add(89)
# print(set1)
#
# #update() takes list as argument
# set1.update([77,88,99])
# print(set1)
#
# #remove
# set1.remove(77)
# print(set1)
#
# set1.pop()#removes element randomly
# print(set1)
#
#
# print(set1.pop())#print the removed element
# print(set1)
#
# # set1.clear()#removes the element
# print(set1)
#
# # del set1#removes the set
#
# list1=[78,90]
#
# set2=set(list1)#converting list into set
# print(set2)
# print(set1)
# print(set1.union(set2))
# # print(set1)
# set1.update(set2)#set2 content will be copied to set1
# print(set1,"After update")

# data1={1,2,3,4,5,6,7}
# data2={3,9,8,11,22,5,3}
# print(data1.intersection(data2))

data3={3,4,5,6,7,8}
data4={4,15,16}
print(data3.issuperset(data4))#all elements of data4 is avaialble in data3
print(data4.issubset(data3))

#difference between sets

print("data3.difference(data4)",data3.difference(data4))#removes the element of data4 from data3 which is common among the two sets
print("data4.difference(data3)",data4.difference(data3))#from data4 to data3

#symmetric difference which give uncommon elements from both sets
# data3={3,4,5,6,7,8}
# data4={4,15,16}
#4 is common in both sets so they are not disjoint

# data3={3,4,5,6,7,8}
# data4={14,15,16}
#no common elements between data3 and data4 so they are disjoint

print("data3.symmetric_difference(data4)",data3.symmetric_difference(data4))

#NO common item between two sets is called disjoint

print("data4.isdisjoint(data3)",data4.isdisjoint(data3))


