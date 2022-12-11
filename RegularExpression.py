#Methods in re module

# re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
# re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
# re.findall: Returns a list containing all matches
# re.split: Takes a string, splits it at the match points, returns a list
# re.sub: Replaces one or many matches within a string


# syntax
# re.match(substring, string, re.I)
# substring is a string or a pattern, string is the text we look for a pattern ,
# re.I is case ignore
#
# import re
#
# txt='I love to teach Python and Java'
#
# match=re.match('I LOVE to teach',txt,re.I)
# print(match)
# span=match.span()#0 15
# start,end=span
# print(start,end)
# substring=txt[start:end]
# print(substring)


# import re
#
# txt = 'I love to teach python and Java'
# match = re.match('I like to teach', txt, re.I)
# print(match)  # None


# syntax
# re.search(substring, string, re.I)
# substring is a pattern, string is the text we look for a pattern , re.I is case ignore flag

#
# import re
#
# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend Python for a first programming language'''
#
# # It returns an object with span and match
# match = re.search('first', txt, re.I)
# print(match)  # <re.Match object; span=(100, 105), match='first'>
# # We can get the starting and ending position of the match as tuple using span
# span = match.span()
# print(span)     # (100,105)
# # Lets find the start and stop position from the span
# start, end = span
# print(start, end)  # 100 105
# substring = txt[start:end]
# print(substring)       # first



# findall() returns all the matches as a list
# import re
# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''
#
# # It return a list
# matches = re.findall('language', txt, re.I)
# print(matches)  # ['language', 'language']

#
# import re
# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''
#
# # It returns list
# matches = re.findall('python', txt, re.I)
# print(matches)  # ['Python', 'python']

# import re
#
# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''
# #
# matches = re.findall('Python|python', txt)
# print(matches)  # ['Python', 'python']
#
# #
# matches = re.findall('[Pp]ython', txt)
# print(matches)  # ['Python', 'python']
#
# c[aie]ll-> call,cill,cell



# Replacing a Substring
# import re
# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''
#
# match_replaced = re.sub('Python|python', 'Java', txt, re.I)
# print(match_replaced)  # Java is the most beautiful language that a human being has ever created.
# # OR
# match_replaced = re.sub('[Pp]ython', 'Java', txt, re.I)
# print(match_replaced)  # Java is the most beautiful language that a human being has ever created.


# import re
# txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
# T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
# I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
# D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''
#
# matches = re.sub('%', '', txt)
# print(matches)


# Splitting Text Using RegEx Split
# import re
# txt = '''I am teacher and  I love teaching.
# There is nothing as rewarding as educating and empowering people.
# I found teaching more interesting than any other jobs.
# Does this motivate you to be a teacher?'''
# print(re.split('\n', txt)) # splitting using \n - end of line symbol,\W for spliting into word


#
# import re
# string='Hello all today is 17th August 2022 and it is a 4th day of this week'
# pattern='\d+'
#
# result=re.findall(pattern,string)
# print(result)
# result2=re.split(pattern,string)
# print(result2)

# details='''rakshan 9987898897 sam 7897897898 riya 4567899876 suki 9089089099'''
details='''suki 
   rakshan'''
# pattern='\d{10}'
# phoneNumbers=re.findall(pattern,details)
# print(phoneNumbers)

pattern='^s..i$'
result4=re.search(pattern,details)
print(result4)







