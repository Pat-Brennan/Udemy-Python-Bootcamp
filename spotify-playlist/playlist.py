
# * Replicating a Spotify Playlist!

playlist = {
    'title': 'Rascals Ricks Big Time Playlist',
    'author': 'Rascal Rick',
    'songs': [
        {'artist': ['Rick James'], 'title': 'song 1', 'duration': 4.00},
        {'artist': ['Johnny Pizzazz', 'Ricky Martin'],
         'title': 'song 2', 'duration': 4.00},
        {'artist': ['Rick Sanchez'], 'title': 'song 3', 'duration': 4.00},
    ]
}
total_length = 0
for song in playlist['songs']:
    total_length += song['duration']
    print(song['title'])

print(total_length)
