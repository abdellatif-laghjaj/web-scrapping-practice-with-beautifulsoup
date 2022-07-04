from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

url = 'https://simplilearn.com/resources/'
webpage = urlopen(url)
soup = BeautifulSoup(webpage, 'html.parser')
webpage.close()


for h2 in soup.find_all('h2'):
    print(h2.text)

for img in soup.find_all('img'):
    print(img['src'])