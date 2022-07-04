from bs4 import BeautifulSoup

book_html = """
    <html>
    <body>
        <h1>The Dormouse's story</h1>
        <p class="title">
        <b>The Dormouse's story</b>
        </p>
        <p class="story">
        Once upon a time there were three little sisters; and their names were
        </p>

        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
            <li>Item 3</li>
            <li>Item 4</li>
        </ul>
    </body>
    </html>
"""

soup = BeautifulSoup(book_html, "html.parser")
print(soup.catalog)