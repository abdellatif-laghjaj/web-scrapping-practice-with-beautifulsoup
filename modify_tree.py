from bs4 import BeautifulSoup

html_doc = """
<html>
	<head>
		<title>Example website</title>
		<meta charset="utf-8"/>
		<meta http-equiv="Content-type" content="text/html; charset=utf-8"/>
		<meta name="viewport" content="width=device-width, initial-scale=1"/>
      <style type="text/css">* {font-family: Inter;} body {padding: 2em;}</style>
	</head>
	<body>
		<div>
			<h1>Hello world!</h1>
			<p>This is a example website.</p>
            <!-- Hi! -->
			<p>
				<a href="https://tiagorangel.com/">Learn More</a>
			</p>
		</div>
	</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

tag = soup.find('h1')
print(tag)

#modify the tag
tag.string.replace_with('Modified text')
print(tag)

# add a new tag
tag.insert_after('<p>This is a new tag</p>')

#view the added tag
print(tag.next_sibling)