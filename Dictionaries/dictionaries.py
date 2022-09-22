
# * Dictionaries
# ? A data structure that consists of key-value pairs
# ? We use the keys to describe our data and the values to represent the data

# ? This is a Dictionary! Much like an OBJECT in JS
from tokenize import Name


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
