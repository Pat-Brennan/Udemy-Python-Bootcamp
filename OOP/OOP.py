
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

class User:  # this is what every user will look like
    pass


user1 = User()  # This is INSTANTIATING user!
user2 = User()  # This is INSTANTIATING user!
user3 = User()  # This is INSTANTIATING user!
user4 = User()  # This is INSTANTIATING user!
print(type(user1))
