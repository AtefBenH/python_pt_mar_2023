# Loops

# For Loops

# for (var i=0;i<11;i++) {
#     console.log(i)
# }
# range() is a function that returns a sequence of Integers 
# - example (0,1,2,,,,10)
#  start --- inclusive, optional - default = 0
#  stop --- exclusive, required
#  step --- increment value - default = 1 , con be positive (+) or negative (-)

# for i in range(0,10,1):
#     print(i)
# for i in range(11):
#     print(i)
# for i in range(11,0,-1):
#     print(i)
# for bob in range(1,11,2):
#     print(bob)
#               0       1           2               3           4      5 6
superheros = ["batman","superman", "spiderman","wonder woman", "thor",10,22]

# for i in range(len(superheros)):
#     print(i, "----",superheros[i])

# for hero in superheros:
#     print(hero)

# for char in "WELCOME TO PYTHON":
#     print(char)
#     if char == "O":
#         print("We Found O !!!")
alex_dict = {
    'username':"alex",
    'age':28,
    'marks' : [9.5,9.25,10]
}

bob_dict = {
    'username':"bob",
    'age':35,
    'marks' : [9.5,9.25,10]
}

# for key in alex_dict:
#     print(f"{key} --- {alex_dict[key]} ")

# for val in alex_dict.values():
#     print(val)

for key,val in alex_dict.items():
    print(key, "---",val)

# While 

x = 5
while x>0: # This while loop will be running until this condition breaks (x>0 == False) 
    print("Hi" , x)
    x-=1