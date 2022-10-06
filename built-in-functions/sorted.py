
# * Sorted!
# ! Different than SORT! Sort is a LIST METHOD!
# ? Syntax: sorted(works on anything that is iterable)

# ? Returns a new sorted list from the items in iterable

numbers = [666, 420, 6969, 3000]

# ? Lowest to highest
print(sorted(numbers))

# ? Highest to Lowest
print(sorted(numbers, reverse=True))

# ? Using a Tuple instead of list
print(sorted((432,765,321,543,6754,876)))

# * Twitter Example for Sorting

users = [
    {'username': 'A1hunk', 'tweets': ["I'm hunkalicious!"]},
    {'username': 'Bill_murry', 'tweets': []},
    {'username': 'Jaba49ers', 'tweets': ["Look!", "It's the Jaba!"]},
    {'username': 'Shadow_fall_69', 'tweets': ["I'm going down!"]},
    {'username': 'eeeeee', 'tweets': ['eeeee', 'eeee', 'eeeeeeeee']}
]
print(users)
print(sorted(users, key=lambda user: user['username']))

songs = [
  {'title': 'Backpocket', 'playcount': 1000 },
  {'title': 'Monster Mash', 'playcount': 666},
  {'title': 'Jabbas night out', 'playcount': 12345},
  {'title': 'Thriller', 'playcount': 3000},
  {'title': 'Tubthumpin', 'playcount': 420},
]

s_songs = sorted(songs, key=lambda song: song['playcount'], reverse=True)
print(s_songs)