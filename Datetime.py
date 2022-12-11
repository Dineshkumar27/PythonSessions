# import datetime
# print(dir(datetime))

#Getting Datetime information

from datetime import datetime
# now=datetime.now()
#
# day=now.day
# month=now.month
# year=now.year
# hour=now.hour
# minute=now.minute
# seconds=now.second
# timestamp=now.timestamp()
# print(day,month,year,hour,minute,seconds)
# print('Timestamp',timestamp)
# print(f'{day}/{month}/{year},{hour}:{minute}')


# now=datetime(2020,1,1)
#
# day=now.day
# month=now.month
# year=now.year
# hour=now.hour
# minute=now.minute
# seconds=now.second
# timestamp=now.timestamp()
# print(day,month,year,hour,minute,seconds)
# print('Timestamp',timestamp)
# print(f'{day}/{month}/{year},{hour}:{minute}')

now=datetime.now()
t=now.strftime("%H:%M:%S")
print("time",t)
time1=now.strftime("%d/%m/%y,%H:%M:%S")#format to dd/mm/yy h:m:s
print(time1)

dataString="31 July 2022"
print("date_string",dataString)
#convering string to date
date_object=datetime.strptime(dataString,"%d  %B %Y")
print(date_object)

