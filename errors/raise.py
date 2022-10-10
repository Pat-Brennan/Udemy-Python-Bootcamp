
# * Raise!
# ? In Python we can also THROW errors using the raise keyword.
# ? This is helpful when creating your own kinds of exceptions and error messages.

# raise ValueError('invalid value')

# ! In other languages, this would usually be called 'throw'

def colorize(text, color):
  colors = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo')
  if type(text) is not str:
    raise TypeError('Text must be a String!')
  elif color not in colors:
    raise ValueError('That color is not an option!')
  print(f'Printed {text} is {color}')
  
# colorize(666, "red")
colorize('Woah Nelly', 'purple')