#!/usr/local/bin/python


import glob 
import urllib2

a = 'list.txt'
b='burrito'

def concatenate(a):
	read_files = glob.glob(a)
	with open("result.txt", "a") as outfile: 
		for f in read_files: 
			with open(f, "rb") as infile:  
				outfile.write(infile.read())
				outfile.close()
				
def organisms(b):
	if b == 'burrito':
		return 'List1.txt_List2.txt'

def database(org):
	c = org.split("_")
	for i in range(0,len(c)):
		concatenate(c[i])
		
		
		
org = organisms(b)
database(org)
concatenate(a)  




'''response = urllib2.urlopen('http://www.uniprot.org/uniprot/?query=organism:4565.fasta')
headers = response.info()
data = response.read()
print data

'''
