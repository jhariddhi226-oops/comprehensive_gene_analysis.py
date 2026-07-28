# ORF ANALYSIS

from Bio.Seq import Seq

# Sequence Object Define Karein
Sequence = Seq("ATGAAATAGATGCCCCCCGCTATGAAGTAG")

print("=" * 60)
print("       OPEN READING FRAME (ORF) ANALYSIS")
print("=" * 60) 

print(f"Sequence Length : {len(Sequence)} bp")
print(f"DNA Sequence    : {Sequence}")

print("\nORFs FOUND")
print("=" * 60)

stop_codons = ["TAA", "TAG", "TGA"]
orf_no = 1

# 3 Forward Reading Frames (0, 1, 2)
for frame in range(3):
    i = frame

    while i <= len(Sequence) - 3:
        codon = str(Sequence[i:i+3])

        # Start Codon Milne Par
        if codon == "ATG":
            # Stop Codon Dhundhne Ke Liye Inner Loop
            for j in range(i + 3, len(Sequence) - 2, 3):
                stop = str(Sequence[j:j+3])

                if stop in stop_codons:
                    orf = Sequence[i:j+3]
                    protein = orf.translate(to_stop=True)

                    print(f"\nORF {orf_no}")
                    print("-" * 60)
                    print(f"Reading Frame : +{frame + 1}")
                    print(f"Start Position: {i + 1}")
                    print(f"End Position  : {j + 3}")
                    print(f"DNA ORF       : {orf}")
                    print(f"Protein       : {protein}")
                    
                    orf_no += 1
                    break  # Pehla Stop Codon milte hi inner loop stop kar de
                    
        i += 3  # Next Codon Par Jaane Ke Liye Corrected Increment

print("\n" + "=" * 60)
print("             ORF ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 60)

