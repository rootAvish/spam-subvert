from __future__ import division
import nltk
from nltk.corpus import wordnet as wn
import sys

script, filename = sys.argv


def lemmalist(str):
    syn_set = []
    for synset in wn.synsets(str):
        for item in synset.lemma_names:
            syn_set.append(item)
    return syn_set

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
if open(filename) != -1:
    print "File opening works ..."

#to tokenize input text into sentences

data = 'dog'

print "Data for usage is '" + data + "'"

print '\n-----\n'.join(tokenizer.tokenize(data))# splits text into sentences

#to tokenize the tokenized sentences into words

tokens = nltk.wordpunct_tokenize(data)
text = nltk.Text(tokens)
words = [w.lower() for w in text]  
print words     #to print the tokens

for a in words:
    print a

lemmalist(data)

syns = wn.synset(a)
print "synset:", syns

for s in syns:
    print 'Printing Lemmas :'
    for l in s.lemmas:
        print l.name
    print 'Printing definitions : '
    print s.definition
    print 'Printing examples : '
    print s.examples