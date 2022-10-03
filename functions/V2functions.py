
# * Even more Functions!

# * '* args'
# ? A special operator we can pass to functions
# ? Gather remaining arguments as a TUPLE.
# ! This is just a parameter! - YOU CAN CALL IT WHATEVER YOU WANT!

# * * Args Example

# ? This ca get kind of clunky!
def sum_all_nums(num1, num2, num3):
  return num1 + num2 + num3

print(sum_all_nums(1, 2, 3))

# ? Same as above but with *args

def v2sum_all_nums(*args):
  total= 0
  for num in args:# we only use the '*' when referring to the parameter
    total += num
  return total

print(v2sum_all_nums(1, 2 ,3))
print(v2sum_all_nums(1, 2 , 3, 4, 5, 6, 6, 6))

def ensure_correct_info (*creds): # Again, DOES NOT NEED TO BE ARGS
  if "Pat" in creds and "Brennan" in creds:
    return "Hey I know you!"
  return "Wait a sec, I don't know you!!!" # Else not needed here

print(ensure_correct_info("Pat", "Brennan"))
print(ensure_correct_info("Kevin", "Seagull"))


# * '** Kwargs'
# ? Uses Two stars, and is pronounced 'QWARGS'
# ? The 'kw' stands for 'Key Word'
# ? A Special operator that we can pass to functions
# ? Gathers remaining KEYWORD ARGUMENTS as a DICTIIONARY
# ! This is just a parameter - you can call it whatever you want! 

def fav_colors (**kwargs):
  for person, color in kwargs.items():
    print(f"{person}'s favorite color is {color}")

fav_colors(taylor='Blue', jonah='purple', kevin='green')