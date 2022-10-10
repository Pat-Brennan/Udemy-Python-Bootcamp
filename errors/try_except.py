
# * Error handling!

# ? In python, it is strongly encouraged to use try/except blocks,
# ? to catch exceptions when we can do something about them.
# ! This is very similar to try/catch in JS!

# ? Syntax:
# try:
#   foobar
# except:
#   print("WE GOT A PROBLEM!")

# * Why not catch them all?
# ? What we are doing here is catching EVERY error,
# ? which means we are not able to correctly identify "what" went wrong.
# ! It is highly discouraged to do this!

# * Try/Except Example:

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None


d = {'name': 'Rickster'}
print(get(d, 'name'))  # Rickster
print(get(d, 'city'))  # None

# * Else and Finally!
# ? Else will run when EXCEPT DOES NOT
# ? Finally will run NO MATTER WHAT
# ! You do not need these for Try and Except to work
while True:
  try:
      num = int(input('Please, Enter a number: '))
  except:
      print('Hey! Thats not a number!')
  else:
      print("I'm in the else! You did it!")
      break
  finally: # not common
      print("Runs no matter what!")
print("REST OF GAME LOGIC HERE")