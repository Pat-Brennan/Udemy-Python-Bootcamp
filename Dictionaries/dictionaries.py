
# * Dictionaries 
# ? A data structure that consists of key-value pairs
# ? We use the keys to describe our data and the values to represent the data

# ? This is a Dictionary! Much like an OBJECT in JS
instructor = {
  "Name": "Pat", # Left side = key, Right side = value
  "owns_cat": True, # Keys and values separated by Colon
  "is_funny": False, # Entries separated by commas
  3: "My Favorite Number!",
  "favorite_game": "No Mans Sky"
}

# * Built-in Dict Function
# ? Assign values to keys by passing in kets and values separated by an =

another_dictionary = dict(key = 'value')
print(another_dictionary) # prints {'key': 'value'}

cat = dict(Cat='Eorah', Evil=True)
print(cat)

# ? A LIST of DICTIONARIES
cart = [
  {
    'item':'ball',
    'price': 100,
    'tax': .7
},
  {
    'item':'gameboy',
    'price': 5000,
    'tax': .7
  }
]

print(cart)