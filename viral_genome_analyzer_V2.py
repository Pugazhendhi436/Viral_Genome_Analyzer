# ==========================================
# VIRAL GENOME ANALYZER - VERSION 2
# DNA SEQUENCE COMPARISON
# ==========================================

print("======================================")
print("      VIRAL GENOME ANALYZER v2")
print("        DNA SEQUENCE COMPARISON")
print("======================================")

# Get sequences from the user
original = input("\nEnter the ORIGINAL DNA sequence: ").upper().replace(" ", "")
mutated = input("Enter the MUTATED DNA sequence: ").upper().replace(" ", "")

# Valid DNA bases
valid_bases = set("ATGC")

# Check sequences
if not original or not mutated:
    print("\nError: Both sequences must be entered.")

elif not set(original).issubset(valid_bases):
    print("\nError: Original sequence contains invalid bases.")

elif not set(mutated).issubset(valid_bases):
    print("\nError: Mutated sequence contains invalid bases.")

elif len(original) != len(mutated):
    print("\nError: The two sequences must have the same length.")

else:

    # Count mutations
    mutations = []

    for i in range(len(original)):

        if original[i] != mutated[i]:

            mutations.append({
                "position": i + 1,
                "original": original[i],
                "mutated": mutated[i]
            })

    # Display results
    print("\n======================================")
    print("             RESULTS")
    print("======================================")

    print("Original sequence length:", len(original))
    print("Mutated sequence length:", len(mutated))

    print("\nTotal mutations:", len(mutations))

    # Mutation rate
    mutation_rate = (len(mutations) / len(original)) * 100

    print("Mutation rate:", round(mutation_rate, 4), "%")

    # Display mutations
    if len(mutations) == 0:

        print("\nNo mutations detected!")

    else:

        print("\n--------------------------------------")
        print("             MUTATIONS")
        print("--------------------------------------")

        for mutation in mutations:

            print(
                "Position:",
                mutation["position"],
                "|",
                mutation["original"],
                "→",
                mutation["mutated"]
            )

    print("\n======================================")
    print("             ANALYSIS COMPLETE")
    print("======================================")