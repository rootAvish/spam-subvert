import sys
from nltk.tokenize import *
import nltk
import numpy as np

def main():
	filedist = {}
	with open(sys.argv[1]) as f:
		database = open("data.txt",'w+')	
		data = database.read()
		tokens = word_tokenize(data)	#taking words from database
		for line in database:
			(key, spam, ham, rating) = line.split()
			filedist.setdefault(key,[]).append(int(spam))
			filedist.setdefault(key,[]).append(int(ham))

		tokens += word_tokenize(f.read())	#adding words from new mail

	f.seek(0)
	for word in tokens:
		if word in filedist:
			filedist.setdefault(word,[])[0] += 1
			filedist.setdefault(word,[])[1] += 1
		else:
			spam = filedist.setdefault(word,[]).append(1)
			ham = filedist.setdefault(word,[]).append(1)
			rating = filedist.setdefault(word,[]).append(0)

		f.write()


if __name__ == '__main__':
	main()


	Nh x Ns /