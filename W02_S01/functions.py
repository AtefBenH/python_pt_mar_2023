# FUNCTIONS

# a set of instructions 
#  could take in parameters 
# ! All functions Always RETURNS SOMETHING EVEN IF IT4S NONE

# VERB

# function sayHi(){
#     console.log("Hi")
# }
def say_hi():
    print("Hello Ninjas")
# ! CALL == INVOKE the function
def say_hello(name):
    return f"Hello {name} !!! "
    print(f"Hello {name} !!! ")

result  = say_hello("Alex")
# print(result)

# --------------------

def multiply(*args):
    print("Args == ",args)
    multiply_result = 1
    for i in args:
        multiply_result = multiply_result*i
    print("Result = ",multiply_result)
    return multiply_result

# def multiply(a,b):
#     print("Args == ",args)
#     a = 1
#     for i in args:
#         a = a*i
#     print("Result = ",a)
#     return a
    

# multiply(2,5,25,41,25,88,63,7,1,83,3,9,555)

# -------------------
def say_mu_fullname(first_name,last_name):
    print(f"Your Fullname is {first_name} {last_name}")
    return None

say_mu_fullname("Marley","Bob")

# -------------------
def say_mu_fullname(**kwargs):
    print("KWARGS === ",kwargs)
    print(f"Your Fullname is {kwargs['first_name']} {kwargs['last_name']}")
    return None

say_mu_fullname(last_name="Marley",first_name="Bob")
say_mu_fullname(first_name="Steve",last_name="Jobs")