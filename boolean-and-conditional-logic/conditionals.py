
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

if animal: # if the string is empty i.e no input. It will evaluate to falsy
    print(f'{animal} is your favorite animal!')
else:
    print('YOU SAID NOTHING OF ANIMALS!') # and print this instead.
