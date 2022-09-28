
# * The Return Keyword!
# ? The OUTPUT side of functions
# ? It's how we get VALUES OUT of Functions!
# ? Exits the function
# ? Outputs whatever value is placed after the return keyword
# ? pops the function off of the 'call stack'

from asyncio import set_event_loop


def print_square_of_7():
    print(7**2)


print_square_of_7()  # prints 49

# ? Same as above with return keyword


def square_of_seven():
    print("HA HAAA! I AM BEFORE!")
    return 7**2
    # This line is faded out in VS Code, because it is AFTER the RETURN
    print("Fiddle sticks I'm too late!")
    # and therefore will not run!


result = square_of_seven()
print(result)

# ! The Return STOPS THE FUNCTION. ANYTHING AFTER IT WILL NOT RUN.
