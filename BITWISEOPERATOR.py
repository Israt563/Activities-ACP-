# Function to print decimal value alongside its binary representation
def show_bits(label, val):
    # bin() returns string like '0b1010' or '-0b1010'
    print(f"{label:<12}: {val:>3} | Binary: {bin(val)}")

# --- Bitwise Right Shift (>>) ---
a = 12
b = -12
shift = 2

print("=== BITWISE RIGHT SHIFT (Floor Division by 2^n) ===")
show_bits("Original a", a)
show_bits(f"a >> {shift}", a >> shift)  # Equivalent to 12 // (2**2) = 3

print("-" * 45)
show_bits("Original b", b)
show_bits(f"b >> {shift}", b >> shift)  # Equivalent to -12 // (2**2) = -3

print("\n" + "=" * 45 + "\n")

# --- Bitwise Left Shift (<<) ---
a = 7
b = -7

print("=== BITWISE LEFT SHIFT (Multiplication by 2^n) ===")
show_bits("Original a", a)
show_bits(f"a << {shift}", a << shift)  # Equivalent to 7 * (2**2) = 28

print("-" * 45)
show_bits("Original b", b)
show_bits(f"b << {shift}", b << shift)  # Equivalent to -7 * (2**2) = -28
