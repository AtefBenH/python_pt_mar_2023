# review OOP


class Ninja :

    all_ninjas = []
    dojo = "Dojo1" # Class Attribute belong the Class itself (Ninja) / No self
    # Constructor 
    def __init__(self,name,health, power, weapon):
        self.name = name
        self.health = health
        self.power = power
        self.weapon = weapon
        Ninja.all_ninjas.append(self)

    # - METHODS             
    def display_info(self):
        print(f"Name : {self.name} \n Health : {self.health} \n Power : {self.power} \n Weapon : {self.weapon}")
        return self
    
    def train(self):
        self.power += 10
        print(f"{self.name} is Trained {self.power}")
        return self
    
    @classmethod
    def change_dojo(cls,new_name):
        cls.dojo = new_name

    @classmethod
    def boot_camp(cls):
        print("*"*25,"WELCOME TO THE BOOT_CAMP", "*"*25)
        for ninja in cls.all_ninjas:
            ninja.train().train()
            ninja.health +=20
    
    @staticmethod
    def is_valid(dictionary):
        is_valid = True
        if dictionary["name"] == "":
            is_valid = False
        return is_valid



ninja1 = Ninja("Leonardo", 100,120,"Sword")
ninja2 = Ninja("M. Angelo", 100,20,"Knife")
ninja3 = Ninja("Bernardo", 100,200,"Arrow")
ninja4 = Ninja("Naruto", 100,525,"Bushido")
# ninja1.display_info().train()

# for ninja in Ninja.all_ninjas:
#     ninja.display_info()

# print(Ninja.dojo)
# Ninja.change_dojo("California")
# print(Ninja.dojo)

# Ninja.boot_camp()

# for ninja in Ninja.all_ninjas:
#     ninja.display_info()

Ninja.instructor = "Alex"
print(Ninja.instructor)

# ****************************************************
# ? (Class) Method that will change class Attributes
# Can be called from the Class
# have no access to the instance 
# ! NO self
# WE CANNOT CHANGE AN INDIVIDUAL INSTANCE FROM IT
# decorator : @classmethod
# ****************************************************

# ****************************************************
# ? (Static) Method
"""
stationary / non changing
no access to anything
independent
validation / utility 
decorator @staticmethod
"""
# *****************************************************