from bs4 import BeautifulSoup

#import the web scrapping example html file
HTML_FILE_PATH = 'examples\example_1.html'

with open(HTML_FILE_PATH, "r") as f:
    soup = BeautifulSoup(f, "html.parser")

#view the contents of the soup object
print(soup.prettify())