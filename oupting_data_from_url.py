from bs4 import BeautifulSoup
import requests

url = 'https://simplilearn.com/'
result = requests.get(url)

page_content = result.content
print(page_content)