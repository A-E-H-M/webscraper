import requests
from bs4 import BeautifulSoup

response_object = requests.get('https://www.nwf.org/Educational-Resources/Wildlife-Guide/Invertebrates/Bees')

soup_object = BeautifulSoup(response_object.text, 'html.parser')

divs = soup_object.find_all('div', {'class': 'bordered-container'})

for div in divs:
    print(div)

