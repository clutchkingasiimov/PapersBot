from feedparser import parse
from bs4 import BeautifulSoup

data = parse("https://onlinelibrary.wiley.com/feed/15406261/most-recent")
# print(data)

# print(len(data.entries))
# print(data.entries[0].title)
# print(data.entries[0].id)
# print(data.entries[0].summary)

soup = BeautifulSoup(data.entries[0].summary, 'html.parser')
print(soup.get_text())

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
