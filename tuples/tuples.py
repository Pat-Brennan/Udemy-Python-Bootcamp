
# * Tuples
# ? An ordered collection or grouping of items
# ? Very similar to lists
# ? Syntax: x = (1, 2, 3, 4) notice the parens
# ! Tuples are IMMUTABLE! You cannot change them!

x = (1, 2, 3, 4)
print(3 in x)  # prints True
# x[0] = "Please help me change!" # creates TYPE ERROR

# * Why would we use these?
# ? Tuples are FASTER than lists
# ? It can also make your code safer from bugs
# ? Valid keys in a dictionary
# ? Some methods return them to you - like .items() when working with Dictionaries!

print(x[2])  # access values with [] just like Lists!

first_tuple = (1, 2, 3, 3, 3)  # Duplicate data is okay!


# * Using Tuples as keys in a dictionary

locations = {
    (45, 89): 'tokyo',
    (100, 666): 'hell',
    (444, 333): 'my house'
}

print(locations[(100, 666)])  # prints hell

# * .items() returns Tuples

cat = {
    'Name': 'Eorah',
    'Age': 666,
    'Favorite Toy': 'Feet'
}

print(cat.items())
