from Bio import SeqIO
import os

# EXACT FILE PATH
file_path = r"C:\Users\jhari\OneDrive\Desktop\PYTHON\.vscode\BIOPYTHON\Homo sapiens BRCA1 & 2 DNA.FASTA"

def read_fasta(path):
    # Verify file existence
    if not os.path.exists(path):
        print(f"❌ Error: File NOT found at:\n{path}")
        return

    print("=" * 70)
    print("        HOMO SAPIENS BRCA 1 & 2 DNA - FASTA READER")
    print("=" * 70)

    count = 0
    # Parse FASTA records
    for record in SeqIO.parse(path, "fasta"):
        count += 1
        print(f"\n[ Record #{count} ]")
        print("-" * 70)
        print(f"Header ID   : {record.id}")
        print(f"Description : {record.description}")
        print(f"Length      : {len(record.seq):,} bp")
        
        # First 100 base pairs preview
        preview = str(record.seq[:100])
        print(f"DNA Preview : {preview}...")

    print("\n" + "=" * 70)
    print(f"SUCCESS: Read {count} sequence(s) successfully!")
    print("=" * 70)

if __name__ == "__main__":
    read_fasta(file_path)



# GC & TRANSLATION ANALYSIS
from Bio import SeqIO
import os

# YOUR EXACT FILE PATH
file_path = r"C:\Users\jhari\OneDrive\Desktop\PYTHON\.vscode\BIOPYTHON\Homo sapiens BRCA1 & 2 DNA.FASTA"

def analyze_fasta(path):
    # Verify file existence
    if not os.path.exists(path):
        print(f"❌ Error: File NOT found at:\n{path}")
        return

    print("=" * 70)
    print("    HOMO SAPIENS BRCA 1 & 2 - GC CONTENT & TRANSLATION ANALYSIS")
    print("=" * 70)

    count = 0
    # Parse FASTA records
    for record in SeqIO.parse(path, "fasta"):
        count += 1
        seq = record.seq
        
        # 1. Calculate GC Content percentage
        g_c_count = seq.count('G') + seq.count('C') + seq.count('g') + seq.count('c')
        gc_content = (g_c_count / len(seq)) * 100 if len(seq) > 0 else 0
        
        # 2. Translate DNA to Protein
        # to_stop=False translates the entire sequence including stop codons (represented as '*')
        protein_seq = seq.translate(to_stop=False)

        print(f"\n[ Record #{count}: {record.id} ]")
        print("-" * 70)
        print(f"Description  : {record.description}")
        print(f"DNA Length   : {len(seq):,} bp")
        print(f"GC Content   : {gc_content:.2f}%")
        print(f"Protein Len  : {len(protein_seq):,} amino acids")
        
        # Preview first 100 amino acids of the protein sequence
        protein_preview = str(protein_seq[:100])
        print(f"Protein Prev : {protein_preview}...")

    print("\n" + "=" * 70)
    print(f"SUCCESS: Analyzed {count} sequence(s) successfully!")
    print("=" * 70)

if __name__ == "__main__":
    analyze_fasta(file_path)