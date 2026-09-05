from dataclasses import dataclass, asdict

# --- PART 1 & 2: Define Data Structure & Collect Details ---
@dataclass
class AgentProfile:
    name: str
    gadget: str
    agent_number: int = 7
    speed_rating: float = 9.5
    mission_count: int = 12
    height_m: float = 1.65
    is_active: bool = True

# Instantiate agent details
agent = AgentProfile(
    name=input("Enter your real name, Agent: "),
    gadget=input("Enter your favorite gadget: ")
)

# --- PART 3 & 4: Dynamic Type Inspection & Casting ---
profile_dict = asdict(agent)

print("\n--- Original Data Types ---")
for key, value in profile_dict.items():
    formatted_key = key.replace('_', ' ').title()
    print(f"{formatted_key:<15}: {value!r:<12} -> type: {type(value).__name__}")

# Convert non-string values into strings using a dictionary comprehension
text_converted = {k: str(v) for k, v in profile_dict.items()}

print("\n--- Converted Data Types (Strings) ---")
for key, value in text_converted.items():
    formatted_key = key.replace('_', ' ').title()
    print(f"{formatted_key:<15} as text: '{value}' -> type: {type(value).__name__}")

# --- PART 5 & 6: Slicing & Code Generation ---
# Pythonic slicing: name[:3] is shorthand for name[0:3], name[-1] gets last char
code_name = f"{agent.name[:3]}{agent.name[-1]}".upper()
reversed_gadget = agent.gadget[::-1].upper()

print(f"\nSecret Code Name    : {code_name}")
print(f"Reversed Gadget Name: {reversed_gadget}")

# --- PART 7 & 8: Formatted Badge Output ---
badge = f"""
===============================
===== SECRET AGENT BADGE ======
AGENT {code_name}
ID: {text_converted['agent_number']} | MISSIONS: {text_converted['mission_count']}
SPEED: {text_converted['speed_rating']} | ACTIVE: {text_converted['is_active']}
SECRET GADGET CODE: {reversed_gadget}
===============================
"""

print(badge)
