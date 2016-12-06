import urllib, urllib2
from bs4 import BeautifulSoup, Comment

def wikipedia_content_fetching(page_url):
	url=page_url
	# url='https://en.wikipedia.org/wiki/India'
	content = urllib2.urlopen(url).read()
	soup = BeautifulSoup(content, "html.parser")
	rows =soup.find_all('div',attrs={"class" : "mw-body-content"})
	filtered_content = [row.text for row in rows]
	output =  ' '.join(filtered_content)
	# print (output)
	return output