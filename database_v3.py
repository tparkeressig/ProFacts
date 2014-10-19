#!/usr/local/bin/python


import glob 
import urllib2

from flask import Flask
app = Flask(__name__)

    

'''Creates a Database for Burrito'''

b='burrito'
		
def organisms(b):
	if b == 'burrito':
		return 'wheat.fasta_soybean.fasta'	

def database(org):
	c = org.split("_")
	for i in range(0,len(c)):
		file=c[i]
		html='https://raw.githubusercontent.com/tparkeressig/ProFacts/master/'
		website = html + file 
		response = urllib2.urlopen(website)
		headers = response.info()
		data = response.read()
		print data[0]
		fo = open("result.txt","a")
		fo.write(data)
		fo.close
		
	
org = organisms(b)
database(org)



'''Finds Durability in Intestines'''


import re

sequence = 'LQLQPFPQPQLPYPQPQLPYPQPQLPYPQPQPF'

def scan(text, letter, threshold):
    sum = 0
    while text:
        section = text[0:19]
        if section.count('P') >= threshold:
            sum += 1
        text = text[1:]
    return sum

"""
for i in range(20):
    print(str(i) + ' => ' + str(scan(sequence, 'P', i)))
"""

# collect all the ids
p = re.compile('>sp[|]\w*[|](\w*)')

# collect all the sequences
r = re.compile('SV=\d\n([A-Z\n]*)')

f = "result.txt"

with open(f) as f:
    file = f.read()
    ids = p.findall(file)
    sequences = r.findall(file)
    scores = [scan(protein, 'P', 9) for protein in sequences]
    proteins = zip(ids, sequences, scores)

with open('wheatoutput.txt', 'w') as f:
    for protein in proteins:
        if protein[2] > 0:
            f.write(protein[0] + ' ' + protein[1] + ' ' + str(protein[2]) + '\n')


v=open("wheatoutput.txt").read()
html=open("/Users/Alex/Desktop/website.html").read().replace("AAAAAA", v)


@app.route("/")
def hello():
	return html
if __name__ == "__main__":
    app.run()
    

