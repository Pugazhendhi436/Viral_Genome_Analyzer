# ============================================================
# VIRAL GENOME ANALYZER - VERSION 5
# REAL FASTA FILE ANALYSIS
# ============================================================

import matplotlib.pyplot as plt
import os


# ============================================================
# SETTINGS
# ============================================================

ORIGINAL_FILE = "sequences/original.fasta"
MUTATED_FILE = "sequences/mutated.fasta"

RESULTS_FOLDER = "results"


# ============================================================
# CREATE RESULTS FOLDER
# ============================================================

if not os.path.exists(RESULTS_FOLDER):
    os.makedirs(RESULTS_FOLDER)


# ============================================================
# FASTA READER
# ============================================================

def read_fasta(filename):

    sequence = ""
    header = ""

    try:

        with open(filename, "r") as file:

            for line in file:

                line = line.strip()

                if line.startswith(">"):

                    header = line[1:]

                else:

                    sequence += line.upper()

        return header, sequence

    except FileNotFoundError:

        print("\nERROR: File not found:")
        print(filename)

        return None, None


# ============================================================
# VALIDATE DNA
# ============================================================

def validate_sequence(sequence):

    valid_bases = set("ATGC")

    return (
        len(sequence) > 0
        and set(sequence).issubset(valid_bases)
    )


# ============================================================
# NUCLEOTIDE COUNTS
# ============================================================

def nucleotide_counts(sequence):

    return {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C")
    }


# ============================================================
# GC CONTENT
# ============================================================

def gc_content(sequence):

    if len(sequence) == 0:
        return 0

    gc = sequence.count("G") + sequence.count("C")

    return (gc / len(sequence)) * 100


# ============================================================
# MUTATION ANALYSIS
# ============================================================

def compare_sequences(original, mutated):

    mutations = []

    transition_pairs = {
        ("A", "G"),
        ("G", "A"),
        ("C", "T"),
        ("T", "C")
    }

    transitions = 0
    transversions = 0

    for i in range(len(original)):

        original_base = original[i]
        mutated_base = mutated[i]

        if original_base != mutated_base:

            if (
                original_base,
                mutated_base
            ) in transition_pairs:

                mutation_type = "Transition"

                transitions += 1

            else:

                mutation_type = "Transversion"

                transversions += 1

            mutation = {
                "position": i + 1,
                "original": original_base,
                "mutated": mutated_base,
                "type": mutation_type
            }

            mutations.append(mutation)

    return mutations, transitions, transversions


# ============================================================
# READ FILES
# ============================================================

print("==============================================")
print("       VIRAL GENOME ANALYZER v5")
print("          FASTA FILE ANALYSIS")
print("==============================================")

print("\nReading genome files...")

original_header, original = read_fasta(
    ORIGINAL_FILE
)

mutated_header, mutated = read_fasta(
    MUTATED_FILE
)


# ============================================================
# CHECK FILES
# ============================================================

if original is None or mutated is None:

    print("\nProgram stopped.")

    exit()


# ============================================================
# VALIDATE SEQUENCES
# ============================================================

if not validate_sequence(original):

    print("\nERROR:")
    print("Original sequence contains invalid DNA bases.")

    exit()


if not validate_sequence(mutated):

    print("\nERROR:")
    print("Mutated sequence contains invalid DNA bases.")

    exit()


# ============================================================
# CHECK LENGTH
# ============================================================

if len(original) != len(mutated):

    print("\nERROR:")
    print("The two sequences have different lengths.")

    print(
        "Original:",
        len(original)
    )

    print(
        "Mutated:",
        len(mutated)
    )

    print(
        "\nVersion 5 currently compares"
        " sequences of equal length."
    )

    exit()


# ============================================================
# BASIC INFORMATION
# ============================================================

original_counts = nucleotide_counts(original)

mutated_counts = nucleotide_counts(mutated)

original_gc = gc_content(original)

mutated_gc = gc_content(mutated)


# ============================================================
# COMPARE GENOMES
# ============================================================

mutations, transitions, transversions = compare_sequences(
    original,
    mutated
)

total_mutations = len(mutations)

mutation_rate = (
    total_mutations / len(original)
) * 100


# ============================================================
# DISPLAY RESULTS
# ============================================================

print("\n==============================================")
print("                 GENOME INFO")
print("==============================================")

print(
    "Original genome:",
    original_header
)

print(
    "Mutated genome:",
    mutated_header
)

print(
    "Genome length:",
    len(original),
    "bases"
)


# ============================================================
# NUCLEOTIDE INFORMATION
# ============================================================

print("\n==============================================")
print("           NUCLEOTIDE COMPOSITION")
print("==============================================")

print("\nOriginal:")

for base in "ATGC":

    print(
        base,
        ":",
        original_counts[base]
    )


print("\nMutated:")

for base in "ATGC":

    print(
        base,
        ":",
        mutated_counts[base]
    )


print(
    "\nOriginal GC content:",
    round(original_gc, 2),
    "%"
)

print(
    "Mutated GC content:",
    round(mutated_gc, 2),
    "%"
)


# ============================================================
# MUTATION RESULTS
# ============================================================

print("\n==============================================")
print("             MUTATION ANALYSIS")
print("==============================================")

print(
    "\nTotal mutations:",
    total_mutations
)

print(
    "Mutation rate:",
    round(mutation_rate, 4),
    "%"
)

