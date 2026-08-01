from Bio import SeqIO
import matplotlib.pyplot as plt
import os

# FASTA File path
file_path = r"C:\Users\jhari\OneDrive\Desktop\PYTHON\.vscode\BIOPYTHON\Homo sapiens BRCA1 & 2 DNA.FASTA"

# Check if file exists
if not os.path.exists(file_path):
    print("Error : FASTA file not found!")
    exit()

sequence_lengths = []

# Read FASTA File
for record in SeqIO.parse(file_path, "fasta"):
    sequence_lengths.append(len(record.seq))

print("Sequence Lengths :" , sequence_lengths)

# Histogram
plt.figure(figsize=(8,5))
plt.hist(sequence_lengths, bins=5, edgecolor= "black")

plt.title("Distribution of DNA Sequence Lengths ")
plt.xlabel("DNA Length (bp)")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()