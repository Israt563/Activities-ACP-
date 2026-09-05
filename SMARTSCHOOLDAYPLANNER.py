# ============================================================
# Smart School Day Planner (Pattern Matching & Structured Logic)
# ============================================================

print("=== Smart School Day Planner ===")
print("Answer 3 quick questions and I will plan your day!\n")

# --- PART 1: User Inputs & Boolean Conversion ---
day = input("What day is it? (Monday to Sunday): ").strip().title()
weather = input("What is the weather? (sunny / rainy / cloudy): ").strip().lower()

# Direct boolean flag evaluation
is_homework_done = input("Is your homework done? (yes / no): ").strip().lower() == "yes"
is_weekend = day in ("Saturday", "Sunday")

print(f"\n=== Your Plan for {day} ===")
print("-" * 35)

# --- PART 2: Data-Driven Lookup for Day Classification ---
day_descriptions = {
    "Monday": "First day of the week. Pack your weekly planner.",
    "Friday": "Last school day. Return library books today.",
    "Saturday": "Weekend - enjoy your free time!",
    "Sunday": "Weekend - enjoy your free time!",
    "Tuesday": "Regular school day. Stay focused!",
    "Wednesday": "Regular school day. Stay focused!",
    "Thursday": "Regular school day. Stay focused!",
}

# dict.get() provides a default message if the day isn't found
day_type = day_descriptions.get(day, "Day not recognised. Please check spelling.")
print(f"Day type    : {day_type}")

# --- PART 3: Short-Circuit Logic & Weather Tips ---
if weather == "sunny" and is_homework_done:
    print("After school: Head to the park - great weather and homework is done!")

if weather in ("rainy", "cloudy"):
    print("Weather tip : Pack your umbrella - it may get wet outside.")

if not is_homework_done:
    print("Homework    : Not done yet. Finish it before going out!")

# --- PART 4: Structural Pattern Matching (match-case) ---
# Evaluates a tuple of (weather, is_homework_done, is_weekend)
match (weather, is_homework_done, is_weekend):
    case ("rainy", False, _):
        best_plan = "Stay in, finish homework, then watch your favourite show."
    case ("sunny", True, False):
        best_plan = "All set for a great school day - you are prepared!"
    case ("sunny", _, True):
        best_plan = "Perfect weekend weather - head outside and have fun!"
    case _:
        best_plan = "Take it one step at a time - you have got this!"

print(f"Best plan   : {best_plan}\n")
print("Plan complete! Have a wonderful day!")
