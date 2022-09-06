
# * Loops!
# ? A means to perform the same operation over and over again!

# * for Loops!

# ? Syntax:
# for item in iterable_object:
#   Do Something with item!


# ? Iterable Object: some kind of collection of items,
# ? for instance: a LIST of numbers, a STRING of characters, a range, etc.

# ? "item" is a new variable that can be called whatever you want

# ? "item" references the current position of our ITERATOR(item) within the ITERABLE(iterable_object)
# ? It will iterate over every item of the colleciton, and go away when it has visited all items.

greeting = 'Hello!'

for char in greeting:
    print(char * 10)  # Characters are multiplied!

for x in range(0, 5):
    print(x)  # Will print 5 numbers... but not including 5

# * Ranges!
# ? Mostly used in for loops to determine length of loop

# range(7) : Gives you 0 - 6
# range(1, 8) : Gives you 1 - 7
# range(1, 10, 2) Gives you odds from 1 - 10 (increments by 2)
# range(7, 0, -1) Gives you 6 - 0 because -1 increments DOWN by 1
