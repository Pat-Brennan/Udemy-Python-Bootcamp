
# * Iterators and Iterables!

# * Iterator
# ? An object that can be iterated upon. An object which returns data ->
# ? one element at a time when next() is called on it.

# * Iterable
# ? An object which will return an iterator when iter() is called on it.

# * next()
# ? When next() is called on an iterator, the iterator returns the next item.
# ? It keeps doing so until it raieses a Stopiteration error.

# * using the above ideas to make a custom for loop

name = "Big Chungus"

def my_for(iterable): # define my_for
  iterator = iter(iterable) # call iter() on what's passed in i.e "iterable"
  print(next(iterator)) # B , call next() to allow iter() to continue
  print(next(iterator)) # i
  print(next(iterator)) # g
  print(next(iterator)) # 
  print(next(iterator)) # C
  print(next(iterator)) # h
  print(next(iterator)) # u
  print(next(iterator)) # n
  print(next(iterator)) # g
  print(next(iterator)) # u
  print(next(iterator)) # s
  # print(next(iterator)) # Stop iteration error

my_for(name)

def better_my_for(iterable, func):
  iterator = iter(iterable)
  while True:
    try:
      thing = next(iterator)
    except StopIteration:
      print("Stop this confounded iterating!!!")
      break
    else:
      func(thing)

better_my_for("heyyy!", print)