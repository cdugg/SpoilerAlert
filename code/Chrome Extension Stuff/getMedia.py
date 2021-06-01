from bs4 import BeautifulSoup
import re
import urllib
import json

def getMedia(url):
	data = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(data)
	element = soup.find('div', attrs={'class': 'title_wrapper'})
	i = 0
	start = -1
	title = str(element.h1)[1:]
	for char in title:
		if char == ">" and start < 0:
			start = i + 1
		elif title[i] == "<":
			end = i
			break
		i += 1

	movieName = title[start:end].strip() + " "

	addition = soup.find(string="See full cast")
	l = addition.find_parents("a")
	url += l[0]['href']
	data = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(data)
	castTable = soup.find("table", "cast_list")
	castItems = castTable.find_all("tr")
	try:
		if len(castTable.find("a", "toggle-episodes")) > 0:
			episodic = True
	except:
		episodic = False
	characters = getCharacters(castItems, episodic)
	return movieName, characters

def getCharacters(castItems, episodic):
	characters = []
	for row in castItems:
		try:
			soup = BeautifulSoup(str(row))
			text = soup.get_text("|", strip=True)
			names = text.split("|")
			names.remove("...")
			reset = []
			for name in names:
				add = name.split("(")[0].strip()
				if add != "" and add != "/" and add != "/ ..." and add != "...":
					reset.append(add)
			reset2 = []
			for name in reset:
				add = name.split("/")
				add2 = []
				for item in add:
					if len(item) > 0 and item.strip()[0].isalnum():
						add2.append(item.strip())
				reset2.extend(add2)
			if episodic:
				characters.extend(reset2[:-1])
			else:
				characters.extend(reset2)
		except:
			pass
	keywords = {'np':{}}
	for char in characters:
		if char[0] in keywords['np'].keys():
			keywords['np'][char[0]].append(char)
		else:
			keywords['np'][char[0]] = [char]
	return keywords


#test samples
name, characters = getMedia('https://www.imdb.com/title/tt4154796/') #Avenger Endgame TEENAGE GROOT
#print(getMedia('https://www.imdb.com/title/tt0397442/')) #Gossip Girl xoxo
with open('keywords.json', 'r') as f:
	keywords = json.loads(f.read())
keywords['np'][name] = characters['np']
jsonKeys = json.dumps(keywords)
print(jsonKeys)
with open('keywords.json', 'w') as f:
	f.write(jsonKeys)