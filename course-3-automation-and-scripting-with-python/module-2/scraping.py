from bs4 import BeautifulSoup

# Sample HTML content (replace with your actual HTML)
html_content = """
<html>
<body>
    <h1>This is a heading</h1>
    <p>This is a paragraph.</p>
    <p class="special">This is another paragraph.</p>
</body>
</html>
"""

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find the first 'p' element
first_paragraph = soup.find('p')
print(first_paragraph)  # Output: <p>This is a paragraph.</p>

# Find all 'p' elements
all_paragraphs = soup.find_all('p')
for paragraph in all_paragraphs:
    print(paragraph)

# Find the 'p' element with the class 'special'
special_paragraph = soup.find('p', class_='special')

print(special_paragraph)  # Output: <p class="special">This is another paragraph.</p>