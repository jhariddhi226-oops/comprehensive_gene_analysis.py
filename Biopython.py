# from Bio.Seq import Seq
# dna = Seq("ATGCATGCATGCATGC")
# print (dna)
# print(dna.complement())
# print(dna.reverse_complement())

# from Bio import SeqIO
# for sequence in SeqIO.parse(r"C:\Users\jhari\Desktop\.vscode\BIOPYTHON\Homo sapiens BRCA1 & 2 DNA.FASTA", "fasta"):
#     print(sequence.id)
#     print(repr(sequence.seq))
#     print(len(sequence))

# from Bio import SeqIO

# input_file = r"C:\Users\jhari\Desktop\.vscode\BIOPYTHON\Homo sapiens BRCA1 & 2 DNA.FASTA"

# for record in SeqIO.parse(input_file,"fasta"):
#     print("ID:", record. id)
#     print("Description:", record.description)
#     print("Length:", len(record.seq))
#     # print("sequence:")
#     # print(record.seq)
#     # print("-" * 50)


# gc = (record.seq.count("G")+record.seq.count("C"))/len(record.seq[:60]) 
# print("GC Content", round(gc, 2),"%")

# rna = record.seq.transcribe()
# print("RNA" , rna)

# protein = record.seq.translate()
# print("protein: ", protein)

# from Bio import SeqIO

# input_file = r"C:\Users\jhari\Desktop\.vscode\BIOPYTHON\Homo sapiens BRCA1 & 2 DNA.FASTA"

# for record in SeqIO.parse(input_file, "fasta"):
#     print("ID" , record.id)
#     print("Description: " , record.description)
#     print("Length: " , len(record.seq))

#     print("\nFirst 100 bases of DNA: ")
#     print(record.seq[:100])

#     rna = record.seq.transcribe()
#     print("\n First 100 bases of RNA: ")
#     print(rna[:100])

#     protein = record.seq.translate()
#     print("\n First 30 amino acids: ")
#     print(protein[:30])

#     gc = (record.seq.count("G") + record.seq.count("C")) / len(record.seq) * 100
#     print("\n GC Content: " , round(gc, 2), "%")


from Bio import SeqIO
import csv

# Read FASTA file
input_file = r"C:\Users\jhari\Desktop\.vscode\BIOPYTHON\Homo sapiens BRCA1 & 2 DNA.FASTA"
results = []

# parse FASTA and translate DNA to protein
for record in SeqIO.parse(input_file, "fasta"):
    print("ID" , record.id)
    print("Description: " , record.description)
    print("Length: " , len(record.seq))

    print("\nFirst 100 bases of DNA: ")
    print(record.seq[:100])

    rna = record.seq.transcribe()
    print("\n First 100 bases of RNA: ")
    print(rna[:100])

    protein = record.seq.translate()
    print("\n First 30 amino acids: ")
    print(protein[:30])

    gc = (record.seq.count("G") + record.seq.count("C")) / len(record.seq) * 100
    print("\n GC Content: " , round(gc, 2), "%")

#store results
results.append([record.id,record.description,len(record.seq),round(gc,2)])
print("_" * 60)

#write results to csv
with open("dna_report.csv" , "w" , newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(["ID" , "Description" , "Length" , "GC Content"])
    writer.writerow(results)
    print("CSV file created successfully!")

#display results
print("\nDNA TP PROTEIN TRANSLATION COMPLETED")
print("\nSummary: ")
for row in results:
    print('\nSequence ID :' , row[0])
    print("Description   :" , row[1])
    print("Length        :" , row[2])
    print("GC Content    :" , row[3], "%")
    



    