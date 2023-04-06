
# 4 Pillars of OOP
# -1 - Encapsulation = Create Classes (blueprint)
# -2 - Inheritance      
# -3 - Polymorphism  = many forms
# -4 - Abstraction = Hide Complexity

class Human:

    # Constructor
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.strength = 10
        self.power = 10
        self.defense = 5
        self.weapon = None
    
    def attack(self,target):
        print(f"[ATTACK] {self.name} is attacking {target.name}")
        target.defend(self.power) #! Abstraction
        # target.health -= self.power
    
    def defend(self, damage):
        damage -= self.defense
        self.health -= damage
        print(f"[DEFEND] {self.name} takes {damage} and now has {self.health} HP")

# ! Inheritance 

class Barbarian(Human):
    def __init__(self, name):
        super().__init__(name)
        self.strength += 20 #! Polymorphism (modify the parent attribute)
        self.rage = 35  #! Polymorphism (add a new attribute that belongs only to the child class(Barbarian))


class Knight(Human):
    def __init__(self, name):
        super().__init__(name) # call my Parent(Human)
        # self.name = name
        self.health += 10
        self.defense += 50
    
    def heal(self): #! Polymorphism (add a new method that belongs only to the child class(Knight))
        self.health += self.defense/4
        print(f"[knight] {self.name} heals for {self.defense/4} and now has {self.health} HP")


class Seer :
    def __init__(self):
        self.magic = 50
        self.hidden_type = Barbarian("No Name") #! Abstraction



alex = Human("Alex")
john = Human("John")
conan = Barbarian("Conan")
# print("Conan Health",conan.health)
alex.attack(john)
# conan.attack(john)
# print(type(alex))
# print(type(conan))
# print(isinstance(conan, Human))
# print("Conan Power",conan.power)

sam = Seer()
print("Conan Health",conan.health)
sam.hidden_type.attack(conan)
print("Conan Health",conan.health)
print("***********",sam.hidden_type,"**********")

arthur = Knight("Arthur")
print(f"Arthur health before healing : {arthur.health}")
arthur.heal()
print(f"Arthur health after healing : {arthur.health}")