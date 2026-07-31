Markdown
# 🧬 Comprehensive Gene Analysis & Phylogenetic Pipeline

An end-to-end bioinformatics pipeline developed using **Python** and **Biopython** to analyze, translate, align, and reconstruct evolutionary relationships for human gene sequences from FASTA files.

This project bridges basic sequence analytics with advanced computational biology — covering **Central Dogma modeling**, **homology searching**, **pairwise sequence alignment**, **phylogenetic tree construction**, and **automated CSV reporting**.

---

## 📌 Project Overview

This pipeline performs automated computational analysis on **Human BRCA1** (`NM_007294.4`) and **BRCA2** (`NM_000059.4`) gene sequences.

### **Pipeline Capabilities:**
1. **FASTA Parsing & Extraction**: Fast, memory-efficient sequence loading via Biopython `SeqIO`.
2. **Nucleotide Composition**: Exact sequence length and GC Content (%) calculation.
3. **Central Dogma Workflow**:
   - DNA Transcription → RNA
   - RNA Translation → Protein sequence
4. **Homology Search**: Automated online NCBI BLAST (`blastn`) integration.
5. **Pairwise Sequence Alignment**: Global (Needleman-Wunsch) and Local (Smith-Waterman) alignments using `PairwiseAligner`.
6. **Phylogenetic Reconstruction**: Pairwise distance matrix computation and Neighbor-Joining (NJ) evolutionary tree generation.
7. **Automated Reporting**: Exporting structured summary metrics into `dna_report.csv`.

---

## 📸 Workflow Architecture

```text
                        [ Input FASTA File ]
                                 |
        +------------------------+------------------------+
        |                                                 |
[ Basic Sequence Analysis ]                       [ Central Dogma ]
  • Sequence Length (bp)                            • DNA → RNA Transcription
  • Base Composition                                • RNA → Protein Translation
  • GC Content Calculation (%)                      • Amino Acid Sequence
        |                                                 |
        +------------------------+------------------------+
                                 |
                    [ Comparative Genomics ]
                        • NCBI BLAST Query
                        • Pairwise Alignment
                        • Alignment Scoring
                                 |
                  [ Phylogenetic Reconstruction ]
                        • Distance Matrix
                        • Neighbor-Joining (NJ) Tree
                                 |
                     [ Automated CSV Export ]
✨ Core Features & Functionality
Feature	Description	Module Used
FASTA Parsing	Reads single/multi-record FASTA files efficiently	Bio.SeqIO
GC Content Calculation	Computes precise G/C nucleotide percentages	Standard Python
Central Dogma Modeling	Transcribes DNA to RNA and translates codons to amino acids	Bio.Seq
NCBI BLAST Search	Connects to web services (blastn) for alignment scores	Bio.Blast.NCBIWWW
Pairwise Alignment	Performs Global/Local pairwise sequence comparisons	Bio.Align.PairwiseAligner
Phylogenetics	Builds distance matrices and generates ASCII tree diagrams	Bio.Phylo
CSV Export	Auto-generates structured summary reports	csv
📊 Summary of Results (dna_report.csv)
Sequence ID	Description	Length (bp)	GC Content (%)
NM_007294.4	Homo sapiens BRCA1, transcript variant 1, mRNA	7,088 bp	41.77%
NM_000059.4	Homo sapiens BRCA2, transcript variant 1, mRNA	11,954 bp	36.18%
📄 Sample Terminal Output
Plaintext
======================================================================
      COMPREHENSIVE GENE & PHYLOGENETIC ANALYSIS PIPELINE
======================================================================

[ MODULE 1: SEQUENCE ANALYSIS & CENTRAL DOGMA ]
----------------------------------------------------------------------
ID          : NM_007294.4
Description : Homo sapiens BRCA1, transcript variant 1, mRNA
Length      : 7,088 bp

First 100 bases of DNA: 
AGCTTGACACAGGTTTGGAGGAGACACAGAAAGTAG...

First 100 bases of RNA: 
AGCUUGACACAGGUUUGGAGGAGACACAGAAAGUAG...

First 30 amino acids: 
SLTQVWRRHREVR...

GC Content  : 41.77%
----------------------------------------------------------------------
✅ CSV file 'dna_report.csv' created successfully!

======================================================================
[ MODULE 2: PAIRWISE SEQUENCE ALIGNMENT ]
======================================================================
Alignment Score (NM_007294.4 vs NM_000059.4): 112.0
Target            0 AGCTTGACACAGGTTTGGAGGAGACACAGAAAGTAG 36
                  | ||||||| | |||||  | | || ||  |||
Query             0 A-CTTGACAC-G-TTTG--G-A-AC-CA--AAG--- 24

======================================================================
[ MODULE 3: PHYLOGENETIC TREE CONSTRUCTION ]
======================================================================
  ________ NM_007294.4
_|
 |________ NM_000059.4

======================================================================
        ALL ANALYSIS MODULES COMPLETED SUCCESSFULLY
======================================================================
🛠 Tech Stack
Language: Python 3.x

Bioinformatics Toolkit: Biopython (SeqIO, PairwiseAligner, NCBIWWW, NCBIXML, Phylo)

Built-in Modules: csv, os, requests, pathlib

⚙️ Installation & Usage Guide
1. Clone the Repository
Bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git)
cd YOUR_REPOSITORY_NAME
2. Install Dependencies
Bash
pip install biopython requests
3. Run the Complete Analysis Script
Bash
python comprehensive_gene_analysis.py
📁 Repository Structure
.
├── Homo sapiens BRCA1 & 2 DNA.FASTA   # Primary input sequence file
├── comprehensive_gene_analysis.py      # Master bioinformatics pipeline
├── dna_report.csv                      # Auto-generated summary report
├── README.md                           # Project documentation
└── requirements.txt                    # Project dependencies
🚀 Future Roadmap
[ ] Interactive Web Dashboard using Streamlit

[ ] Open Reading Frame (ORF) finder with frame visualization

[ ] Mutation & Single Nucleotide Polymorphism (SNP) variant caller

[ ] High-resolution graphical tree rendering using Matplotlib / Toytree

👩‍💻 Author
Riddhi Jha

M.Sc. Biotechnology Student

Focused on Python • Bioinformatics • Computational Biology

⭐ If you found this project helpful or inspiring, please consider giving it a star on GitHub!

## 🏅 Achievement Badge

- Python for Data Science (IBM)
  - 🔗 Badge: https://www.credly.com/badges/a6d0e9de-1874-42e8-89df-6436a76be329/linked_in_profile

---

