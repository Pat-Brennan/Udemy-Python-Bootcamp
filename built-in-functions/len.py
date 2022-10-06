
# * Len!
# ? Return the length (the number of items) of an Object.
# ? The Argument may be a sequence (such as a string, tuple, list, or range)
# ? or a collection (such as a dictionary, set)

# ? When we use len(), it's actually calling .__len__() behind the scenes

# ? Using Len
nums = [1, 2, 3, 4, 5]
print(len(nums))

# ? Using Dunder
print(nums.__len__())