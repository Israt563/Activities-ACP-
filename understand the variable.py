# --- Multi-variable Unpacking & Direct Assignment ---
x, y = 5, "John"
company = "Codingal"

# Print using concise f-string representations
print(f"Number: {x}")
print(f"Name: {y}")
print(f"Company: {company}\n")

# --- Interactive Input with Fallback Default ---
# strip() removes accidental whitespace; 'or' provides a default if blank
user_name = input("Enter your name: ").strip().title() or "Guest"

# --- Clean Multiline Output ---
welcome_message = f"""
Hello, {user_name}!
Welcome to {company}.
"""

print(welcome_message)
