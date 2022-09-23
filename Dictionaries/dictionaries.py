
# * Dictionaries
# ? A data structure that consists of key-value pairs
# ? We use the keys to describe our data and the values to represent the data

# ? This is a Dictionary! Much like an OBJECT in JS


instructor = {
    "Name": "Pat",  # Left side = key, Right side = value
    "owns_cat": True,  # Keys and values separated by Colon
    "is_funny": False,  # Entries separated by commas
    3: "My Favorite Number!",
    "favorite_game": "No Mans Sky"
}

# * Built-in Dict Function
# ? Assign values to keys by passing in kets and values separated by an =

another_dictionary = dict(key='value')
print(another_dictionary)  # prints {'key': 'value'}

cat = dict(Name='Eorah', Evil=True, is_alive=True,)
print(cat['Name'])

# ? A LIST of DICTIONARIES
cart = [
    {
        'item': 'ball',
        'price': 100,
        'tax': .7
    },
    {
        'item': 'gameboy',
        'price': 5000,
        'tax': .7
    }
]
print(cart[0]['item'])
print(cart[1]['price'])


# * .values() method
# ? This will... you guessed it! Grab all the values in a given dictionary.

# ? This works for an individual dictionary
for attributes in cat.values():
    print(attributes)

# ? But what about a list of dictionaries?
for items in cart:
    for info in items.values():
        print(info)

# * .keys() method
# ? This will...you guessed it! Grab all of the keys in a given dictionary
for items in cart:
    for info in items.keys():
        print(info)

for attributes in cat.keys():
    print(attributes)

# * Grabbing both KEY and VALUE in the same loop using .items()

for k, v in cat.items():
    print(f'The key is {k}, and the value is {v}')

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5,
                  stan=150.0, lisa=50.25, harrison=10.0)
print(donations)

total_donations = 0
for donation in donations.values():
    total_donations += donation
    print(total_donations)


# * Check if a dictionary has a certain KEY

print('name' in cat) # prints FALSE because ... it's case sensitive!
print('Name' in cat) # This on the other hand ... prints TRUE!

# * Check if a dictionary has a certain VALUE

print('eorah' in cat.values()) # Again, prints FALSE. IT MUST BE EXACT.
print('Eorah' in cat.values()) # prints True

# ? The 'in' keyword is a lot like opening a book
# ? "Find the 'Name' of the 'cat' IN the cat dictionary"

# * Dictionary Methods!
# ? A means to manipulate dictionaries!

# * Clear
# ? Clear all the keys and values in a dictionary

d = dict(a=1, b=2, c=3)
d.clear()
print(d) # prints {} 

# * Copy
# ? Makes a copy of a dictionary

highscores = dict(Bozo=300, Bongo=666, Brad=420)
score_stealer = highscores.copy()
print(score_stealer)
print(highscores is score_stealer) # FALSE, while they look the same. They are stored in different memory spaces!
print(highscores == score_stealer) # TRUE, because they contain the same contents

# * fromkeys
# ? Creates Key-value pairs from comma separated by values
# ? Odd because it is called on an empty object {}

print({}.fromkeys('a', 'b')) # prints {'a': 'b'}

# ? Purpose? Usually a way to programmatically create default dictionaries

# ! Must be passed an array or list most of the time!
# ? This will generate a default user
new_user = {}.fromkeys(['name', 'score', 'email', 'profile bio'], 'unknown')
print(new_user)

# ? Can be used on an existing dictionary, but it will just generate a new dictionary 🤷

# * get
# ? Retrieves a key in an object and return None instead of a KeyError if the key does not exist

print(highscores.get('Bozo')) # prints 300

# * pop
# ? Takes a single argument corresponding to a key and removes that key-value pair
# ? from the dictionary. Returns the value corresponding to the key that was removed.

print(highscores.pop('Bozo'))

# * popitem
# ? Removes a RANDOM key in a dictionary

print(highscores.popitem())
print(highscores)

# * update
# ? Update keys and values in a dictionary with another set of key-value pairs

first = dict(a=1, b=2, c=3, d=4, e=5)
second = {}
second.update(first)
print(second)