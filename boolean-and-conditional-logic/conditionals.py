
# * Conditional logic!
# ? Conditional logic using if statements represents different paths a
# ? Progrram can take based on some type of comparison of input

print('Who is it you seek?')
print('')
print('1. Arya Stark')
print('2. Jon Snow')

option1 = '1'
option2 = '2'

name = input()

if name == option1:
    print('Valar Morgulis')
elif name == option2:
    print('You know NOTHING!')
else:
    print('Well... Carry on then!')

# ! INDENTATION MATTERS! IT'S HOW PYTHON TELLS WHAT'S RELATED TO WHAT!

# * Multiple elif Example

print('What\'s your favorite color?')  # Use of escape characters
color = input()

if color == 'Black' or 'black':  # Use of OR boolean Operator
    print('That would be correct!')
elif color == 'Red' or 'red':
    print('That would also be correct!')
elif color == 'Turquoise' or 'turquoise':
    print('What are you some kind of Turtle??')
elif color == 'Yellow' or 'yellow':
    print('Are you aware that can make babies cry?')
else:
    print('I can\'t believe what I am hearing!')

# * Truthiness and Falsiness
# ? In Python, all conditiional checks resolve to TRUE or FALSE
# ? We call values that resolve to true... truthy
# ? and values that resolve to false... falsy

# ? Generally, 1 is True, and 0 is False

x = 1
x is 1  # true : The IS keyword works very similarly to double equals
x is 0  # false

# ? Besides conditional checks, other things that are naturally
# ? falsy include: empty objects, empty strings, None, and zero.

print('What is your favorite animal?')
animal = input()

if animal:  # if the string is empty i.e no input. It will evaluate to falsy
    print(f'{animal} is your favorite animal!')
else:
    print('YOU SAID NOTHING OF ANIMALS!')  # and print this instead.


# * Logical Operators!
# ? In Python, the following operators can be used to make boolean logic
# ? comparisons or statements...and, or, and not

# ? and - if a and b:
# ? or - if a or b:
# ? not - if not a:

# * AND Example
print('How old are you?')
age = int(input())

if age < 2:
    print('You\'re a baby!')
elif age >= 2 and age <= 8:
    print('You\'re a child!')
elif age >= 9 and age <= 18:
    print('you\'re a teen!')
else:
    print('congrats you are adult!')

# * NOT Example
# if not age >= 2 and <= 8 or age > 65:
#   print('You pay the adult price!')
# else:
#   print('you are a child or senior!') 

# * OR Example
print('Where do you live?')
city = input()

if city == 'Los Angelos' or city == 'San Francisco':
    print('You live in California!')
else:
    print('You can\'t hide from me!!!')

# * is vs. ==
# ? In python, == and 'is' are very similar, not the same.
# ? == will check if the VALUES are the same
# ? IS will check if they have the same VALUES are STORED in the same place

a = 1
a == 1 # True
a is 1 # True

a = [1, 2, 3]
b = [1, 2, 3]
a == b # True : They have the same VALUES
a is b # False : They have the same VALUES but are not STORED in the same place

c = b # We make a new variable called 'c', and have it point to the same memory space as b
b is c # True

# ? 'is' is only truthy if the variables reference the same item in memory