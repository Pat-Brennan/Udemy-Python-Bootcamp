
# * Abs!
# ? Return the absolute value of a number.
# ? The argument may be an integer or a floating point number.
# ? The magnitude of a real number without regard to its sign.

print(abs(-5))  # 5
print(abs(5))  # 5

print(abs(-6.66))  # 6.66
print(abs(6.66))  # 6.66

# * Sum!
# ? Takes an iterable and an optional start
# ? returns the sum of start and the items of an iterable from left to right
# ? and returns the total

nums = [1, 2, 3, 4]

print(sum(nums))  # 10
print(sum(nums, 2))  # 12, Started with 2, and then summed everything up

# * Round!
# ? return number rounded to ndigits precision after the decimal point.
# ? If ndigits is omitted or is None, it returns the nearest integer to its input.

print(round(6.66))  # 7

'''
sum_even_values(1,2,3,4,5,6) # 12
sum_even_values(4,2,1,10) # 16
sum_even_values(1) # 0
'''

# define sum_even_values


def sum_even_values(*values):
    evens = [val for val in values if val % 2 == 0]
    return sum(evens)


print(sum_even_values(1, 2, 3, 4, 5, 6))
