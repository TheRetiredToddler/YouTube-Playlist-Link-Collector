from bs4 import BeautifulSoup
import requests
import sys

def getPlaylistLinks(url):
	sourceCode = requests.get(url).text
	soup = BeautifulSoup(sourceCode, 'html.parser')
	domain = 'https://www.youtube.com'
	sys.stdout.write('\n');
	for link in soup.find_all("a", {"dir": "ltr"}):
		href = link.get('href')
		if href.startswith('/watch?'):
			sys.stdout.write(domain + href + '\n')
			sys.stdout.flush()

getPlaylistLinks(sys.argv[1])