import keyword

# List of words to test
test_words = ["for", "while", "lambda", "async", "variable", "main", "True", "true"]

print(f"Total Python keywords in this version: {len(keyword.kwlist)}\n")

# --- PART 1: Testing individual words using keyword.iskeyword() ---
print("--- Keyword Verification Check ---")
for word in test_words:
    # returns True if word is a reserved keyword
    is_kw = keyword.iskeyword(word) 
    print(f"Is '{word}' a reserved keyword? -> {is_kw}")

print("\n" + "=" * 45 + "\n")

# --- PART 2: Clean multi-column display of all keywords ---
print("--- All Reserved Keywords (Sorted Grid) ---")

# Print keywords in rows of 5 for easy scanning
kw_list = keyword.kwlist
for index in range(0, len(kw_list), 5):
    # Slice 5 keywords at a time and join with tab spacing
    row = kw_list[index : index + 5]
    print("".join(f"{kw:<12}" for kw in row))
