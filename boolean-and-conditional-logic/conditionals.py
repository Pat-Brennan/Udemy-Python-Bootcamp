
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
