
# * The Mysterious __name__

# ? When run, every python file has a __name__ variable
# ? If the file is the main file being run, its value is "__main__"

def say_hi():
    print(f'Hi! my name is {__name__}')  # __main__


say_hi()
