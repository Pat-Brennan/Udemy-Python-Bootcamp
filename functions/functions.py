
# * Functions!

# * What is a function?
# ? A process for executing a task.
# ? A Little bundle of code for us to recall at any point
# ? It can accept input and return an output
# ? Useful for executing similar procesures over and over and over again

colors = ['red', 'orange', 'yellow', 'blue', 'indigo']
colors.append('violet')
print(colors)

# * Why use functions?
# ? Stay DRY! ☀️🌻😎
# ? D - Don't, R - Repeat, Y - Yourself
# ! Not WET! 💦🤽🌊
# ! W - Write, E - Everything, T - Twice

# ? Clean up and prevent code duplication
# ? "Abstract away" code for other users
# ? + Imagine, you had to rewrite the print() function everytime... wouldn't that suck?

# * Function Structure!
# ? Syntax: def name_of_function ():
# ?             block of runnable code here

# ? We are now using the 'def' keyword!

def say_hi():
  print('Well Howdy!')

say_hi()

def happy_birthday():
  print('Happy birthday to you!')
  print('Happy birthday to you!')
  print('Happy birthday dearest yoooouuu!')
  print('Happy birthday to you!')
  
happy_birthday() # The parens are key! The parens are 'calling' the function!
