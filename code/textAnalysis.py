import nltk
from nltk import word_tokenize, pos_tag, sent_tokenize
from nltk.corpus import stopwords, wordnet as wn
from nltk.stem import WordNetLemmatizer
from nltk.corpus.reader.wordnet import WordNetError
import splitter
from splitter import text

keyWords = ["alternate ending", "antagonist", "anti-climax", "anti-hero", "backstory", "cameo", "cliffhanger",
"credits", "crisis", "deus ex machina", "die", "epilogue", "finale", "flashback", "flashforward", "foreshadowing", 
"punchline", "red herring", "resolution", "retrospective", "scenario", "scene", "sequence", "spoiler", "subplot",
"time lapse", "twist", "kill"]

stopWords = set(stopwords.words("english"))

def filterSw(sentence):
    filterStopWords = []
    tokenizedWord = word_tokenize(sentence)
    for i in tokenizedWord:
        if i not in stopWords:
            filterStopWords.append(i)
    return(" ".join(filterStopWords))

def penn2morphy(penntag):
    """ Converts Penn Treebank tags to necessary tags. 
    IE:Penn Treebank II tag set
    {'CC':'coordinating conjunction', #and or but
    'CD':'cardinal number', #five
    'DT':'determiner', #the a these
    'EX':'existential there', # THERE were 6 boys
    'FW':'foreign word', #hola
    'IN':'subordinating or preposition conjunction', #of on before unless
    'JJ':'adjective', #nice
    'JJR':'comparative adjective', #nicer
    'JJS':'superlative adjective', #nicest
    'LS':'list item marker',
    'MD':'modal auxillary verb',#may should
    'NN':'singular or mass noun',#tiger
    'NNS':'plural noun',#tigers
    'NNP':'proper singular noun',#Germany
    'NNPS':'proper plural noun',#two CHRISTMASES ago
    'PDT':'predeterminer',#BOTH of them
    'POS':'possessive ending',#'s
    'PRP':'personal possessive',#me you it
    'PRP$':'possessive pronoun',#my your our
    'RB':'adverb',#loudly
    'RBR':'comparative adverb',#better
    'RBS':'superlative adverb',#best
    'RP':'particle adverb',#about off up
    'SYM':'symbol',#%
    'TO':'infinitival to',#what TO do?
    'UH':'interjection',#oh oops gosh
    'VB':'base form verb',#think
    'VBZ':'3rd person singular present verb',#she THINKS
    'VBP':'non-3rd person singular present verb',#I THINK
    'VBD':'past tense verb',#they THOUGHT
    'VBN':'past participle verb',#a SUNKEN ship
    'VBG':'present participle verb',#THINKING is fun
    'WDT':'wh-determiner',#which whatever whichever
    'WP':'personal wh-pronoun',#what who whom
    'WP$':'possessive wh-pronoun',#whose whosever
    'WRB':'wh-adverb' #where when
    }
    Our own tags to be converted:
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

"""
    morphy_tag = {'NN':'n', 'JJ':'aj',
                  'VB':'v', 'RB':'av', 'MD':'md'}
    try:
        if penntag[:3] == 'NNP':
            return 'np'
        return morphy_tag[penntag[:2]]
    except:
        if penntag == 'PRP':
            return 'n'
        return 'q'


wnl = WordNetLemmatizer()

def findTag(sentence):
    #Finds pos tags and prints lemmatized words with pos tag adjusted to speicifc word
    myText = []

    for token, pos in pos_tag(word_tokenize(sentence)):
        try:
            morphy_pos = penn2morphy(pos)
            if token == "dies":
                myText.append("die")
            if morphy_pos in ["a", "n", "v"]:
                myText.append(wnl.lemmatize(token, pos=morphy_pos))
            elif morphy_pos in ['r']: 
                myText.append(wn.synset(token+".r.1").lemmas()[0].pertainyms()[0].name())
            else:
                myText.append(wnl.lemmatize(token))
        except IndexError:
            myText.append(token)
            continue
        except WordNetError:
            myText.append(token)
            continue
    return " ".join(myText)

text = filterSw(findTag(text))

        
def blockKeyWords(wordList, blackList):
    #block defined keywords 
    blockedList = []
    wordList = word_tokenize(wordList)

    for word in wordList:
        spoilerCount = 0

        for spoiler in blackList:
            if spoiler in word:
                spoilerCount += 1

        if spoilerCount > 0:
            blockedList.append("[SPOILER(S) BLOCKED]") #to be changed with javascript html css blur 
        else:
            blockedList.append(word)

    blockedList = " ".join(blockedList)

    print(blockedList)