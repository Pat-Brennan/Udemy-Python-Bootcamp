
# * Function that accepts arguments!

def square(num):  # accepts the INPUT of num
    return num ** 2  # and returns the OUTPUT of num squared!


print(square(2))
print(square(13))


def sing_happy_birthday(name):
    print('Happy Birthday to you!')
    print('Happy Birthday to you!')
    print(f'Happy Birthday dear {name}!')
    print('Happy Birthday to you!')


sing_happy_birthday('Zazzy')

# ? Parameters can be named whatever you want! (a, b) (this, that)
# ! Worth noting: parameters only exist inside of the function!


def add(a, b):
    return a + b


def multiply(first, second):
    return first * second


def divide(this, that):
    return this / that


def your_name(first_name, last_name):  # first_name and last_name are parameters
    return f'your full name is {first_name} {last_name}!'


print(your_name('ziggy', 'stardust'))  # 'ziggy' and 'stardust' are arguments

# * Parameters vs Arguments
# ? A parameter is a VARIABLE in a METHOD DEFINITION (a, b)
# ? When a method is called, the ARGUMENTS are the DATA you pass into the METHODS PARAMETERS
# ? Parameter is variable in the declaration of function
# ? Argument is the actual value of this variable that gets passed to function

# ! Order of parameters does matter!

# * Default Parameters
# ? When no argument is passed to a given parameter
# ? It can be helpful for that parameter to have a DEFAULT value
# ? Syntax: parameter=default


def exponent(num, power=2):
    return num ** power


print(exponent(2))
print(exponent(3))
print(exponent(3, 6))

# * Why use Default Params(parameters)?
# ? Allows you to be more defensive
# ? Avoids errors with incorrect parameters
# ? More readable examples

# * What can default params be?
# ? Anything!
# ? Functions, lists, dictionaries, strings, booleans ... Anything!

# ? I'm passing the 'add()' function from earlier, to the math() function


def math(a, b, function=add):
    return function(a, b)


print(math(666, 420))  # 1089
print(math(666, 420, multiply))  # 279720
print(math(666, 420, divide))  # 1.58

# * Keyword Arguments
# ? As long as you know the param names, order will not matter!


def full_name(first, last):
    return f'{first} {last} is your name! Right?!'


# ? Both of these will print the same thing
print(full_name(first='JARVIS', last='MARVIS'))
print(full_name(last='JARVIS', first='MARVIS'))

# * Why use Keyword Arguments?
# ? Particularly useful when passing a dictionary to a function
# ? and unpacking it's values!

# ! KEYWORD ARGS ARE DIFFERENT FROM DEFAULT PARAMS
# ? When you define a function and use an = you are setting a default parameter
# ? When you invoke a function and use an = you are making a keyword arg
