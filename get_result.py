import sys
from nltk.tokenize import *
import nltk
import numpy as np

def main():
	filedist = {}
	with open(sys.argv[1]) as f:
		lines = f.readlines()

		database = open("data.txt",'w+')
		data = database.read()
		tokens = word_tokenize(data)
		f.seek(0)
		for line in f:
			(key, value, num_files) = line.split()
			filedist.setdefault(key,[]).append(value)
			filedist.setdefault(key,[]).append(num_files)

		tokens += word_tokenize(filedata)
		fdist = nltk.FreqDist(tokens)
		fdist = dict(fdist)
		d = {k:[x+y for x,y in zip(fdist.get(k,0),filedist.get(k,0))] for k in set(fdist) | set(filedist)}
		for i in d:
			database.write(str(i)+'\t'+str(d.setdefault(i,[])[0])+'\t'+str(d.setdefault(i,[])[1])+'\n')
			
		spamscores = [line for line in lines if "X-Spambayes-Classification" in line] 

	
	with open(sys.argv[2],'w') as output:
		
		for res in spamscores:
			output.write(res)

if __name__ == '__main__':
	main()