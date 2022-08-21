
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

print('What\'s your favorite color?') # Use of escape characters
color = input()

if color == 'Black' or 'black': # Use of OR boolean Operator
  print('That would be correct!')
elif color == 'Red' or 'red':
  print('That would also be correct!')
elif color == 'Turquoise' or 'turquoise':
  print('What are you some kind of Turtle??')
elif color == 'Yellow' or 'yellow':
  print('Are you aware that can make babies cry?')
else:
  print('I can\'t believe what I am hearing!')