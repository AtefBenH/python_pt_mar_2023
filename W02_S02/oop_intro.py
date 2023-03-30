# OOP

# ? OOP ? =  Object Orientated Programming 

# Model Real Life
# write Cleaner Code 
# DRY : Don't Repeat Yourself

student_1 = {'id':1,'first_name':"John", 'last_name':"Wick",'age':45,'grade':9.8}
student_2 = {'first_name':"Jack", 'last_name':"Sparrow",'age':56,'grade':7.5}
student_3 = {'first_name':"May", 'last_name':"Jones",'age':32,'grade':8.7}

#? Class ? = template or blueprint for creating new objects (students)
# Constructor  ==> create new objects == initialize  instances ( = objects) of the class

# Naming classes we must follow the PascalCase

class Student:

    school  = "MIT" # Class Attribute
    all_students = [] # Class Attribute ==> All the Instances of the Class have the access to these Class Attributes 
    def __init__(self,first_name, last_name,age ,grade):
        # - Attributes = What the Class Can Have (nouns) characteristics
        # Attributes -----Values 
        # Note Instance Attributes ==> reserved to the Instance
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grade = grade
        Student.all_students.append(self)
    
    # --Methods = What the class can do (verbs) actions == Functions inside a Class
    def increase_age(self):
        self.age+=1
        print(f"Happy Birthday you are {self.age} years old now !!!!!!")
        return self
    
    def __repr__(self):
         return(f"Student fullname is {self.first_name} {self.last_name} and he is {self.age} years Old ! 😎" )
    # def print_info(self):
    #     print(f"Student FullName is {self.first_name} {self.last_name} and he is {self.age} years Old !")
    #     return self


alex = Student("Alex", "Max",28, 7.23)
# print(alex.first_name, " --- ", alex.last_name, " --- ",alex.grade, " --- ",alex.age)
# -  Chaining Methods 
# alex.print_info().increase_age().print_info().increase_age().print_info()

sam = Student("Sam","Maxwell", 39,8.75)
jack = Student("Jack","Sparrow", 22,8.75)
john = Student("John","Wick", 49,8.75)
mary = Student("Mary","Jones", 78,8.75)
# print(sam.first_name, " --- ", sam.last_name)
# print("Alex == ",alex.school)
# alex.print_info()
# print("Sam == ",sam.school)
# sam.print_info()

# print(sam.all_students)
# for student in alex.all_students:
#     student.print_info()

print(alex)