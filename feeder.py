from feedparser import parse
from collections import namedtuple
import requests
from bs4 import BeautifulSoup

"""
Variables to extract:

Title of the paper (Done)
Publication date  (Done)
Journal Volume 
Authors 
Direct link to the paper (Done)
Abstract 
"""

class Parser:
	journals = {
		'ESWA': "http://rss.sciencedirect.com/publication/science/09574174",
		'IJF': "http://rss.sciencedirect.com/publication/science/01692070",
		'BDR': "http://rss.sciencedirect.com/publication/science/22145796",
		'DSS': "http://rss.sciencedirect.com/publication/science/01679236",
		'KBS': "http://rss.sciencedirect.com/publication/science/09507051",
		'NN': "http://rss.sciencedirect.com/publication/science/08936080",
		'NC': "http://rss.sciencedirect.com/publication/science/09252312",
		'JCF': "http://rss.sciencedirect.com/publication/science/09291199",
		'JOF': "https://onlinelibrary.wiley.com/feed/15406261/most-recent",
		'JOFE': "https://academic.oup.com/rss/site_5193/3058.xml"
	}
	publishers = {
		'Elsevier': ['ESWA','IJF','BDR','DSS','KBS','NN','NC','PR','JCF'],
		'Wiley': ['JOF', 'JOFE']
	}
	#User agent for crawling the webpage without giving error 404/403
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


	def __init__(self, feeds, journal_name=str):
		self.journal_name = journal_name
		self.feeds = feeds
		self.feeder = parse(self.journals[self.journal_name])
		self.journal_info = self.feeder['feed']['title']

	def __str__(self):
		return self.journal_info

	def fetch_feeds(self):
		total_count = len(self.feeder.entries) #Maximum number of feeds available on the RSS
		if self.feeds == 'all':
			self.feeds = total_count

		if type(self.feeds) == int:
			try:
				assert self.feeds < total_count
			except:
				self.feeds = total_count

			print("Showing Recent {} feeds".format(self.feeds))
			for i in range(self.feeds):
				title = self.feeder.entries[i].title
				print("{}. {}, ".format(i+1, title))

	def select_feed(self, feed_number):
		for key in self.publishers.keys():
			if self.journal_name in self.publishers['Elsevier']:
				url = self.feeder.entries[feed_number-1].id #URL assignment for wiley below

				#Generate request for the ScienceDirect URL link
				page = requests.get(url, headers=self.headers)
				paper_page = BeautifulSoup(page.content, 'html.parser')
				paras = paper_page.find_all('p')
				abstr= [] #Store abstracts within the list (unpack them later)
				for i in range(1, len(paras)-2):
					abstr.append("-> {}\n".format(paras[i].get_text()))
				break

			if self.journal_name in self.publishers['Wiley']:
				url = self.feeder.entries[feed_number-1].link #URL assignment for elsevier above
				abstr = BeautifulSoup(self.feeder.entries[feed_number-1].summary,
				                      'html.parser').get_text()
				break

		paper_info = namedtuple('PaperInfo', ['title','url','abstract'])
		paper = paper_info(self.feeder.entries[feed_number-1].title,
		                   url,
		                   abstr)
		print("Title: {}\n".format(paper.title))
		print("Link: {}\n".format(paper.url))
		if self.journal_name in self.publishers['Elsevier']:
			print("Abstract:\n")
			for i in range(len(paper.abstract)):
				print(paper.abstract[i])
		else:
			print(paper.abstract)



es = Parser(100, 'JOF')
es.fetch_feeds()
es.select_feed(2)
