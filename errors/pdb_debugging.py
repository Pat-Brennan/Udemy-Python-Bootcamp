import pdb

# * PDB! (Python Debugger)
# ? To set breakpoints in our code we can use pdb by inserting this line:
# ? import pdb; pdb.set_trace()

first = 'first'
second = 'second'
pdb.set_trace()
result = first + second
third = 'Third'
result += third
print(result)

# * PDB Command List
# ? l (list)
# ? n (next line)
# ? p (print)
# ? c (continue - finishes debugging)

# ! This is not something that is usually kept in the code!

# * PDB on one line

# def add(a, b, c, d):
#   import pdb; pdb.set_trace()
  
#   return a + b + c + d 