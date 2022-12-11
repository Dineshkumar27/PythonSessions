#Exception-> abnormal error in a program during runtime
#try,except,else,finally
#try-> check for exception and throw only the first exception
#except-> will execute when there is exception
#else-> will execute with try block
#finally->will execute compulsorily

# try:
#     print(1/0)
#     print("Kaavin")
# except:
#     print("Error")

# try:
#     name=input("enter your name")
#     yearborn=input("Enter you born year")
#     age=2022-int(yearborn)
#     print(f'your name is {name} your age is {age}')
# except TypeError:
#     print("Type Error ")
# except ValueError:
#     print("Value error occured")
# except ZeroDivisionError:
#     print("Zero division Error")
# else:
#     print("I run with try block")
# finally:
#     print("Finally block")

try:
    name=input("enter your name")
    yearborn=input("Enter you born year")
    age=2022-int(yearborn)
    print(f'your name is {name} your age is {age}')
except Exception as e:
    print(e)
else:
    print("I run with try block")
finally:
    print("Finally block")