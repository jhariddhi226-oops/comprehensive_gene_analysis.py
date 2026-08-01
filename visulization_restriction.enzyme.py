import matplotlib.pyplot as plt
from Bio.Restriction import BamHI, EcoRI, HindIII, PstI, RestrictionBatch
from Bio.Seq import Seq

# DNA Sequence
sequence = Seq("ATGAATTCGGATCCAAGCTTGCGGCCGCCTGCAG")
seq_len = len(sequence)

enzymes = RestrictionBatch(["EcoRI", "BamHI", "HindIII", "PstI"])
results = enzymes.search(sequence)

# -------------------------------------------------------------
# 1. VISUALIZE RESTRICTION MAP (Linear DNA Map)
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), gridspec_kw={"height_ratios": [1, 2]})

# Plot 1: Linear DNA Map
ax1.plot([1, seq_len], [0, 0], color="black", linewidth=6, label="DNA Strand")
ax1.set_xlim(0, seq_len + 5)
ax1.set_ylim(-1, 1)
ax1.axis("off")
ax1.set_title("Linear DNA Restriction Map", fontsize=12, fontweight="bold")

# Add markers for cuts
colors = {"EcoRI": "red", "BamHI": "blue", "HindIII": "green", "PstI": "purple"}

for enzyme, cuts in results.items():
    for cut in cuts:
        c = colors.get(str(enzyme), "orange")
        ax1.plot([cut, cut], [-0.3, 0.3], color=c, linewidth=2.5)
        ax1.text(
            cut,
            0.4,
            f"{enzyme}\n({cut} bp)",
            ha="center",
            va="bottom",
            fontsize=9,
            color=c,
            fontweight="bold",
        )

# -------------------------------------------------------------
# 2. VISUALIZE SIMULATED AGAROSE GEL ELECTROPHORESIS
# -------------------------------------------------------------
ax2.set_facecolor("#222222")  # Dark gel background
ax2.set_xlim(0, 5)
ax2.set_ylim(0, 40)
ax2.set_ylabel("Fragment Size (bp)", fontsize=10)
ax2.set_title(
    "Simulated Agarose Gel Electrophoresis", fontsize=12, fontweight="bold"
)
ax2.set_xticks([1, 2, 3, 4])
ax2.set_xticklabels(["Uncut", "EcoRI", "BamHI", "Multiple"], fontsize=9)

# Draw Gel Lanes
# Lane 1: Uncut DNA
ax2.hlines(
    y=seq_len,
    xmin=0.7,
    xmax=1.3,
    colors="#00FF66",
    linewidth=4,
    alpha=0.9,
)

# Lane 2: EcoRI Digestion
eco_cuts = EcoRI.search(sequence)
if eco_cuts:
    c = eco_cuts[0] - 1
    f1, f2 = c, seq_len - c
    ax2.hlines(
        y=[f1, f2],
        xmin=1.7,
        xmax=2.3,
        colors="#00FF66",
        linewidth=4,
        alpha=0.9,
    )

# Lane 3: BamHI Digestion
bam_cuts = BamHI.search(sequence)
if bam_cuts:
    c = bam_cuts[0] - 1
    f1, f2 = c, seq_len - c
    ax2.hlines(
        y=[f1, f2],
        xmin=2.7,
        xmax=3.3,
        colors="#00FF66",
        linewidth=4,
        alpha=0.9,
    )

# Lane 4: All Cut Fragments
all_cuts = sorted(
    list(set([c - 1 for cuts in results.values() for c in cuts]))
)
all_cuts = [0] + all_cuts + [seq_len]
frag_sizes = [all_cuts[i + 1] - all_cuts[i] for i in range(len(all_cuts) - 1)]

ax2.hlines(
    y=frag_sizes,
    xmin=3.7,
    xmax=4.3,
    colors="#00FF66",
    linewidth=4,
    alpha=0.9,
)

plt.tight_layout()
plt.show()