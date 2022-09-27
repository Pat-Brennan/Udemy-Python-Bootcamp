
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