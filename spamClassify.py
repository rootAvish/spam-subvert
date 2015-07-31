import random, re
import string
import csv
import nltk
from nltk.corpus import stopwords, wordnet
from stemming.porter2 import stem
import math
import sys
import os
import codecs
from robe.settings import BASE_DIR
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
reload(sys)
sys.setdefaultencoding('utf-8')

ham = os.path.join(BASE_DIR,'ham.txt')
spam = os.path.join(BASE_DIR,'spam.txt')

with open(ham,'r') as f:
    ham = f.read().split('\n')

with open(spam,'r') as f:
    spam = f.read().split('\n')

parenthesis = [')','(', ']','[','{','}','*','&','\\','!','$','^',';','<','>','?','_','=','+','RT','.']

def getTaggedWords():
    
    spamlist = []
    hamlist = []

    for i in range(0,len(spam)):
        spamlist.append(-1)

    for i in range(0,len(ham)):
        hamlist.append(1)

    hamtagged = zip(ham, hamlist)
    spamtagged = zip(spam, spamlist)

    taggedtext = hamtagged + spamtagged

    return taggedtext

def getWords(taggedtext): # seems correct
    # print wordlist

    tweets = []
    customstopwords = ['band', 'they', 'them','and','the']

    for (word, mailtype) in taggedtext:
        word_filter = [i.lower() for i in word.split()]
        tweets.append((word_filter, mailtype))

    wordlist = getWordFeatures(getAllWords(tweets))
    wordlist = [i for i in wordlist if not i in stopwords.words('english')]
    wordlist = [i for i in wordlist if not i in customstopwords]

    return wordlist

def getInfo(value):
    links = []
    for word in value.split(' '):
        if 'http://' in word or 'http' in word or '.com' in word:
            links += word
            value = re.sub(word,"",value)
            # print word

def textCleaner(value):
    # print value
    
    for i in parenthesis:
        value = value.replace(i, '')
    # print value
    
    for i in string.punctuation:
        value = value.replace(i, '')
    return value

def create_ngram_model():
    tfidf_ngrams = TfidfVectorizer(ngram_range=(1, 3),analyzer="word", binary=False)
    clf = MultinomialNB()
    pipeline = Pipeline([('vect', tfidf_ngrams), ('clf', clf)])
    return pipeline

def getAllWords(tweets):
    allwords = []
    for (words, mailtype) in tweets:
        allwords.extend(words)
    return allwords

#Order a list of tweets by their frequency.
def getWordFeatures(listoftweets):
    #Print out wordfreq if you want to have a look at the individual counts of words.
    wordfreq = nltk.FreqDist(listoftweets)
    words = wordfreq.keys()
    return words

taggedtext = getTaggedWords()
word_features = getWords(taggedtext)

def makeDocument(tweets): # seems correct
    documents = []
    for (words, mailtype) in tweets:
        words_filtered = [e.lower() for e in words]
        documents.append((words_filtered, mailtype))
    return documents

def textClean(s):
    remove = ['\\t','\\n','  ']
    # s = s.replace(i, Noneunct)
    for i in remove:
        s = re.sub(i,'',s)
    s = s.lower()
    s = s.split()
    return s

def classify(raw):
    # raw = str(raw_input('enter : '))
    document_words = set(textClean(raw))
    # print document_words
    features = {}
    value = 0
    num = 0
    for word in wordlist:
        num += 1
        if word in ham:
            value += 1
        elif word in spam:
            value -= 1

    # print '%0.5f' % (float(value)/float(num))
    if value==0:
        return 0
    else:
        return value

def spamClassify(stmt):
    print 'Getting Mail Type... '
    # print stmt
    count_spam =0
    count_ham =0
    count_neutral = 0
    for s in stmt:
        # print s
        # s = textClean(s)
        if s!=' ':
            out = classify(s)
            # print out
            if out < 0:
                count_spam += 1
            elif out > 0.0:
                count_ham += 1
            else:
                count_neutral += 1
            # print s, out
    # print count_neutral, count_spam, count_ham, len(stmt)
    return count_neutral, count_spam, count_ham, len(stmt)