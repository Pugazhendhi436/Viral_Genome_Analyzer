sequence = input("Enter a DNA sequence: ").upper().replace(" ", "")

# Check whether the sequence contains only valid DNA bases
valid_bases = set("ATGC")

if not sequence:
    print("No sequence entered.")

elif not set(sequence).issubset(valid_bases):
    print("Invalid DNA sequence!")
    print("Only A, T, G and C are allowed.")

else:
    length = len(sequence)

    A = sequence.count("A")
    T = sequence.count("T")
    G = sequence.count("G")
    C = sequence.count("C")

    GC_percentage = ((G + C) / length) * 100
    AT_percentage = ((A + T) / length) * 100

    print("\n===== VIRAL GENOME ANALYZER =====")

    print("Sequence length:", length)

    print("\nNucleotide counts:")
    print("A:", A)
    print("T:", T)
    print("G:", G)
    print("C:", C)

    print("\nNucleotide percentages:")
    print("A:", round((A / length) * 100, 2), "%")
    print("T:", round((T / length) * 100, 2), "%")
    print("G:", round((G / length) * 100, 2), "%")
    print("C:", round((C / length) * 100, 2), "%")

    print("\nGC content:", round(GC_percentage, 2), "%")
    print("AT content:", round(AT_percentage, 2), "%")