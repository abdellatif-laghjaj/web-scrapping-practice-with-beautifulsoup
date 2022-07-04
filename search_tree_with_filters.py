from bs4 import BeautifulSoup
import re

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
search_for_string_only = soup.findAll(text = 'Learn More')
print(search_for_string_only)

#search using css class
search_for_css_class = soup.findAll('p', class_ = 'link')
print(search_for_css_class)

#find all tags
for tag in soup.findAll(True):
    print(tag.name)

#use regex to search for a tag
email_example = """
    <br>
    <p>My email is :</p>
    example@gmail.com
    </br>
"""

soup_email = BeautifulSoup(email_example, 'html.parser')

#compile the information into a regex
regex = re.compile(r'[\w\.-]+@[\w\.-]+')
email_id = soup_email.find(text=regex)
print(email_id)