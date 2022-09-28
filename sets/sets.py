
# * Sets!
# ? A Collection of data that DOES NOT have DUPLICATE VALUES.
# ? Similar to duples in that that they are faster than Dictionaries and Lists
# ? Elements in sets DO NOT HAVE AN ORDER
# ? This means that we CANNOT ACCESS THINGS BY INDEX

# * Why would we use this?
# ? Sets can be useful if you need to keep track of a collection of
# ? elements, but don't care about ordering, keys or values and duplicates.

# ? Syntax : x = {insert, elements, here}
# ? Looks like a dictionary, but you don't use colons to create key-value pairs

import math


set_with_duplicates = ({1, 2, 3, 4, 5, 5, 5})  # Sets cannot have duplicates

first_set = ({1, 4, 5})

s = {1, 4, 5}  # same as above

4 in s  # True
8 in s  # False

# ? There is no order, and not totally sure what's governing order in the first place...

# * Looping through Sets
# ? Also basically works like a list!

for thing in s:
    print(thing)

# * Removing duplicates from a LIST with a SET

cities = ['Philly', 'New York City', 'Balitmore', 'Chicago', 'Philly']
print(list(set(cities)))
# ? The LIST is turned into a SET (removing duplicates)
# ? and then turned BACK INTO A LIST and printed to the console

# * Set Methods!

# * .add()
# ? Adds an element to a set.
# ? If the element is already in the set, the set doesn't change!

s.add(2)
print(s)

s.add(2)  # This will not throw an error
print(s)  # but it WILL NOT add another 2 to the set

# * .remove()
# ? removes a value from the set
# ? returns a KeyError if the value is not found

s.remove(5)
print(s)

# s.remove(8) results in a KeyError
# print(s)

# ? .discard() can be used in place of .remove(), but
# ? you will not get an informal error message!

# * .copy()
# ? Creates a copy of the set!

another_s = s.copy()
print(another_s)

# ? while they have the info, they are not stored in the same place in memory

# * .clear()
# ? Removes all the contents of the set

s.clear()
print(s)  # prints set()

# * Set Math!
# ? Some methods are intersection, symmetric_difference, and union!

math_students = {'Eorah', 'Jack', 'Addy', 'Dixie', 'Ruby'}
bio_students = {'Eorah', 'Jack', 'Bongo', 'Ruby', 'Bird'}

# * Union |
# ? Combines the sets ignoring duplicates
# ? uses the ' | '

print(math_students | bio_students)

# * Intersection &
# ? Specifically points out the duplicates between sets

print(math_students & bio_students)


# * Set Comprehension
# ? Works similarly to Dictionary Comprehension
# ? Syntactically, you do not specify a key:value pair (becuase it's not a dictionary)

# ? Set Comprehension Example
print({x**2 for x in range(10)})

# ? Same as above, but as a Dictionary Comprehension
print({x: x**2 for x in range(10)})
