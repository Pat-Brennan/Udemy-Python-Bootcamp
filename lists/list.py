
# * Lists!

# ? A collection or grouping of items!
# ? This could be a variety of data types! 
# ? Also known as an ARRAY in other languages!
# ? A fundamental data structure for organizing data!
# ? Defined by []

# item1 = 'Bananas'
# item2 = 'Potatoes'
# This will get clunky FAST! If only there was a way...

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