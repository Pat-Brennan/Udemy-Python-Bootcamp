
# * OOP! : Object Oriented Programming
# ! OOP is NOT unique to Python!
# ? OOP is  a method of programming that attempts to model some process or thing ->
# ? in the world as a CLASS or OBJECT.

# * What is a CLASS?
# ? A blueprint for objects. Classes can contain methods (functions) ->
# ? and attributes(similar to keys in a dict)

# * What is an INSTANCE?
# ? Objects that are constructed from a class blueprint that contains their class's ->
# ? methods and properties.

# * Why OOP?
# ? With object oriented programming, the goal is to encapsulate your code into ->
# ? LOGICAL, HIERARCHICAL groupings using classes so that you can reason ->
# ? about your code at a higher level.

# * Encapsulation
# ? The grouping of public and private attributes and methods into a ->
# ? programmatic class, making abstraction possible.

# * Abstraction
# ? Exposing only "relevant" data in a class interface, hiding private attributes and methods ->
# ? (aka the "inner workings") from users.

# * Creating a Class
# ? conventionally named with singular terms, i.e "User", "Dog", "Person"
# ? also typically written with camelcase instead of snake case

# * The 'self' keyword
# ? refers to the current class instance
# ? Technically, this doesn't need to be called self, but it is standard and ->
# ? pretty much the only thing you'll see.
class User:  # this is what every user will look like

    def __init__(self, first, last, pet):  # Does not need to be SELF, but it's practical!
        self.first = first
        self.last = last
        self.pet = pet


user1 = User('steve', 'jobs', 'porcupine')  # This is INSTANTIATING user!
user2 = User('Joey', 'bag o donuts', 'rock')  # This is INSTANTIATING user!
print(user1.first, user1.pet)
print(user2.first, user2.pet)


# * __init__
# ? Classes in python can have a special __init__ method, which gets called every time ->
# ? you create an instance of the class (instantiate).


class Vehicle:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


# * What's the deal with underscores anyway?
# ? _name: Merely Conventional. Meant to IMPLY that an attribute should be PRIVATE
# ? __name: "Name Mangling": Meant to make an attribute very specific to it's class
# ? __name__: Dunders define PYTHON SPECIFIC METHODS
