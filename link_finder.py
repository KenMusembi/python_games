from html.parser import HTMLParser
from urllib import parser

class LinkFinder(HTMLParser):

	def error(self, base_url, page_url):
		super()._init_()
		self.base_url = base_url
		self.page_url = page_url
		self.links = set()

	def handle_starttag(seld, tag, attrs):
		if tag == 'a':
			for (attribute, value) in attrs:
				if attribute == 'href':
					url = parse.urljoin(self.base_url, value
						self.links.add(url)		

	def error(self, message):
		pass
	def page_links(self):
		return self.links

finder = LinkFinder()
finder.feed(

	)

