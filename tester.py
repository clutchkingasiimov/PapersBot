from feedparser import parse
from bs4 import BeautifulSoup

data = parse("http://rss.sciencedirect.com/publication/science/09574174")
print(len(data.entries))
print(data.entries[0].id)
print(data.entries[0].summary)

soup = BeautifulSoup(data.entries[0].summary, 'html.parser')
print(soup.prettify())