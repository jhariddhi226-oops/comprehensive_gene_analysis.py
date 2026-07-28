
# 🧬 Comprehensive Gene & Phylogenetic Analysis Pipeline

An end-to-end bioinformatics pipeline built with **Python** and **Biopython** to process, align, analyze, and construct evolutionary trees for human gene sequences from FASTA files.

This project demonstrates a complete computational biology workflow — bridging basic sequence statistics, Central Dogma modeling, homology searching, sequence alignment, and evolutionary phylogenetics into a single structured pipeline.

---

## 📌 Project Overview

This workflow processes and analyzes **Human BRCA1** and **BRCA2** gene sequences from raw FASTA input files.

The automated pipeline performs:

- **Sequence Parsing & Extraction**: Fast and memory-efficient sequence loading using Biopython.
- **Nucleotide & Composition Stats**: Sequence length, base distribution, and precise GC content calculation.
- **Central Dogma Modeling**: DNA transcription to RNA and full translation into Protein sequence.
- **Homology Search**: Automated online querying via **NCBI BLAST** (`blastn`).
- **Sequence Alignment**: Pairwise Global/Local alignments and Multiple Sequence Alignment (MSA).
- **Phylogenetic Reconstruction**: Pairwise Distance Matrix creation and Neighbor-Joining (NJ) Evolutionary Tree generation.
- **Structured Reporting**: Auto-generated CSV reports summarizing sequence properties.

---

## 📸 Workflow Architecture
[ FASTA Input File ]
                            |
    +-----------------------+-----------------------+
    |                                               |
[ Basic Analysis ]                              [ Central Dogma ]
• Sequence Length                               • DNA → RNA Transcription
• Base Pair Counts                              • RNA → Protein Translation
• GC Content (%)                                • Reading Frame Analysis
|                                               |
+-----------------------+-----------------------+
|
[ Comparative Genomics ]
• NCBI BLAST Search
• Pairwise Alignment
• Multiple Alignment (MSA)
|
[ Phylogenetic Reconstruction ]
• Distance Matrix
• Neighbour-Joining Tree
|
[ Automated CSV Export ]


---

## ✨ Core Features

| Feature | Description |
| :--- | :--- |
| **FASTA Parsing** | Handles single and multi-record FASTA files efficiently with Biopython's `SeqIO`. |
| **GC Content Calculation** | Computes nucleotide distribution and exact GC percentage. |
| **Central Dogma Processing** | Transcribes DNA to RNA and translates nucleotide codons into amino acid sequences. |
| **NCBI BLAST Querying** | Connects to NCBI web services (`blastn`) to fetch alignment scores and E-values. |
| **Pairwise Alignment** | Global (Needleman-Wunsch) and Local (Smith-Waterman) sequence comparisons. |
| **Multiple Sequence Alignment** | Aligns multiple target sequences using EBI ClustalOmega APIs / Matrix algorithms. |
| **Phylogenetic Trees** | Calculates distance matrices and renders Neighbor-Joining (NJ) evolutionary trees. |
| **Data Export** | Exports calculated metrics into structured `.csv` reports for downstream work. |

---

## 📊 Sample Results Summary

| Gene / Accession | Sequence Type | Length (bp) | GC Content (%) | Protein Length (aa) |
| :--- | :---: | :---: | :---: | :---: |
| **BRCA1** | Human DNA | 7,088 bp | 41.77% | 2,362 aa |
| **BRCA2** | Human DNA | 11,954 bp | 36.18% | 3,984 aa |

---

## 🛠 Tech Stack

- **Primary Language:** Python 3.x
- **Core Bio-Libraries:** `biopython` (`SeqIO`, `PairwiseAligner`, `NCBIWWW`, `NCBIXML`, `Phylo`)
- **System & Utility Modules:** `csv`, `os`, `requests`, `pathlib`

---

## ⚙️ Installation & Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git)
cd YOUR_REPOSITORY_NAME
2. Install Required Packages
Bash
pip install biopython requests
3. Run the Main Pipeline
Bash
python comprehensive_gene_analysis.py
📁 Repository Structure
├── Homo sapiens BRCA1 & 2 DNA.FASTA   # Target input sequence file
├── comprehensive_gene_analysis.py      # Main pipeline script
├── dna_report.csv                      # Output summary report (Auto-generated)
├── README.md                           # Project documentation
└── requirements.txt                    # Python dependencies
🚀 Future Roadmap
[ ] Interactive Web Dashboard using Streamlit

[ ] Mutation & Single Nucleotide Polymorphism (SNP) variant caller

[ ] Open Reading Frame (ORF) finder with frame visualization

[ ] High-resolution tree rendering with Matplotlib / Toytree

👩‍💻 Author
Riddhi Jha

M.Sc. Biotechnology Student

Focused on Python • Bioinformatics • Computational Biology

⭐ If you found this project helpful or inspiring, please consider giving it a star on GitHub!
