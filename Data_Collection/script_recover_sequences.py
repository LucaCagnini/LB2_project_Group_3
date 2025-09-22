from sys import argv
from Bio import SeqIO
import subprocess
import shlex
'''
Takes as input a list of ids as argv[1] (ids that contain the > character)
and as argv[2] a dataset of fasta sequences (for example the entire swissprot)
'''

to_get = argv[1] #clusterized file with ids
dataset = argv[2] #fasta file all the sequences
subprocess.run(shlex.split("touch recovered_sequences.fasta")) #creates an empty file recovered_sequences.fasta
output_file_name = 'recovered_sequences.fasta'
with open(to_get , 'r') as file:
    ids_to_get = {line[1:].strip() for line in file}

found = 0 #keeps track of single ids.
counter = len(ids_to_get)

with open(dataset , 'r') as file1 , open(output_file_name , 'w') as file2:
    for prot in SeqIO.parse(file1 , 'fasta'):
        if prot.id in ids_to_get:
            found = found + 1
            SeqIO.write(prot , file2 , 'fasta')
        else:
            pass

print(found)
print(counter)
        