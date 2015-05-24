import sys
from nltk.tokenize import *
import nltk
import numpy as np

def main():
	filedist = {}
	with open(sys.argv[1]) as f:
		lines = f.readlines()
			
		spamscores = [line for line in lines if "X-Spambayes-Classification" in line] 

	
	with open(sys.argv[2],'w') as output:
		
		for res in spamscores:
			output.write(res)

if __name__ == '__main__':
	main()