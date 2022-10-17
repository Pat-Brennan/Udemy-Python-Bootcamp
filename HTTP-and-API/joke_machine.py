import requests
from random import choice
import pyfiglet
from termcolor import colored

title = pyfiglet.figlet_format('DAD JOKE 3000', font='slant')
colored_title = colored(f"{title}", 'red')
print(colored_title)

url = 'https://icanhazdadjoke.com/search'

search_term = input('What would you like to search? ')

response = requests.get(
    url,
    headers={'Accept': 'application/json'},
    params={'term': {search_term}, 'limit': 1}
)

data = response.json()
# print(data)

num_jokes = data["total_jokes"]
results = data["results"]
if num_jokes > 1:
    print(f"Got it! I've got {num_jokes} jokes you might like.")
    print(choice(results)['joke'])
elif num_jokes == 1:
    print("Woah! I have exactly 1 joke for that! Congrats!")
    print(results[0]['joke'])
else:
    print(f'There are no Jokes for {search_term}! Come again!')
