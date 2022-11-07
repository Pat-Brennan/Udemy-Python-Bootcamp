
# * Inheritance!
# ? A key feature of OOP is the ability to define a class which inherits from ->
# ? another class (a "base" or "parent" class)

# ? In Python, inheritance works by passing the parent class as an ->
# ? argument to the definition of a child class

class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"This animal says {sound}")


# * Using super()

class Cat(Animal):
    def __init__(self, name, breed, toy):
        # super() reduces the duplication of "self.whatever" etc
        super().__init__(name, species="Cat")
        # In this case self.name and species since they are already in class Animal
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")


eorah = Cat()
print(eorah.make_sound("Meowmeoeoemeow"))

# isinstance = Boolean method. Should return True.
print(isinstance(eorah, Cat))
