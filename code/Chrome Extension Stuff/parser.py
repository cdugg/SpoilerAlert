from nltk.data import find
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer
from bllipparser import RerankingParser, Tree
from splitter import splitt
import json, re

def penn2morphy(penntag):
    """ Converts Penn Treebank tags to WordNet. """
    morphy_tag = {'NN':'n', 'JJ':'a',
                  'VB':'v', 'RB':'r', 'MD': 'md'}
    try:
        if penntag[:3] == 'NNP':
           return 'np'
        return morphy_tag[penntag[:2]]
    except:
        if penntag == 'PRP':
            return 'n'
        return 'q' 

def properNouns(x):
	newx = []
	i = 0
	#finding proper nouns
	pNoun = ""
	while i < len(x) - 1:
		if x[i][1] == 'NNP':
			pNoun += x[i][0] + " "
		else:
			if pNoun != "":
				newx.append((pNoun.strip(), 'NNP'))
				pNoun = ""
			newx.append(x[i])
		i += 1
	newx.append(x[i])
	return newx

def morph(newx):
	newx2 = []
	for item in newx:
		sample = penn2morphy(item[1])
		if sample != 'q' and sample != 'md':
			newx2.append((item[0], sample))
		if sample == 'md' and newx[-1][0] == '?':
			print('spoiler')
	return newx2

def getScore(tup):
	try:
		return keywords[tup[1]][tup[0]]
	except:
		return 0

def inNames(name):
	try:
		for item in keywords['np'].keys():
			if name in keywords['np'][item][name[0]]:
				return True
	except:
		return False
		
def parseSent(sent, parser, cfg):
	nbest_list = parser.parse(sent)
	tree = (nbest_list[0].ptb_parse)
	trees = Tree(str(tree))
	x = trees.tokens_and_tags()
	x2 = properNouns(x)
	importants = morph(x2)
	#print(importants)

	wnl = WordNetLemmatizer()

	score = 0
	properMultiplier = 1
	verbMultiplier = 1
	prevNoun = ""
	for item in importants:
		if item[1] == 'v' and prevNoun == 'np':
			word = wnl.lemmatize(item[0], pos = item[1])
			tmp = getScore((word, item[1]))
			score += tmp
			if tmp > 0:
				verbMultiplier += .25
		elif item[1] == 'n':
			word = wnl.lemmatize(item[0], pos = item[1])
			score += getScore((word, item[1]))
			prevNoun = item[1]
		elif item[1] != 'np':
			word = wnl.lemmatize(item[0], pos = item[1])
			score += getScore((word, item[1]))
		else:
			if inNames(item[0]):
				prevNoun = 'np'
				properMultiplier += .5
			
	#print(verbMultiplier, properMultiplier, score)
	score = verbMultiplier * properMultiplier * score
	if score  >= 150:
		print("SPOILER: ", end = "")
	else:
		print("NOT SPOILER: ", end = "")

def main():
	cfg = find('models/bllip_wsj_no_aux').path
	parser = RerankingParser.from_unified_model_dir(cfg)

	link = "https://screenrant.com/avengers-endgame-movie-spoilers/"
	content = splitt(link).split("\n")
	print(content)
	for item in content:
		item = sent_tokenize(item)
		for sentence in item:
			sentence = sentence.replace(u'\xa0', u' ')
			parseSent(sentence, parser, cfg)
			print(sentence)


with open('keywords.json', 'r') as f:
	keywords = json.loads(f.read())

if __name__ == '__main__':
	main()

'''
Join as aj:
	[JJ - adjective - dying
	JJR - comparitive adjective - stronger
	JJS - superlative adjective - strongest]
NOT A SPOILER as md:
	MD - modal auxillary verb - predictive spoiler not to be blocked
Join as n:
	[NN - singular mass noun - dog
	NNS - plural noun - dogs
	NNP - proper singular noun - Tony Stark
	NNPS - proper plural noun - The Starks]
Join as av:
	[RB - adverb - deadly
	RBR - comparative adverb - healthier
	RBS - superlative adverb - helathiest]
Join as v:
	[VB - base form verb - think
	VBZ - 3rd person singular present verb - she THINKS
	VBP - non-3rd person singular present verb - I THINK
	VBD - past tense verb - they THOUGHT
	VBN - past participle verb - SUNKEN ship
	VBG - present participle verb - #THINKING is fun]

'''
