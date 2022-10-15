import requests
import random
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
    params={'term': f'{search_term}', 'limit': 1}
)

data = response.json()
# print(data)

print(f"Got it! I've got a {data['total_jokes']} jokes you might like.")
print(data['results'][0]['joke'])
