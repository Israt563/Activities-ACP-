# ================================
# SWIMMING POOL ENTRY CHECKER
# ================================

print("=== Swimming Pool Entry Checker ===")
print("Answer 3 questions and I will tell you which pool you can use.\n")

age = int(input("How old are you? "))
can_swim = input("Can you swim 25 metres? (yes / no): ").lower()
adult_here = input("Is an adult with you? (yes / no): ").lower()

print()
print("=== Entry Decision ===")
print("-" * 32)


# ---------- PART 1: age group - narrowest condition FIRST ----------
if age < 4:
    print("Age group   : Toddler - splash pool only, always with an adult.")
elif age < 12:
    print("Age group   : Child - main pool with an adult.")
elif age < 18:
    print("Age group   : Teen - main pool alone if you can swim.")
else:
    print("Age group   : Adult - all pools open to you.")


# ---------- PART 2: did they actually answer yes or no? ----------
# 'and' because an unrecognised answer is neither yes nor no
if can_swim != "yes" and can_swim != "no":
    print("Input error : Please answer the swimming question with yes or no.")
    swim_known = False
else:
    swim_known = True

if adult_here != "yes" and adult_here != "no":
    print("Input error : Please answer the adult question with yes or no.")
    adult_known = False
else:
    adult_known = True


# ---------- PART 3: AND - both required to grant the deep pool ----------
if can_swim == "yes" and adult_here == "yes":
    print("Deep pool   : Allowed - you can swim and an adult is present.")


# ---------- PART 4: OR - either one is enough to raise the caution ----------
if age < 12 or can_swim == "no":
    print("Shallow only: Stay in the shallow end today.")


# ---------- PART 5: NOT - but only once we trust the answer ----------
if adult_known == True and not (adult_here == "yes"):
    print("Reminder    : No adult with you - the lifeguard must be told.")


# ---------- PART 6: the verdict - refusal FIRST ----------
if swim_known == False or adult_known == False:
    print("Verdict     : Cannot decide until both questions are answered properly.")
elif age >= 18 and can_swim == "yes":
    print("Verdict     : Full access. Enjoy your swim.")
elif age >= 12 and can_swim == "yes" and adult_here == "yes":
    print("Verdict     : Main pool access with your adult nearby.")
elif can_swim == "no" and not (adult_here == "yes"):
    print("Verdict     : Shallow end only, and please find an adult first.")
else:
    print("Verdict     : Shallow end today - come back with an adult for more.")


print()
print("Have a safe swim!")
