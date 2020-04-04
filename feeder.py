from feedparser import parse
import warnings

"""
Variables to extract:

Title of the paper 
Publication date 
Journal Volume 
Authors 
Direct link to the paper 
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
		'PR': "http://rss.sciencedirect.com/publication/science/00313203",
		'JCF': "http://rss.sciencedirect.com/publication/science/09291199",
		'JOF': "https://onlinelibrary.wiley.com/feed/15406261/most-recent",
		'JOFE': "https://academic.oup.com/rss/site_5193/3058.xml",
		'AAP': "https://projecteuclid.org/feeds/euclid.aoap_article_rss.xml"
	}


	def __init__(self, feeds, journal_name=str,show_abstract=bool):
		self.journal_name = journal_name
		self.feeds = feeds
		self.show_abstract = show_abstract

		self.feeder = parse(self.journals[self.journal_name])
		self.journal_info = self.feeder['feed']['title']

	def __str__(self):
		return self.journal_info

	def fetch_feeds(self):
		total_count = len(self.feeder.entries) #Maximum number of feeds available on the RSS
		if (self.feeds == 'all'):
			self.feeds = total_count

		if type(self.feeds) == int:
			print("Showing Recent {} feeds".format(self.feeds))
			for i in range(self.feeds):
				title = self.feeder.entries[i].title
				print("{}. {}, ".format(i+1, title))

	def select_feed(self, feed_number):
		url =






es = Parser(22, 'ESWA',  show_abstract=True)
es.fetch_feeds()

