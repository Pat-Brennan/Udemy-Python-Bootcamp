import requests

# * Query Strings!
# ? A way to pass data to the serer as part of a GET request
# ? Example: https://www.website.com/?key1=value1&key2=value2
# ? The '?' is the beginning of the query, followed by key-value pairs

url = 'https://icanhazdadjoke.com/search'

response = requests.get(
    url,
    headers={'Accept': 'application/json'},
    params={'term': 'cat', 'limit': 1}
)

data = response.json()

print(data['results'])

# print(data['joke'])
# print(f"status: {data['status']}")
