
# * All!
# ? Return True if all elements of the iterable are truthy (or if the iterable is empty)

names = ['Derek', 'Darren', 'Dorkel', 'Darius']

d_names = all([name[0] == "D" for name in names])

print(d_names) # True, because all names start with D

# * Any!
# ? Return True if ANY element of the iterable is truthy.
# ? If the iterable is empty, return False

nums = [0, 1, 2, 3, 4, 5]

evens = any([num % 2 == 0 for num in nums])
print(evens) # True

odds = any([num % 2 == 1 for num in nums])
print(odds) # Also True