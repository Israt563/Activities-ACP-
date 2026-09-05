# ============================================================
# Weather Outfit Picker (Pythonic Refactoring)
# ============================================================

# --- PART 1: Inputs & Sanitization ---
temperature = int(input("Enter today's temperature in Celsius: "))
is_raining = input("Is it raining today? (yes/no): ").strip().lower() == "yes"
wind_speed = int(input("Enter the wind speed in km/h: "))
has_puddles = input("Are there puddles on the ground? (yes/no): ").strip().lower() == "yes"

# --- PART 2: Conditional Decisions using Ternary Operators ---
outfit = "jacket" if temperature < 20 else "t-shirt"
temp_desc = "cold" if temperature < 20 else "warm"

needs_windbreaker = wind_speed > 30
wind_desc = "windy" if needs_windbreaker else "calm"

shoes = "boots" if has_puddles else "sneakers"
ground_desc = "wet" if has_puddles else "dry"

# --- PART 3: Weather Reminders ---
print(f"\nIt is {temp_desc} today. Wear a {outfit}.")
if is_raining:
    print("Bring an umbrella!")

print(f"It is {wind_desc} today. " + 
      (f"Wear a windbreaker over your {outfit}." if needs_windbreaker else f"No windbreaker needed over your {outfit}."))

print(f"The ground is {ground_desc}. Wear {shoes}.")

# --- PART 4: Structured Data Storage & Summary Display ---
outfit_summary = {
    "Temperature": f"{temperature}°C",
    "Outfit Chosen": outfit,
    "Raining": "yes" if is_raining else "no",
    "Windbreaker Needed": "yes" if needs_windbreaker else "no",
    "Shoes Chosen": shoes
}

print("\nWeather check complete!")
print("=" * 35)
print(f"{'WEATHER OUTFIT PICKER':^35}")
print("=" * 35)

for key, value in outfit_summary.items():
    print(f"{key:<20}: {value}")

print("=" * 35)
