from Bio import SeqIO
import matplotlib.pyplot as plt
import os

# FASTA file path
file_path = r"C:\Users\jhari\OneDrive\Desktop\PYTHON\.vscode\BIOPYTHON\Homo sapiens BRCA1 & 2 DNA.FASTA"

# Check if file exists
if not os.path.exists(file_path):
    print("Error : FASTA file not found!")
    exit()

sequence_ids = []
sequence_lengths = []

# Read FASTA File
for record in SeqIO.parse(file_path, "fasta"):
    sequence_ids.append(record.id)
    sequence_lengths.append(len(record.seq))

# Display lengths in terminal
print("\nDNA Sequence Lengths:")
for seq_id, length in zip(sequence_ids,sequence_lengths):
    print(f"{seq_id}: {length} bp")

# Create Bar Chart
plt.figure(figsize=(8,5))
print(sequence_ids)
print(sequence_lengths)
print(len(sequence_ids))
print(len(sequence_lengths))
plt.bar(sequence_ids, sequence_lengths)

plt.title("DNA Sequence Length Comparison")
plt.xlabel("Sequence ID")
plt.ylabel("Sequence Length (bp)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()