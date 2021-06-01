from bs4 import BeautifulSoup
import urllib.request

def splitt(link):
	source = urllib.request.urlopen(link)
	html = source.read()
	soup = BeautifulSoup(html,"html5lib")
	for script in soup(["script", "style"]):
		script.extract()
	text = soup.get_text()

	lines = (line.strip() for line in text.splitlines())
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	text = "\n".join(chunk for chunk in chunks if chunk)
	return text