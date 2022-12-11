
# Python program to demonstrate
# dictionary


# Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# print("Dictionary:")
# print(Dict)
# print(Dict[4])

# Uncommenting this print(Dict[4])
# will raise a KeyError as the
# 4 is not present in the dictionary

# Python program to demonstrate
# defaultdict
from collections import defaultdict


# Function to return a default
# values for keys that is not
# present
def def_value():
    return "Not Present"


# Defining the dict
d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])
