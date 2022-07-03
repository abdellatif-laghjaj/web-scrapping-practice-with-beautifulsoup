#import beatifull soup library
from bs4 import BeautifulSoup
#create html document
html_doc = """
    <html>
        <head>
            <title>My First Page</title>
        </head>
        <body>
            <b><!-- This is a comment --></b>
            <h2>My First Heading</h2>
            <p>My first paragraph.</p>
        </body>
    </html>
""";

#parse html document
soup = BeautifulSoup(html_doc, 'html.parser')

#view the soup type
print(type(soup))

#create a tag object
tag = soup.title

#view the tag type
print(tag)

#create a comment object type
comment = soup.b.string

#view the comment type
print(comment)

#view tag attributes
print(tag.attrs)