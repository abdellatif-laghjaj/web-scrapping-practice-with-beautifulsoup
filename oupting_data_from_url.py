from bs4 import BeautifulSoup
import requests

url = 'https://simplilearn.com/'
result = requests.get(url)

web_page = result.content

soup = BeautifulSoup(web_page, 'html.parser')
result.close()

for link in soup.find_all('a'):
    print(link.get('href'))