
# * Lists!

# ? A collection or grouping of items!
# ? This could be a variety of data types! 
# ? Also known as an ARRAY in other languages!
# ? A fundamental data structure for organizing data!
# ? Defined by []

# item1 = 'Bananas'
# item2 = 'Potatoes'
# This will get clunky FAST! If only there was a way...

from itertools import count
from pickle import TRUE


demo_list = [1, "potato", True]

len(demo_list) # this will find the LENGTH of the list

# * Built-in List Function

r = range(0, 666)
list(r) # this will turn 'r' into a LIST, just like str() turns things into strings

# * Accessing Values in a List

# ? Like ranges, lists ALWAYS start counting at zero. So the first ELEMENT is index 0

colors = ['red', 'blue', 'yellow', 8 , True, 6.66]
best_color = colors[0] # accesses index 0 and saves to variable best_color
print(best_color) # prints red

# ? Negative indexing grabs the end of the list instead of the beginning
print(colors[-1]) # prints yellow

# ? Check if a value is IN a list
# ! HAS TO MATCH EXACTLY(Capitalization matters)

print('red' in colors) # prints True
print('purple' in colors) # prints False

if 'blue' in colors:
  print('You have great taste!')
  
# * Using Loops with Lists

# ? For Loop

for color in colors: # Grabs each index in the list 'colors'
  print(color) # and prints them! 
  
numbers = [1,2,3,4,5,6,6,6,16,16,16]

for num in numbers:
  print(num * num)
  
# ? While Loop

i = 0 # To avoid an infinite loop we must set a counter
while i < len(colors): # check length of colors list and compare to i
  print(colors[i])
  i += 1 # Add to i to eventually stop the loop
  
# * Methods and functions are not necessarily the same

len(numbers) # len is a built-in function

numbers.append(666) # ? APPEND is a METHOD
print(numbers)

# ? METHODS are indicated by the .
# ? and don't necessarily need to be attached to variables

['this', 'is', 'just', 'a'].append('list')

# * List Methods

# ? Append: add an item to the end of the list
# ! Append can only take ONE argument!

count_down = [3, 2, 1]
count_down.append('GO!')
print(count_down) # prints 3, 2, 1, GO

# ? Extend: add the the end of a list all values passed to extend
# ? Even though we're passing count_down a LIST, each item will be added INDIVIDUALLY!

count_down.extend(['Your', 'life', 'depends', 'on', 'it!!!'])
print(count_down)

# ? Insert: Insert an item at a given position
# ? .insert(arg1: WHERE to insert, arg2: WHAT to insert)

count_down.insert(2, 'Where was I again? Oh right...')
print(count_down)

# ? Clear: Remove all items from the list

animals = ['bear', 'koala', 'pikachu']
animals.clear()
print(animals) # prints []

# ? Pop: Remove the item at the given position in the list, and return it.
# ? If no index is specified, removes and returns the last item in the list.

pokemon = ['Lycanroc', 'eevee', 'charizard']
pokemon.pop() # removes charizard
print(pokemon)
pokemon.pop(1) # removes eevee
print(pokemon) 

# ! The item that gets popped is not erased!
stray_pokemon = pokemon.pop()
print(stray_pokemon)

# ? Remove: Remove the first item from the list whose value is x (whatever x might be)\
# ? Throws a VALUE ERROR if the item is not found.

food = ['salsa', 'chips', 'tacos', 'chips']
food.remove('chips') # finds the FIRST instance of chips, and removes it!
print(food)

# ? Index: returns the index of the specified item in the list

cereal = ['capn crunch', 'count chocula', 'fruity pebbles', 'capn crunch']
print(cereal.index('count chocula')) # prints 1
print(cereal.index('capn crunch', 1)) # arg1: What to find, arg2: a starting point

# ? Count: return the number of times x appears in the list

beast_number = [6, 6, 6, 4, 2, 0, 16, 16, 16, 13, 7]
print(beast_number.count(6)) # prints 3

# ? Reverse: Reverse the elements of the list(in-place)
# ? Edits the ORIGINAL LIST does NOT make a copy

beast_number.reverse()
print(beast_number)

# ? Sort: sort the items of the list(in-place)
beast_number.sort()
print(beast_number)

# ? Join: technically a STRING METHOD that takes an iterable argument 
# ? Concatenates a copy of the base string  between each item of the iterable
# ? returns a new string
# ? Can be used to make sentences out of a list of words by joining on a space

words = ['Welllll', 'hello', 'there!']
print(' '.join(words))

# ? Slice: Slice into an old list, and make a new list from what you sliced!
# ? Syntax: some_list[start:end:step] The colons are important!
# ? arg1: where to start, arg2: where to end, arg3: what interval to move by
# ? The end point is NOT INCLUSIVE (similar to range)

print(beast_number[3:6:1]) # prints [6, 6, 6]

# ? You can also NEGATIVE INDEX this!
print(cereal[-2:]) # Prints [Fruity pebbles, Capn Crunch]

# * Tricks with Slices!

# ? reversing lists/strings

string = "This is fun!"
print(string[::-1]) # reverses whole string

# ? Modifying portions of lists

numbers = [1, 2, 3 ,4 , 5]
numbers[1:3] = ['a', 'b', 'c'] # removes 2, 3, 4, and replaces with a, b, c
print(numbers)

# ? Chain them together to grab a piece of list, then manipulate it

print(cereal[1][::-1]) # reverses the string at index of 1 in the list 'cereal'

# * How to swap things in a list 
# ? Uses the comma syntax to separate the items 

card_hand = ['queen', 8, 'jack', 'ace']

card_hand[0], card_hand[3] = card_hand[3], card_hand[0]

print(card_hand)

# * List Comprehension
# ? Syntax: [ __ for __ in __ ]
# ? arg1: What should happen, arg2: what it will happen to, arg3: Where to find the things(in this case a list)
# [x*10 for x in numbers]
# multiply by 10 for each entry within the list numbers

# ? Same as above, but with a for loop

doubled_numbers = []
for num in numbers:
  doubled_number = num * 2
  doubled_numbers.append(doubled_number)
  
print(doubled_numbers)

# ? List Comprehension allows us to do the above... but in a single line

doubled_numbers2 = [num * 2 for num in numbers] # BAM!

print(doubled_numbers2)

cat = 'Eorah'
print([char.upper() for char in cat]) 
# Loops over Cat nad uppercases each letter and creates a new list

friends = ['Jonald', 'Bengy', 'Gerber']
print([char[0].upper() for char in friends])

print([bool(val) for val in ['', [], 0]])

print([[str(count) for count in count_down]])