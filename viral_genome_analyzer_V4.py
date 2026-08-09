# ==========================================
# VIRAL GENOME ANALYZER - VERSION 4
# MUTATION ANALYSIS + VISUALIZATION
# ==========================================

import matplotlib.pyplot as plt

print("==========================================")
print("       VIRAL GENOME ANALYZER v4")
print("        MUTATION VISUALIZATION")
print("==========================================")

# ==========================================
# INPUT
# ==========================================

original = input("\nEnter the ORIGINAL DNA sequence: ").upper().replace(" ", "")
mutated = input("Enter the MUTATED DNA sequence: ").upper().replace(" ", "")

# ==========================================
# VALIDATION
# ==========================================

valid_bases = set("ATGC")

if not original or not mutated:
    print("\nERROR: Both sequences must be entered.")
    exit()

if not set(original).issubset(valid_bases):
    print("\nERROR: Original sequence contains invalid bases.")
    exit()

if not set(mutated).issubset(valid_bases):
    print("\nERROR: Mutated sequence contains invalid bases.")
    exit()

if len(original) != len(mutated):
    print("\nERROR: Both sequences must have the same length.")
    exit()

# ==========================================
# MUTATION ANALYSIS
# ==========================================

mutations = []

transitions = 0
transversions = 0

transition_pairs = {
    ("A", "G"),
    ("G", "A"),
    ("C", "T"),
    ("T", "C")
}

for i in range(len(original)):

    old_base = original[i]
    new_base = mutated[i]

    if old_base != new_base:

        if (old_base, new_base) in transition_pairs:
            mutation_type = "Transition"
            transitions += 1

        else:
            mutation_type = "Transversion"
            transversions += 1

        mutations.append({
            "position": i + 1,
            "original": old_base,
            "mutated": new_base,
            "type": mutation_type
        })

# ==========================================
# BASIC RESULTS
# ==========================================

total_mutations = len(mutations)

mutation_rate = (
    total_mutations / len(original)
) * 100

print("\n==========================================")
print("                 RESULTS")
print("==========================================")

print("Sequence length:", len(original))
print("Total mutations:", total_mutations)
print("Mutation rate:", round(mutation_rate, 4), "%")

print("\nTransitions:", transitions)
print("Transversions:", transversions)

# ==========================================
# MUTATION TABLE
# ==========================================

if total_mutations == 0:

    print("\nNo mutations detected.")

else:

    print("\n------------------------------------------")
    print("              MUTATION TABLE")
    print("------------------------------------------")

    print(
        f"{'Position':<10}"
        f"{'Original':<10}"
        f"{'Mutated':<10}"
        f"{'Type':<15}"
    )

    print("-" * 45)

    for mutation in mutations:

        print(
            f"{mutation['position']:<10}"
            f"{mutation['original']:<10}"
            f"{mutation['mutated']:<10}"
            f"{mutation['type']:<15}"
        )

# ==========================================
# GRAPH 1
# NUCLEOTIDE COMPOSITION
# ==========================================

bases = ["A", "T", "G", "C"]

original_counts = [
    original.count("A"),
    original.count("T"),
    original.count("G"),
    original.count("C")
]

mutated_counts = [
    mutated.count("A"),
    mutated.count("T"),
    mutated.count("G"),
    mutated.count("C")
]

x = range(len(bases))

plt.figure(figsize=(8, 5))

plt.bar(
    [i - 0.2 for i in x],
    original_counts,
    width=0.4,
    label="Original"
)

plt.bar(
    [i + 0.2 for i in x],
    mutated_counts,
    width=0.4,
    label="Mutated"
)

plt.xticks(list(x), bases)

plt.xlabel("Nucleotide")
plt.ylabel("Count")

plt.title("Nucleotide Composition")

plt.legend()

plt.tight_layout()

plt.show()

# ==========================================
# GRAPH 2
# TRANSITION VS TRANSVERSION
# ==========================================

if total_mutations > 0:

    mutation_types = [
        "Transitions",
        "Transversions"
    ]

    mutation_counts = [
        transitions,
        transversions
    ]

    plt.figure(figsize=(7, 5))

    plt.bar(
        mutation_types,
        mutation_counts
    )

    plt.xlabel("Mutation Type")
    plt.ylabel("Number of Mutations")

    plt.title("Transition vs Transversion")

    plt.tight_layout()

    plt.show()

# ==========================================
# GRAPH 3
# MUTATION POSITIONS
# ==========================================

if total_mutations > 0:

    positions = []

    for mutation in mutations:
        positions.append(mutation["position"])

    plt.figure(figsize=(10, 4))

    plt.scatter(
        positions,
        [1] * len(positions)
    )

    plt.xlabel("Position in DNA Sequence")

    plt.yticks([])

    plt.title("Mutation Positions Along DNA Sequence")

    plt.tight_layout()

    plt.show()

# ==========================================
# SAVE RESULTS
# ==========================================

with open("mutation_results.txt", "w") as file:

    file.write("VIRAL GENOME ANALYZER v4\n")
    file.write("========================\n\n")

    file.write(
        f"Sequence length: {len(original)}\n"
    )

    file.write(
        f"Total mutations: {total_mutations}\n"
    )

    file.write(
        f"Mutation rate: {mutation_rate:.4f}%\n\n"
    )

    file.write(
        f"Transitions: {transitions}\n"
    )

    file.write(
        f"Transversions: {transversions}\n\n"
    )

    for mutation in mutations:

        file.write(
            f"Position {mutation['position']}: "
            f"{mutation['original']} -> "
            f"{mutation['mutated']} "
            f"({mutation['type']})\n"
        )

print("\n==========================================")
print("       ANALYSIS COMPLETE")
print("==========================================")

print("\nResults saved to:")
print("mutation_results.txt")