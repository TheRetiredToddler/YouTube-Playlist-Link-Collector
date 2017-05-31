from bs4 import BeautifulSoup
import requests
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("url", type=str)
parser.add_argument("--wt", type=str)

args = parser.parse_args()

def getPlaylistLinks(url, withTitle):
	sourceCode = requests.get(url).text
	soup = BeautifulSoup(sourceCode, 'html.parser')
	domain = "https://www.youtube.com"
	
	sys.stdout.write("\n")
	for link in soup.find_all("a", {"dir": "ltr"}):
		href = link.get("href")
		videoTitle = link.string.strip()
		
		if args.wt is 't':
			if href.startswith("/watch?"):
				sys.stdout.write(videoTitle + '\n')
				sys.stdout.write(domain + href + '\n\n')
		if args.wt is None:
			if href.startswith("/watch?"):
				sys.stdout.write(domain + href + '\n')
				
getPlaylistLinks(args.url, args.wt)
