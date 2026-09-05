# ================================
# GROCERY COST COMPARISON TOOL
# ================================

print("=== GROCERY COST COMPARISON TOOL ===")


# ---------- PART 1: what did this week's shop cost per person? ----------
rice_price = 12
milk_price = 4
fruit_price = 8
number_of_baskets = 2
family_members = 4

# parentheses force the addition to happen before the * and /
basket_cost_per_person = (rice_price + milk_price + fruit_price) * number_of_baskets / family_members

print("\nPART 1 - This week's shop")
print("Cost per person:", basket_cost_per_person)


# ---------- PART 2: can the items be shared equally? ----------
print("\nPART 2 - Sharing the items")

total_items = int(input("Enter the total number of grocery items: "))
people = int(input("Enter the number of people sharing them: "))

if people == 0:
    print("You cannot share items between 0 people.")
else:
    if total_items % people == 0:
        print(total_items, "items divide equally among", people, "people -", total_items // people, "each.")
    else:
        print(total_items, "items do not divide equally among", people, "people -", total_items % people, "left over.")


# ---------- PART 3: fix the weekly average ----------
print("\nPART 3 - Fixing the weekly average")

recorded_average = 65
total_weeks = 4
wrong_week_cost = 50
correct_week_cost = 80

recorded_total = recorded_average * total_weeks              # 65 x 4  = 260
corrected_total = recorded_total - wrong_week_cost + correct_week_cost   # 260 - 50 + 80 = 290
corrected_average = corrected_total / total_weeks            # 290 / 4 = 72.5

print("Recorded total was:", recorded_total)
print("Corrected total is:", corrected_total)
print("Corrected weekly average:", corrected_average)


# ---------- PART 4: compare with three stores ----------
print("\nPART 4 - Comparing the stores")

store_a_average = 70
store_b_average = 75
store_c_average = 80

print("Store A:", store_a_average, "| Store B:", store_b_average, "| Store C:", store_c_average)

if corrected_average < store_a_average and corrected_average < store_b_average and corrected_average < store_c_average:
    verdict = "cheaper than all three stores"
elif corrected_average > store_a_average and corrected_average > store_b_average and corrected_average > store_c_average:
    verdict = "more expensive than all three stores"
else:
    verdict = "somewhere in between the three stores"

print("Your average is", verdict)


# ---------- PART 5: the summary ----------
print("\n=== SUMMARY ===")
print("Cost per person this week:", basket_cost_per_person)
print("Corrected weekly average :", corrected_average)
print("Verdict                  :", verdict)
