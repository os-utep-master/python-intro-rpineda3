#Ricardo Pineda

import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists

#Check to see if nuber of arguments is correct if not EXIT
if len(sys.argv) is not 3:
	print 'Incorrect formatt, use wordCounter.py <inputFile> <outputFile>'
	exit()

#Declare variables
inputFile = sys.argv[1]
outputFile = sys.argv[2]
#Lists
mainList = {}
testList = {}

#Check input file exists
if not os.path.exists(inputFile):
	print ('Input File does not exists: %s' % inputFile)
	exit()

#Open input file and count words.
print ('Openning File: %s - counting words.....' % inputFile)
inFile = open(inputFile, 'r')
text = inFile.read()

#Use regex to get all words
mainList = re.findall(r'\w+', text, flags=re.I) 
for word in mainList:
	word = word.lower() # make words lowercase
	#Check if the word exists in the output, if exists increment count++ if not, add it
	if word in testList.keys():
		testList[word] += 1
	else:
		testList[word] = 1
	
#Sort words and write to output file.
outFile = open(outputFile, 'w+')
for word in sorted(testList):
	outFile.write('%s %s \n' % (word, testList[word]) )
print 'Output File Created: %s' % outputFile