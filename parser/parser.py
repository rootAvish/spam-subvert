from __future__ import division
import nltk
from nltk.corpus import wordnet as wn
import sys

if len(sys.argv) == 1:
    print 'Usage: python parser.py <filename>'
    exit(1)
else:
    scripts, filename = sys.argv

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
if open(filename,'r+') == -1:
	print 'Error in opening file.'
	quit()
else:
	fp = open(filename,'r+')
	data = fp.read()
	print data
	#print '\n-----\n'.join(tokenizer.tokenize(data))
	tokens = nltk.wordpunct_tokenize(data) 
	text = nltk.Text(tokens)
	words = [w.lower() for w in text]
	tags = nltk.pos_tag(words)
	#nltk.corpus.tags.tagged_words(tagset='universal')

for a in words:
	if wn.morphy(a,wn.NOUN) == None:
		words = [w.replace(a, '') for w in words]
	else:
		words = [w.replace(a, wn.morphy(a,wn.NOUN)) for w in words]
	
#print words
print ' '.join(words)