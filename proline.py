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

f = "wheat.fasta"

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
