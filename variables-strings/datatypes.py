
# * Data Types!
# ? bool : True or false
# ? int : an integer (1, 2, 3)
# ? str : a string. A sequence of unicode characters in ""
# ? list : an ordered sequence of values of other data types [1, 2, 3]
# ? dict : A dictionary. A collection of Key:values pairs {"first_name":"Jerry"}


from operator import not_


game_over = False  # Bool

i_am_number = 666  # int

i_am_string = "I'm mr.meeseeks look at me!!!"  # string

i_am_list = [0, "Hey you!", "stop that!", 4, 5, True]  # list

i_am_dictionary = {"Animal": "Froggo", "Food": "Flies",
                   "Hometown": "Pondville"}  # dictionary

# * Dynamic Typing
# ? The ability to reassign variables to different types readily

awesomeness = True
print(awesomeness)

awesomeness = "A meow meow!"
print(awesomeness)

awesomeness = None  # literally means nothing
print(awesomeness)

awesomeness = 22 / 7
print(awesomeness)

# * Static Typing
# ? The inability to reassign variables to different types(C++ for example)

# int not_awesomeness = 5
# not_awesomeness = "Great!"  this would throw an error

# * None
# ? This is Pythons version of NULL

person = {
    'Name': 'Roger',
    'Age': 'Over a thousand',
    'Children': None,
    'Is_alive': True
}
print(person)

# * Declaring Strings
# ? Using single or double quotes is perfectly fine!(but be consistant)

name = "Bingo"
other_name = 'Bango'

# ? Using quotes inside of quotes is fine, but must be one or the other!

quote_example = "I said 'Hey! What a wonderful kind of day'"

# * String Escape Characters
# ? In Python, there are also 'escape characters', which are 'metacharacters'
# ? They get interpretted by python to do something special...
# ? and the all start with \

# ? \n : Makes a new line for string information to be placed

new_line = 'Hi \n There \n Bongo!'
print(new_line)

# ? \\ : used if you don't want to mix and match single versus double quotes

string = "He done told me \"Takeyourwaterballoonselsewhere!\""
print(string)

# * String Concatentation
# ? Combining multiple strings together.
# ? In Python, you can do this simply with a + operator

first_part = "WOah Nelly!"
second_part = "Hold your horse!"
put_together = first_part + ' ' + second_part
print(put_together)

# ? you can also use the += operator!

dino = "Tyranosaurus "
dino += "Rex"
print(dino)
