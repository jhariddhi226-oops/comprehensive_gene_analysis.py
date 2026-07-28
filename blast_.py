from Bio import SeqIO
from Bio.Blast import NCBIWWW, NCBIXML
import os

# YOUR FASTA FILE PATH
file_path = r"C:\Users\jhari\OneDrive\Desktop\PYTHON\.vscode\BIOPYTHON\Homo sapiens BRCA1 & 2 DNA.FASTA"

def run_online_blast(path):
    if not os.path.exists(path):
        print(f"❌ Error: File NOT found at:\n{path}")
        return

    print("=" * 70)
    print("                 NCBI ONLINE BLAST ANALYSIS")
    print("=" * 70)

    # 1. Read the first sequence from your FASTA file
    record = next(SeqIO.parse(path, "fasta"))
    # We take the first 500 bp for faster web submission
    query_seq = record.seq[:500]

    print(f"Query ID     : {record.id}")
    print(f"Query Length : {len(query_seq)} bp (Subset submitted to NCBI)")
    print("\n⏳ Submitting sequence to NCBI BLAST servers... (This may take 30-90 seconds)")

    try:
        # 2. Run BLASTN against the 'nt' (nucleotide) database
        result_handle = NCBIWWW.qblast(
            program="blastn", 
            database="nt", 
            sequence=query_seq
        )
        print("✅ BLAST search finished! Parsing results...\n")

        # 3. Parse XML output
        blast_records = NCBIXML.parse(result_handle)
        blast_record = next(blast_records)

        # 4. Print top alignment results
        E_VALUE_THRESH = 0.04
        hit_count = 0

        print("=" * 70)
        print("                       TOP ALIGNMENTS")
        print("=" * 70)

        for alignment in blast_record.alignments[:5]:  # Top 5 hits
            for hsp in alignment.hsps:
                if hsp.expect < E_VALUE_THRESH:
                    hit_count += 1
                    print(f"\n[ Hit #{hit_count} ]")
                    print(f"Sequence Title : {alignment.title}")
                    print(f"Length         : {alignment.length:,} bp")
                    print(f"E-Value        : {hsp.expect}")
                    print(f"Bit Score      : {hsp.score}")
                    print(f"Identities     : {hsp.identities}/{hsp.align_length} ({(hsp.identities/hsp.align_length)*100:.2f}%)")
                    print("-" * 70)

        result_handle.close()

    except Exception as e:
        print(f"❌ Error running BLAST: {e}")

if __name__ == "__main__":
    run_online_blast(file_path)