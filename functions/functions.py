
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


happy_birthday()  # The parens are key! The parens are 'calling' the function!

# * Common mistakes when using the return keyword

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ? Leaving the return INSIDE OF THE FOR LOOP


def sum_odd_numbers():
    total = 0
    for number in numbers:
        if number % 2 != 0:
            total += number
    # here, the return is OUTDENTED (so it is not inside of the for loop)
    return total


print(sum_odd_numbers())

# ? When returning boolean values, the 'else' is not necessary


def is_odd_number(num):
    if num % 2 != 0:
        return True
    return False

print(is_odd_number(3))  # True
print(is_odd_number(2))  # False

