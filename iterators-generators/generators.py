
# * Generators!
# ? Generators are Iterators
# ? Generators can be created with generator functions
# ? Generator functions use the YIELD keyword
# ? Generators can be created with generator expressions

# *  Generator Functions (compared to functions)
# ? uses YIELD (uses return)
# ? can YIELD multiple times (returns once)
# ? When invoked, returns a generator (returns the return value)


def week():
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    for day in days:
        yield day


def yes_or_no():
    response = 'yes'
    while True:
        yield response
        response = 'no' if response == 'yes' else 'yes'
