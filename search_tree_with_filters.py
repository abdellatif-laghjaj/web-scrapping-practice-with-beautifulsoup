from bs4 import BeautifulSoup

#import the web scrapping example html file
HTML_FILE_PATH = 'examples\example_1.html'

with open(HTML_FILE_PATH, "r") as f:
    soup = BeautifulSoup(f, "html.parser")

#view the contents of the soup object
# print(soup.contents)

#search using the find() method
print(soup.find('p'))

#search the document using the find method for ID
print(soup.find(id = 'h1'))

#search using string only
search_for_string_only = soup.findAll('p', string = 'My first paragraph.')