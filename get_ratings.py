import sys
from nltk.tokenize import *
import nltk
import numpy as np
import os, re, codecs

def main():
    filedist = {}
    tokens = []
    
    exclude = raw_input('Enter directories to exclude, separated by a space: ')
    exclude = exclude.split(' ')
    defaultexclude = ['images','parser','results']
    exclude += defaultexclude

    print "Excluding directories " + str(exclude)
    '''

    for path, subdirs, files in os.walk(".", topdown=True):
        subdirs[:] = [i for i in subdirs if i not in exclude]

        for filen in files:
            if 'ham' in path:
                with codecs.open(path+'/'+filen,'r',encoding='utf-8') as f:
                    subject = re.split('Subject: ',f.readline())[1]
                    body = f.read()
                    tokens += word_tokenize(body)   #adding words from ham emails
            if 'spam' in path:
                with codecs.open(path+'/'+filen,'r',encoding='utf-8') as f:
                    subject = re.split('Subject: ',f.readline())[1]
                    body = f.read()
                    tokens += word_tokenize(body)   #adding words from spam emails'''
                #print tokens

    for path, subdirs, files in os.walk(".", topdown=True):
        subdirs[:] = [i for i in subdirs if i not in exclude]
        
        for file in files:
            f = open(path+'/'+file,'r')
            subject = re.split('Subject: ',f.readline())
            body = f.read()
            tokens += word_tokenize(body)

    database = open(sys.argv[1],'w+')   
    data = database.read()
    for line in database:
        (key, spam, ham, rating) = line.split()
        filedist.setdefault(key,[]).append(int(spam))
        filedist.setdefault(key,[]).append(int(ham))

    num_spam=0                          #Finding the total number of spam, unsure and ham
    num_ham=0
    num_unsure=0
    for line in open('results/before.txt','r+'):
        if 'spam' in line:
            num_spam += 1
        elif 'ham' in line:
            num_ham += 1
        else:
            num_unsure += 1
    #print num_unsure, num_ham, num_spam

    database.seek(0)
    d1 = dict(filedist)
    fdist = nltk.FreqDist(tokens)
    d2 = dict(fdist)
    for word in tokens:                 #for each word add spam count and ham count and ham count to table
        if word in filedist:
            filedist.setdefault(word,[])[0] += 1
            filedist.setdefault(word,[])[1] += 1
        else:
            filedist.setdefault(word,[]).append(1)
            filedist.setdefault(word,[]).append(1)
            filedist.setdefault(word,[]).append(0)
        
    for word in filedist:
        spam = filedist.setdefault(word,[])[0]
        ham = filedist.setdefault(word,[])[1]
        rating = (spam*ham) / (ham*num_ham) + (spam*num_spam)

        database.write(str(word)+'\t'+str(spam)+'\t'+str(ham)+'\t'+str(rating)+'\n')

    f.close()
    database.close()


if __name__ == '__main__':
    main()

