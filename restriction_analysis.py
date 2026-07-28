
# RESTRICTION ENZYME ANALYSIS
from Bio.Seq import Seq
from Bio.Restriction import EcoRI

# DNA Sequence
Sequence = Seq("ATGAATTCGGATCCAAGCTTGCGGCCGCCTGCAG")

print("=" * 45)
print(" RESTRICTION ENZYMES")
print("=" * 45)

# Restriction analysis
result = EcoRI.search(Sequence)

# Output
print("DNA Sequence :" , Sequence)
print("Enzyme       :" , EcoRI)
print("Recognition Site :", EcoRI.site)
print("Cut Position(s) :", result)

# CHECKING EcoRI SITE PRESENT OR NOT?
print("DNA Sequence :", Sequence)
print("Restriction sites found :", len(result))
print("Cut Position(s) :", result)

if len(result) > 0:
    print("EcoRI can cut this DNA.")
else:
    print("No EcoRI site found.")
print("") 

from Bio.Seq import Seq
from Bio.Restriction import RestrictionBatch
enzymes = RestrictionBatch(["EcoRI","BamHI", "HindIII", "PstI"])
analysis = enzymes.search(Sequence)

print("=" * 45)
print(" RESTRICTION ENZYME ANALYSIS")
print("=" * 45)

print(f"\nDNA Sequence :  {Sequence}")
print(f"Sequence Length : {len(Sequence)} bp\n")

for enzyme, positions in analysis.items():
    print("-" * 30)
    print(f"Enzyme           : {enzyme}")
    print(f"Recognition Site : {enzyme.site}")
    print(f"Cut Position(s)  : {positions}")

# DNA DIGESTION 

#EcoRI cut position
cuts = EcoRI.search(Sequence)

print("=" * 50)
print(" DNA DIGESTIOIN ANALYSIS")
print("=" * 50)

print (f"\nOrignal DNA ({len(Sequence)} bp):")
print(Sequence)