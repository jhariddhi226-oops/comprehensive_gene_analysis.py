from Bio import SeqIO
from Bio.Align import PairwiseAligner

file_path = r"C:\Users\jhari\OneDrive\Desktop\PYTHON\.vscode\BIOPYTHON\Homo sapiens BRCA1 & 2 DNA.FASTA"

def progressive_msa_pure_python(path):
    # Load all sequences from FASTA
    records = list(SeqIO.parse(path, "fasta"))
    
    if len(records) < 2:
        print("❌ At least 2 sequences required for alignment.")
        return

    # Truncate sequences to equal length window (e.g., first 100 bp) for testing
    seqs = [rec.seq[:100] for rec in records]
    
    aligner = PairwiseAligner()
    aligner.mode = 'global'
    aligner.match_score = 1
    aligner.mismatch_score = -1
    aligner.open_gap_score = -1

    print("=" * 70)
    print("       PROGRESSIVE PAIRWISE MATRIX ALIGNMENT (PURE PYTHON)")
    print("=" * 70)

    # Step 1: Pairwise Distance Matrix Score
    print("Score Matrix:")
    for i in range(len(seqs)):
        for j in range(i + 1, len(seqs)):
            score = aligner.score(seqs[i], seqs[j])
            print(f"[{records[i].id}] vs [{records[j].id}] -> Score: {score}")

    # Step 2: Show Best Pairwise Alignment
    best_alignment = aligner.align(seqs[0], seqs[1])[0]
    print("\nPrimary Pairwise Alignment Base:")
    print(best_alignment)

if __name__ == "__main__":
    progressive_msa_pure_python(file_path)