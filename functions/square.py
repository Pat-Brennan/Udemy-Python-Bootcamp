
# * Function that accepts arguments!

def square (num): # accepts the INPUT of num
  return num ** 2 # and returns the OUTPUT of num squared!

print(square(2))
print(square(13))

def sing_happy_birthday (name):
  print('Happy Birthday to you!')
  print('Happy Birthday to you!')
  print(f'Happy Birthday dear {name}!')
  print('Happy Birthday to you!')

sing_happy_birthday('Zazzy')

# ? Parameters can be named whatever you want! (a, b) (this, that)
# ! Worth noting: parameters only exist inside of the function!

def add(a, b):
  return a + b

def multiply (first, second):
  return first * second 

def divide (this, that):
  return this / that

def your_name (first_name, last_name): # first_name and last_name are parameters
  return f'your full name is {first_name} {last_name}!'

print(your_name('ziggy', 'stardust')) # 'ziggy' and 'stardust' are arguments

# * Parameters vs Arguments
# ? A parameter is a VARIABLE in a METHOD DEFINITION (a, b)
# ? When a method is called, the ARGUMENTS are the DATA you pass into the METHODS PARAMETERS
# ? Parameter is variable in the declaration of function
# ? Argument is the actual value of this variable that gets passed to function

# ! Order of parameters does matter!