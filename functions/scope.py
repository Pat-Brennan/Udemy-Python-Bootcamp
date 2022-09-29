
# * Scope!
# ? How much your program can see and where
# ? Variables created in function are SCOPED in that function!

def say_hello():
    instructor = 'BONGO'  # instructor is SCOPED to 'say_hello'
    return f'hello {instructor}'

# ? 'instructor' cannot be accessed outside of 'say_hello'


print(say_hello())

# * Global Scope!
# ? Any variable defined outside of a function, is a global variable.
# ? These are not always a good idea!

# ? Functions will generally look for LOCAL VARIABLES,
# ? and throw errors if the are not found

# * Global Keyword
# ? The global keyword allows functions to reach outside of LOCAL SCOPE

total = 0


def increment():
    global total  # using global keyword to get total
    total += 1
    return total


print(increment())  # 1

# ? This mainly pertains to variables that you are trying to MANIPULATE

# * Nonlocal Keyword
# ? How to grab variables within declared in functions inside of functions


def outer():
    count = 0  # count is in outer scope

    def inner():
        nonlocal count  # count is made available within inner due to nonlocal keyword
        count += 1  # count is manipulated
        return count  # we get count back
    return inner()  # we get inner that contains count


print(outer())  # we get outer that contains inner that contains count.

# ! Global and Nonlocal are not that common!
