import urllib, urllib2
from bs4 import BeautifulSoup, Comment
import re

def wikipedia_content_fetching:
	url='https://en.wikipedia.org/wiki/India'
	content = urllib2.urlopen(url).read()
	soup = BeautifulSoup(content, "html.parser")

	rows =soup.find_all('div',attrs={"class" : "mw-body-content"})
	 
	filtered_content = [row.text for row in rows]
	# print filtered_content
	return filtered_content