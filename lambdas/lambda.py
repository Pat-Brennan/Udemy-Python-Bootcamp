
# * Lambdas!
# ? Similar to anonymous functions in JavaScript
# ? Syntax: lambda parameter: expression
# ? Expression is automatically returned
# ! Can only be one line!

# ? lambdas are not usually saved to variables (forewarning)
square = lambda num: num * num
print(square(5))

add = lambda a,b: a + b
print(add(1, 6))

# ? Mostly used when passing a function to another function as an ARGUMENT
# ? Particularly when that function will never be used again

# ? Generally, Lambdas are not that common.

