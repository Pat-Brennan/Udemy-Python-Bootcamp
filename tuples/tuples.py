
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

# * Looping over Tuples
# ? Basically the same as looping over a list!

names = ('Eorah', 'Bongo', 'Reptar')

# ? Prints the list of names
for name in names:
    print(name)

# ? Prints the list of names in reverse
i = len(names) - 1
while i >= 0:
    print(names[i])
    i -= 1

# * Tuple Methods
# ? Thankfully, there's only two! 

# * .count()
# ? Returns the number of times a value appears in a Tuple

print(first_tuple.count(3)) # prints 3 because there are three... 3's

# * .index()
# ? Returns the index at which a value is found in a Tuple
# ? If there are multiple of the item you're looking for, it gives you the first 

print(first_tuple.index(2)) # prints 1

# * Nested Tuples
# ? Just like lists, you can nest tuples in tuples!

nested_tuple = (1, 2, (3, 4), 5, 6)
print(nested_tuple[2]) # prints (3, 4)
print(nested_tuple[2][0]) # prints 3

# ? Tossing in Slice

print(nested_tuple[0: 3]) # prints (1, 2, (3, 4))

# ? Tossing in Slice with a Step

print(nested_tuple[0: 3: 2]) # prints (1, (3, 4))

# ! VERDICT: Faster than lists, but not as flexible!