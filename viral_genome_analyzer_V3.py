# ==========================================
# VIRAL GENOME ANALYZER - VERSION 3
# MUTATION CLASSIFICATION
# ==========================================

print("==========================================")
print("       VIRAL GENOME ANALYZER v3")
print("          MUTATION CLASSIFIER")
print("==========================================")

# Get DNA sequences
original = input("\nEnter the ORIGINAL DNA sequence: ").upper().replace(" ", "")
mutated = input("Enter the MUTATED DNA sequence: ").upper().replace(" ", "")

# Valid DNA bases
valid_bases = set("ATGC")

# Check for empty sequences
if not original or not mutated:
    print("\nERROR: Both sequences must be entered.")

# Check for invalid characters
elif not set(original).issubset(valid_bases):
    print("\nERROR: Original sequence contains invalid characters.")

elif not set(mutated).issubset(valid_bases):
    print("\nERROR: Mutated sequence contains invalid characters.")

# Sequences must have equal length
elif len(original) != len(mutated):
    print("\nERROR: Both sequences must have the same length.")

else:

    # Lists to store mutation information
    mutations = []

    transitions = 0
    transversions = 0

    # Transition pairs
    transition_pairs = {
        ("A", "G"),
        ("G", "A"),
        ("C", "T"),
        ("T", "C")
    }

    # Compare the sequences
    for i in range(len(original)):

        old_base = original[i]
        new_base = mutated[i]

        # If bases are different
        if old_base != new_base:

            # Determine mutation type
            if (old_base, new_base) in transition_pairs:
                mutation_type = "Transition"
                transitions += 1

            else:
                mutation_type = "Transversion"
                transversions += 1

            # Store mutation
            mutations.append({
                "position": i + 1,
                "original": old_base,
                "mutated": new_base,
                "type": mutation_type
            })

    # ==========================================
    # RESULTS
    # ==========================================

    print("\n==========================================")
    print("                 RESULTS")
    print("==========================================")

    print("Original sequence length:", len(original))
    print("Mutated sequence length:", len(mutated))

    total_mutations = len(mutations)

    print("\nTotal mutations:", total_mutations)

    # Mutation rate
    mutation_rate = (total_mutations / len(original)) * 100

    print("Mutation rate:", round(mutation_rate, 4), "%")

    # ==========================================
    # MUTATION TABLE
    # ==========================================

    if total_mutations == 0:

        print("\nNo mutations detected!")

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
    # SUMMARY
    # ==========================================

    print("\n==========================================")
    print("             MUTATION SUMMARY")
    print("==========================================")

    print("Transitions:", transitions)
    print("Transversions:", transversions)

    if total_mutations > 0:

        transition_percentage = (
            transitions / total_mutations
        ) * 100

        transversion_percentage = (
            transversions / total_mutations
        ) * 100

        print(
            "Transition percentage:",
            round(transition_percentage, 2),
            "%"
        )

        print(
            "Transversion percentage:",
            round(transversion_percentage, 2),
            "%"
        )

    print("\n==========================================")
    print("            ANALYSIS COMPLETE")
    print("==========================================")