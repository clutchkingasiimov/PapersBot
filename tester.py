from feedparser import parse
from bs4 import BeautifulSoup

data = parse("http://rss.sciencedirect.com/publication/science/01692070")
print(data)
#
print(len(data.entries))
print(data.entries[0].title)
print(data.entries[0].summary)

# soup = BeautifulSoup(data.entries[0].summary, 'html.parser')
# print(soup.get_text())

# publishers = {
# 	'Elsevier': ['ESWA', 'IJF', 'BDR', 'DSS', 'KBS', 'NN', 'NC', 'PR', 'JCF'],
# 	'Wiley': ['JOF', 'JOFE']
# }
#
# for key in publishers.keys():
# 	if 'ESWA' in publishers[key]:
# 		print(key)
# 		break
#
