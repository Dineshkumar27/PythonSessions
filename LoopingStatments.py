#for
# #while
# friends=['Raja','Ragu','Mani','Divakar','John']
# for friend in friends:
#     print(friend,"is my friend",sep='->',end="\n")
# #
# numbers=[45,67,89,32,59]
# for number in numbers:
#     print(number*2)

# example of end and sep
# print("hello","python",sep='-')#hello-python
# print('Kaavin is',end='-')
# print('Learning python')

# print('Python','is','used','everywhere','and','it is','popular',sep="-",end="_as well")
# Python-is-used-everywhere-and-it is-popular_as well

# for i in [3,4,5,6]:
#     print(i*i,end=' ')


#while loop

# i=1
# while(i<=10):
#     print(i,end='\n')
#     i+=1#add 1 with current i value


friends=['Raja','Ragu','Mani','Divakar','John']
# indexNumber 0     1      2       3        4
# print(friends[0])
# print(friends[1])
# print(friends[2])
# print(friends[3])

# index=0
# while(index<len(friends)):
#     print(friends[index],end=" ")
#     index+=1

#break-it will make the loop to stop
# for i in range(100,110):
#     if(i==105):
#         break#stop the execution and come out of the loop
#     print(i,end=' ')

# continue
# for i in range(100,110):
#     if(i%2==0):#check if the remainder is zero
#         continue
#     print(i,end=' ')


#get input from user untill user says no or n
total=0
while(True):
    val=int(input("Enter a number"))
    total+=val
    choice=input('you like enter another number')
    if(choice in ('no','n')):
        break

print(total)