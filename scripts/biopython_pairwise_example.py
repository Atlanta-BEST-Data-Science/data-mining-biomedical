#Import statements
from Bio import SeqIO

#Load the sequence
file_path = "E:/Data Science Biology Tutorial/sequence 1.fasta" #<- INSERT YOUR PATH HERE
num_sequences = 0
for seq_record in SeqIO.parse(file_path, "fasta"):
    sequence = seq_record.seq
    num_sequences += 1

print(num_sequences)
print(len(sequence))

#Subest the sequence
from Bio import pairwise2
seq_1 = sequence[0:1000]
seq_2 = sequence[-1000:-1]

#Perform the alignment
alignments = pairwise2.align.globalxx(seq_1, seq_2)
print(len(alignments))
print(alignments[0])

print(pairwise2.format_alignment(*alignments[0]))
