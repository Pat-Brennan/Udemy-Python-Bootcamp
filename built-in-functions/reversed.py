
# * Reversed!
# ? Return a reversed iterator
# ? Best when you specifically want to iterate over something in reverse
# ! This is different from REVERSE, the LIST METHOD

# ? Reversing a string with this
print(''.join(list(reversed("Hello There!"))))

nums = [1, 2, 3, 4]
print(reversed(nums)) # prints list_reverseiterator_object
print(list(reversed(nums))) # prints [4,3,2,1]

