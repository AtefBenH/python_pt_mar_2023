
# This is a comment this line will not be interpreted

"""
this is a multi
line comment == DOCSTRING
"""

# Variables

# JavaScript var name = "alex"
# ! PRiMITIVE types
# String
name = "alex"
# firstStr = camelCase
first_str = "hello welcome to python"

snake_case = "all lower case, separated  by underscore"

GLOBAL_VAR = "all caps"

# numbers 
# - Integers
age = 35

# - Floats
my_bmi = 2.32

# print(type(name))

concat_string = "My name is " + name + " I am " + str(age) + " years old . "

formatted_string = f"My name is {name} I am {age} years old !!!!"
# print(formatted_string)

# boolean

vote = True
is_admin = False

# print(type(vote))

# * COMPOSITE Types --- variables
# ------------LISTS--------------

# index    0,1,2,3,4,5 
my_list = [1,2,3,4,5,6]

#             -3     -2        -1
names = ["sam", name,"john", "sarah"]

names[1] = "daniel"
# print(names[1])
# print(names[1:3])
# print(names[-1])

# print(f"the length of th list is {len(names)*200}")
names.sort(reverse=True)

# names.append("BoB")
names.insert(1,"Bob")
# print(names)

# --------- DICTIONARIES ---------
# oBJECTS IN JS

# ! NO index, couple (pair) key,value pair

alex_dict = {
    'username':name,
    'age':28,
    'marks' : [9.5,9.25,10]
}

bob_dict = {
    'username':"bob",
    'age':35,
    'marks' : [9.5,9.25,10]
}
users = [bob_dict,alex_dict]

# print(users)
# print(alex_dict["marks"][1])
alex_dict["is_admin"] = is_admin
# print(alex_dict)

# ------------TUPLES-------------
# similar to list :immutable : cannot be changed 
tup  = (1,2,3,4)
# print(tup[2])

#! tup[0] = 2000
tup2 = (vote,names,users,alex_dict,"HI")
print(tup2)