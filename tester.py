from feedparser import parse


data = parse("http://rss.sciencedirect.com/publication/science/09574174")
print(len(data.entries))
print(data.entries[0].id)
print(data.entries[0].summary)