#!/usr/local/bin/python


import glob 
import urllib2

from flask import Flask
app = Flask(__name__)

    

'''Creates a Database for Burrito'''

b='burrito'
		
def organisms(b):
	if b == 'burrito':
		return 'wheat.fasta_soybean.fasta_beef.fasta_corn.fasta_rice.fasta'	

def database(org):
	c = org.split("_")
	for i in range(0,len(c)):
		file=c[i]
		html='https://raw.githubusercontent.com/tparkeressig/ProFacts/master/'
		website = html + file 
		response = urllib2.urlopen(website)
		headers = response.info()
		data = response.read()
		fo = open("result.txt","a")
		fo.write(file+'\n')
		fo.write(data)
		fo.close
		
	
org = organisms(b)
database(org)
