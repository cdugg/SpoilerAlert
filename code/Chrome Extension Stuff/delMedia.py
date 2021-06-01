import json
mediaTitle = "Gossip Girl "
with open('keywords.json', 'r') as f:
	keywords = json.loads(f.read())
	keywords['np'].pop(mediaTitle)

with open('keywords.json', 'w') as f:
	f.write(json.dumps(keywords))