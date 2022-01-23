import requests

response_object = requests.get('https://www.nwf.org/Educational-Resources/Wildlife-Guide/Invertebrates/Bees')

print(response_object.text)
