#Python is Object oriented programming language
# Everything in python is object, object has properties and methods
#string,list, tuple, dictionary are all object
# We create a class to create a object
# A class is like object constructor or 'BluePrint' for creating an object
# we have to instantiate class to create an object
#while object on other hand represents the class
# num=10
# print(type(num))
# name='Kaavin'
# print(type(name))
# marks=[78,79,80]
# print(type(marks))

#creating class in python
#use keyword class followed by name and colon

# class Class_name:
#     code

#
# class Person:
#     pass
# print(Person)
# #
# # #creating an object to Person
# #
# p=Person()
# print(p)

#having a class without constructor is useless
#python has built in constructor
#init() function with self parameter
#
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
# p1=Person('Kavin',15)
# print(p1.name)
# print(p1.age)
# print(p1)
# p2=Person('Jagan',25)
# print(p2.name)
# print(p2.age)
# print(p2)

#
#
# class Person:
#     #constructor with 4 parameter
#     def __init__(self,name,age,country,city):
#         self.name=name
#         self.age=age
#         self.country=country
#         self.city=city
#
# #
# p1=Person('Kavin',15,'India','Chennai')
# print(p1.name)
# print(p1.age)
# print(p1.country)
# print(p1.city)
# print(p1)

#
#
# class Person:
#     #constructor with 4 parameter
#     def __init__(self,name,age,country,city):
#         self.name=name
#         self.age=age
#         self.country=country
#         self.city=city
#     #method
#     def person_info(self):
#         return f'{self.name} age is {self.age} from city {self.city} of {self.country}'
#
# p1=Person('Kavin',15,'India','Chennai')
# # print(p1.name)
# # print(p1.age)
# # print(p1.country)
# # print(p1.city)
#
# print(p1.person_info())


#Object with default methods
#it is used to avoid errors when we call or instantiate our class without parameter

# class Person:
#     #constructor with 4 parameter
#     def __init__(self,name='Raj',age=15,country='India',city='Hyderabad'):
#         self.name=name
#         self.age=age
#         self.country=country
#         self.city=city
#     #method
#     def person_info(self):
#         return f'{self.name} age is {self.age} from city {self.city} of {self.country}'
#
# p1=Person('Kavin',15,'India','Chennai')
# print(p1.person_info())
# p2=Person()
# print(p2.person_info())


#method to modify a class default value


class Person:
    #constructor with 4 parameter
    def __init__(self, name='Raj', age=15, country='India', city='Hyderabad'):
        self.name=name
        self.age=age
        self.country=country
        self.city=city
        self.skills=[]

    #method
    def person_info(self):
        return f'{self.name} age is {self.age} from city {self.city} of {self.country} has skills {self.skills}'
    def add_skills(self,skill):
        self.skills.append(skill)

p1=Person()
print(p1.person_info())
p1.add_skills('HTML')
p1.add_skills('CSS')
p1.add_skills('Python')
p2=Person('John',16,'Mumbai','India')
print(p2.person_info())
print(p1.skills)#['HTML', 'CSS', 'Python']
print(p2.skills)#empty []
#
#
# #Inheritance
# #we can reuse the code of the parent class.
# #It allows a child class(Sub class) to inherit the properties and methods of parent class(Super class)
#
#
# class Student(Person):#student class inherits Person class
#     pass
# #
# s1=Student('Akub',23,'Johnesberg','SouthAfrica')
# s2=Student('Jagan',27,'Chicago','USA')
# s1.add_skills('Java')
# s1.add_skills('Machine Learning')
# s1.add_skills('Big Data')
# s2.add_skills('C')
# s2.add_skills('C#')
# s2.add_skills('MySQL')
# print(s1.person_info())
# print(s2.person_info())

#Overriding
#rewriting the logic of the method in parent class with same name
#method with same name in both Parent class and Child class

class Student(Person):
    def __init__(self, name='Raj', age=15, country='India', city='Hyderabad',gender='Male'):
        super().__init__(name,age,country,city)
        self.gender=gender

    # method
    def person_info(self):
        gender='He' if self.gender=='Male' else 'She'
        return f'{self.name} age is {self.age}. {gender} lives  in {self.city} of {self.country} has skills {self.skills}'


s1=Student('Akub',23,'Johnesberg','SouthAfrica','Male')
s2=Student('Subhashini',27,'Chicago','USA','Female')
s1.add_skills('Java')
s1.add_skills('Machine Learning')
s1.add_skills('Big Data')
s2.add_skills('C')
s2.add_skills('C#')
s2.add_skills('MySQL')
print(s1.person_info())
print(s2.person_info())


# Exercise
# Create a class called PersonAccount. It as firstName, lastName, incomes, expenses properties
# and it has method, total_income, total_expenses, account_info, add_income, add_expense and accout_balance.for Incomes is a set of income and its description
# same for expense as well.