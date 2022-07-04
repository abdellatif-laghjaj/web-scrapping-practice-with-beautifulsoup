from bs4 import BeautifulSoup
import requests

url = 'https://simplilearn.com/'
result = requests.get(url)

page_content = result.content

soup = BeautifulSoup(page_content, 'html.parser')
soup.contents

#prettify the html
print(soup.prettify())
