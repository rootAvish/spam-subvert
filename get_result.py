import sys
from nltk.tokenize import *
import nltk
import numpy as np

def get_result():
    filedist = {}
    with open('results/primary.txt') as f:
        lines = f.readlines()
            
        spamscores = [line for line in lines if "X-Spambayes-Classification" in line] 

    
    with open('results/before.txt','w') as output:
        
        for res in spamscores:
            output.write(res)
    
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

    return num_ham, num_spam
