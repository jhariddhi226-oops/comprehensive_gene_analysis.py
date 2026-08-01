from Bio.Seq import Seq
import matplotlib.pyplot as plt

sequence = Seq("ATGAAATAGATGCCCCCCGCTATGAAGTAG")
seq_len = len(sequence)
stop_codons = ["TAA", "TAG", "TGA"]

orfs = []

# Forward Reading Frames (0, 1, 2)
for frame in range(3):
    i = frame
    while i <= seq_len - 3:
        if str(sequence[i:i+3]) == "ATG":
            for j in range(i + 3, seq_len - 2, 3):
                if str(sequence[j:j+3]) in stop_codons:
                    orfs.append({
                        "frame": frame + 1,
                        "start": i + 1,
                        "end": j + 3,
                        "length": (j + 3) - i
                    })
                    break
        i += 3

# Visualization Setup
fig, ax = plt.subplots(figsize=(10, 4))

# Sequence Base Line
ax.plot([1, seq_len], [0, 0], color='gray', linewidth=4, label="DNA Sequence")

# Colors for Frames
colors = {1: '#e74c3c', 2: '#3498db', 3: '#2ecc71'}

# Plot each ORF as a block
for idx, orf in enumerate(orfs):
    f = orf["frame"]
    start = orf["start"]
    end = orf["end"]
    
    # Draw ORF rectangle/bar
    ax.barh(y=f, width=end - start + 1, left=start, height=0.4, 
            color=colors[f], alpha=0.8, edgecolor='black', label=f"Frame +{f}" if f not in [o['frame'] for o in orfs[:idx]] else "")
    
    # Label on ORF
    ax.text((start + end) / 2, f, f"ORF {idx+1}\n({start}-{end} bp)", 
            ha='center', va='center', color='white', fontsize=8, fontweight='bold')

# Chart Customization
ax.set_xlabel("Base Pair Position (bp)", fontsize=10, fontweight='bold')
ax.set_ylabel("Reading Frame", fontsize=10, fontweight='bold')
ax.set_yticks([1, 2, 3])
ax.set_yticklabels(["Frame +1", "Frame +2", "Frame +3"])
ax.set_xlim(0, seq_len + 2)
ax.set_ylim(0.5, 3.5)
ax.set_title("Open Reading Frame (ORF) Map", fontsize=12, fontweight='bold')
ax.grid(axis='x', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
