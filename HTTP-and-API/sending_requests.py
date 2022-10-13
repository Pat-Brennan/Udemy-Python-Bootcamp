from wsgiref import headers
import requests

# * Requests MODULE!
# ? Lets us make HTTP requests from our python code!
# ? Installed using pip
# ? Useful for webscraping/crawling, grabbing data from other APIs etc.

url = 'https://www.nomanssky.com/'
response = requests.get(url)
print(response)

dad_url = "https://icanhazdadjoke.com/"
dad_response = requests.get(dad_url, headers={'Accept': 'text/plain'})
# ? text/plain makes it so you ONLY get the joke
# ! This is NOT the case for every website!

dad_response_json = requests.get(
    dad_url, headers={'Accept': 'application/json'})
data = dad_response_json.json()

print(dad_response.text)
print(data)
print(data['joke'])
