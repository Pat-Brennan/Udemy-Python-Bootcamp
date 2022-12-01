
# * Using fibonacci sequence with generators

# ? Stores all numbers in a list 
def fib_list(max):
  nums = []
  a, b = 0, 1
  while len(nums) < max:
    nums.append(b)
    a, b = b, a+b
  return nums

print(fib_list(10))

# ? Same as above but uses significantly less memory
def fib_gen(max):
  x = 0
  y = 1
  count = 0
  while count < max:
    x, y = y, x + y
    yield x
    count += 1
    
for n in fib_gen(1000000):
  print(n)