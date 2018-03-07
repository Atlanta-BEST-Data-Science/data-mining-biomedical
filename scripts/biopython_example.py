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