print(
    "Transitions:",
    transitions
)

print(
    "Transversions:",
    transversions
)


# ============================================================
# MUTATION TABLE
# ============================================================

if total_mutations > 0:

    print("\n----------------------------------------------")
    print("                 MUTATIONS")
    print("----------------------------------------------")

    print(
        f"{'Position':<12}"
        f"{'Original':<12}"
        f"{'Mutated':<12}"
        f"{'Type':<18}"
    )

    print("-" * 54)

    for mutation in mutations:

        print(
            f"{mutation['position']:<12}"
            f"{mutation['original']:<12}"
            f"{mutation['mutated']:<12}"
            f"{mutation['type']:<18}"
        )

else:

    print("\nNo mutations detected.")


# ============================================================
# GRAPH 1
# NUCLEOTIDE COMPOSITION
# ============================================================

bases = ["A", "T", "G", "C"]

original_values = [
    original_counts["A"],
    original_counts["T"],
    original_counts["G"],
    original_counts["C"]
]

mutated_values = [
    mutated_counts["A"],
    mutated_counts["T"],
    mutated_counts["G"],
    mutated_counts["C"]
]

x = range(len(bases))

plt.figure(figsize=(8, 5))

plt.bar(
    [i - 0.2 for i in x],
    original_values,
    width=0.4,
    label="Original"
)

plt.bar(
    [i + 0.2 for i in x],
    mutated_values,
    width=0.4,
    label="Mutated"
)

plt.xticks(
    list(x),
    bases
)

plt.xlabel("Nucleotide")

plt.ylabel("Number of Bases")

plt.title(
    "Genome Nucleotide Composition"
)

plt.legend()

plt.tight_layout()

plt.savefig(
    f"{RESULTS_FOLDER}/nucleotide_composition.png"
)

plt.show()


# ============================================================
# GRAPH 2
# MUTATION TYPES
# ============================================================

if total_mutations > 0:

    mutation_names = [
        "Transitions",
        "Transversions"
    ]

    mutation_values = [
        transitions,
        transversions
    ]

    plt.figure(figsize=(7, 5))

    plt.bar(
        mutation_names,
        mutation_values
    )

    plt.xlabel("Mutation Type")

    plt.ylabel("Number of Mutations")

    plt.title(
        "Mutation Type Distribution"
    )

    plt.tight_layout()

    plt.savefig(
        f"{RESULTS_FOLDER}/mutation_types.png"
    )

    plt.show()


# ============================================================
# GRAPH 3
# MUTATION POSITIONS
# ============================================================

if total_mutations > 0:

    positions = []

    for mutation in mutations:

        positions.append(
            mutation["position"]
        )

    plt.figure(figsize=(10, 4))

    plt.scatter(
        positions,
        [1] * len(positions)
    )

    plt.xlabel(
        "Position in Genome"
    )

    plt.ylabel(
        "Mutation"
    )

    plt.yticks([])

    plt.title(
        "Mutation Positions Along Genome"
    )

    plt.tight_layout()

    plt.savefig(
        f"{RESULTS_FOLDER}/mutation_positions.png"
    )

    plt.show()


# ============================================================
# SAVE TEXT REPORT
# ============================================================

report_file = (
    f"{RESULTS_FOLDER}/analysis_report.txt"
)

with open(report_file, "w") as report:

    report.write(
        "VIRAL GENOME ANALYZER v5\n"
    )

    report.write(
        "=========================\n\n"
    )

    report.write(
        f"Original genome: "
        f"{original_header}\n"
    )

    report.write(
        f"Mutated genome: "
        f"{mutated_header}\n\n"
    )

    report.write(
        f"Genome length: "
        f"{len(original)} bases\n\n"
    )

    report.write(
        "ORIGINAL NUCLEOTIDE COUNTS\n"
    )

    for base in "ATGC":

        report.write(
            f"{base}: "
            f"{original_counts[base]}\n"
        )

    report.write("\n")

    report.write(
        "MUTATED NUCLEOTIDE COUNTS\n"
    )

    for base in "ATGC":

        report.write(
            f"{base}: "
            f"{mutated_counts[base]}\n"
        )

    report.write("\n")

    report.write(
        f"Original GC content: "
        f"{original_gc:.2f}%\n"
    )

    report.write(
        f"Mutated GC content: "
        f"{mutated_gc:.2f}%\n\n"
    )

    report.write(
        f"Total mutations: "
        f"{total_mutations}\n"
    )

    report.write(
        f"Mutation rate: "
        f"{mutation_rate:.4f}%\n"
    )

    report.write(
        f"Transitions: "
        f"{transitions}\n"
    )

    report.write(
        f"Transversions: "
        f"{transversions}\n\n"
    )

    report.write(
        "MUTATION DETAILS\n"
    )

    report.write(
        "----------------\n"
    )

    for mutation in mutations:

        report.write(
            f"Position {mutation['position']}: "
            f"{mutation['original']} -> "
            f"{mutation['mutated']} "
            f"({mutation['type']})\n"
        )


# ============================================================
# FINISHED
# ============================================================

print("\n==============================================")
print("             ANALYSIS COMPLETE")
print("==============================================")

print("\nFiles created inside the results folder:")

print("1. nucleotide_composition.png")
print("2. mutation_types.png")
print("3. mutation_positions.png")
print("4. analysis_report.txt")

print("\nYour genome analysis is complete!")