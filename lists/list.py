
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

colors = ['red', 'blue', 'yellow']
best_color = colors[0] # accesses index 0 and saves to variable best_color
print(best_color) # prints red