
# * Inheritance!
# ? A key feature of OOP is the ability to define a class which inherits from ->
# ? another class (a "base" or "parent" class)

# ? In Python, inheritance works by passing the parent class as an ->
# ? argument to the definition of a child class

class Animal:

    def make_sound(self, sound):
        print(sound)

    cool = True


class Cat(Animal):
    pass


eorah = Cat()
print(eorah.make_sound("Meowmeoeoemeow"))

# isinstance = Boolean method. Should return True.
print(isinstance(eorah, Cat))
