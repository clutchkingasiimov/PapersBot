from feedparser import parse
from bs4 import BeautifulSoup
import logging

data = parse("https://onlinelibrary.wiley.com/feed/15406261/most-recent")
# print(data)
#
# print(len(data.entries))
# print(data.entries[0].title)
# print(data.entries[0].summary)

print(data.entries[0].link)

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


logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')