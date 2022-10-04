
# * Map!
# ? A standard function that accepts at least two arguments,
# ? a function and an 'iterable.'
# ? Syntax: map(lambda parameter: expression, iterable)

# ? iterable - something that can be iterated over (lists, strings, dictionaries, sets, tuples)

# ? Runs the LAMBDA(Anonymous function) for each value in the iterable and returns a MAP OBJECT
# ? which can be converted into another data structure.

numbers = [1, 3, 5, 7, 9]

squared = map(lambda num: num * num, numbers)
print(squared) # ! This will print a MAP OBJECT (Not a list)

print(list(squared)) # ! The MAP OBJECT must be CONVERTED!

people = ['Garfield', 'Chubacca', 'Iron Maiden', 'Chuck E. Cheese']

peeps = map(lambda peep: peep.upper(), people)
print(list(peeps))

friends = [
  {'first' : 'Darkness my', 'last' : 'Oldfriend'},
  {'first' : 'The Hand', 'last' : 'that Feeds'},
  {'first' : 'The Chained', 'last' : 'One'}
] 

first_name = list(map(lambda x: x['first'] , friends))
print(first_name)