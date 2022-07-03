#import beatifull soup library
from bs4 import BeautifulSoup
#create html document
html_doc = """
    <html>
        <head>
            <title>My First Page</title>
        </head>
        <body>
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