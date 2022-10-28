
# * Inheritance!
# ? A key feature of OOP is the ability to define a class which inherits from ->
# ? another class (a "base" or "parent" class)

# ? In Python, inheritance works by passing the parent class as an ->
# ? argument to the definition of a child class

class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        print(f"This animal says {sound}")


class Cat(Animal):
    def __init__(self, name, species, breed, toy):
        self.name = name  # ? Eorah 😈
        self.species = species  # ? Cat 😸
        self.breed = breed  # ? Hellspawn 🔥
        self.toy = toy  # ? Human Feet 🦶


eorah = Cat()
print(eorah.make_sound("Meowmeoeoemeow"))

# isinstance = Boolean method. Should return True.
print(isinstance(eorah, Cat))
