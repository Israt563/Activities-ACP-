# ============================================================
# Student Grade Evaluator
# ============================================================

# --- Part 1: Collect & Validate Marks with a Loop ---
marks = []
NUM_SUBJECTS = 5

print(f"Enter Marks Obtained in {NUM_SUBJECTS} Subjects:")

for i in range(1, NUM_SUBJECTS + 1):
    score = int(input(f"Subject {i}: "))
    marks.append(score)

# --- Part 2: Calculate Total & Average ---
tot = sum(marks)
avg = tot / NUM_SUBJECTS  # Float division preserves accuracy

print(f"\nTotal Marks : {tot} / {NUM_SUBJECTS * 100}")
print(f"Average     : {avg:.2f}")

# Check overall input validity (all marks must be between 0 and 100)
if any(m < 0 or m > 100 for m in marks):
    print("Invalid Input! Individual subject marks must be 0–100.")

else:
    # --- Part 3: Efficient Grade Lookup ---
    # Tuple format: (Minimum Average, Grade String)
    grade_thresholds = [
        (91, "A1"), (81, "A2"), (71, "B1"), (61, "B2"),
        (51, "C1"), (41, "C2"), (33, "D"),  (21, "E1"), (0, "E2")
    ]

    # Evaluate grade based on descending thresholds
    assigned_grade = "Invalid"
    for min_score, grade in grade_thresholds:
        if avg >= min_score:
            assigned_grade = grade
            break

    print(f"Your Grade is {assigned_grade}")
