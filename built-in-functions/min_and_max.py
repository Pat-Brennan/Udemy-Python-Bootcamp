
# * Max!
# ? Return the largest item in an iterable or the largest of two or more arguments!

# ? Largest in a list of nums
from turtle import title


nums = [123, 324, 345, 567, 321]
print(max(nums))

# ? Largest in a String
print(max('West World'))

# * Min!
# ? Return the smallest item in an iterable or smallest of two or more arguments!

print(min(nums))
print(min('West World')) # In this case the space is the smallest

names = ['Ronald', 'McDonald', 'Hamburglar', 'Bigbird', 'Trashcan Sam']

longest_name = max(names, key=lambda name: len(name))
print(longest_name)

shortest_name = min(names, key=lambda n: len(n))
print(shortest_name)

# * Spotify Filter Example

songs = [
  {'title': 'Backpocket', 'playcount': 1000 },
  {'title': 'Monster Mash', 'playcount': 666},
  {'title': 'Jabbas night out', 'playcount': 12345},
  {'title': 'Thriller', 'playcount': 3000},
  {'title': 'Tubthumpin', 'playcount': 420},
]

longest_title = max(songs, key=lambda t: t['title'])
print(longest_title)

least_played = min(songs, key=lambda s: s['playcount'])
print(least_played)