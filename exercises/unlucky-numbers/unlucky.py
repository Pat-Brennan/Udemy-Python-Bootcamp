
# * Unlucky Numbers!

# ? loop through 1 - 20 and determine what is unlucky!

# 4 and 13 should print "x is unlucky"

# for num in range(1, 21):
#     if num == 4 or num == 13:
#         print(f'{num} is unlucky!')
#     elif num % 2 == 0:
#         print(f'{num} is even')
#     else:
#         print(f'{num} is odd')

# ? Same as above, just written a different way! 

for num in range(1, 21):
    if num == 4 or num == 13:
        state = "unlucky"
    elif num % 2 == 0:
        state = "even"
    else:
      state = "odd"
    print(f'{num} is {state}')
