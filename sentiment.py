import sys

# Safe import check for external third-party library
try:
    from textblob import TextBlob
except ImportError:
    sys.exit("Error: 'textblob' module not installed. Install it via 'pip install textblob'.")

# --- User Setup & Greeting ---
user_name = input("Enter your name: ").strip().title() or "Agent"
print(f"\nWelcome, {user_name}! Type any text to analyze sentiment (or 'exit' to quit).\n")

# --- Sentiment Threshold Mapping ---
# Maps conditions to (Emoji, Sentiment Category)
def analyze_polarity(polarity: float) -> tuple[str, str]:
    if polarity > 0:
        return "\U0001F642", "Positive"  # Slightly smiling face
    elif polarity < 0:
        return "\U0001F641", "Negative"  # Slightly frowning face
    return "\U0001F640", "Neutral"       # Weary/Neutral cat face

# --- Main Interaction Loop using Walrus Operator (:=) ---
# Continually prompts for input until user types 'exit'
while (text_input := input("Sequence > ").strip()).lower() != 'exit':
    
    # Skip empty lines without processing sentiment
    if not text_input:
        print("Please enter a valid text sequence.\n")
        continue

    # Sentiment extraction
    blob = TextBlob(text_input)
    polarity_score = blob.sentiment.polarity
    emoji, sentiment_label = analyze_polarity(polarity_score)

    # Output formatting using f-strings and precision rounding
    print(f"[{sentiment_label}] {emoji} | Polarity Score: {polarity_score:+.2f}\n")

# Exit Message
print(f"\nGoodbye, {user_name}! Have a great day.")
