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
    #d1 = dict(filedist)
    for path, subdirs, files in os.walk(".", topdown=True):

        subdirs[:] = [i for i in subdirs if i not in exclude]

        if "ham" in path:

            for filen in files:
                with open(path+'/'+filen,'r') as f:

                    # Remove the subject from the body                  
                    subject = re.split('Subject: ',f.readline())[1]
                    
                    body = f.read().decode('utf-8', errors='ignore')
                    #print body
                    tokens = word_tokenize(body)
                    #print tokens
                    for word in tokens:
                        #print word
                        if word in filedist:
                            filedist.setdefault(word,[])[0] += 1
                        else:
                            filedist.setdefault(word,[]).append(1)
                            filedist.setdefault(word,[]).append(0)
                            filedist.setdefault(word,[]).append(0)
                        #print filedist

        if "spam" in path:

            for filen in files:
                with open(path+'/'+filen,'r') as f:

                    # Remove the subject from the body                  
                    subject = re.split('Subject: ',f.readline())[1]
                    
                    body = f.read().decode('utf-8', errors='ignore')
                    tokens = word_tokenize(body)

                    for word in tokens:
                        #print word
                        if word in filedist:
                            filedist.setdefault(word,[])[1] += 1
                        else:
                            filedist.setdefault(word,[]).append(0)
                            filedist.setdefault(word,[]).append(1)
                            filedist.setdefault(word,[]).append(0)
                        #print filedist

    num_spam=0
    num_ham=0
    num_unsure=0
    for line in open(sys.argv[1],'r+'):
        if 'spam' in line:
            num_spam += 1
        elif 'ham' in line:
            num_ham += 1
        else:
            num_unsure += 1
    
    
    database = open(sys.argv[2],'wb')
    for word in filedist:
        ham = filedist.setdefault(word,[])[0]
        spam = filedist.setdefault(word,[])[1]
        rating = ((spam*num_ham) / ((ham*num_spam) + (spam*num_ham)))

        print (str(word)+'\t'+str(ham)+'\t'+str(spam)+'\t'+str(rating)+'\n')
        database.write(str(word)+'\t'+str(ham)+'\t'+str(spam)+'\t'+str(rating)+'\n')

if __name__ == '__main__':
    main()