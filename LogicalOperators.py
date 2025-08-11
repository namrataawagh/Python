# -------------------------------
# Python Logical Operators
# -------------------------------
# Logical operators are used to combine conditional statements.
# They return a Boolean value (True or False).

# Logical operators:
# and → True if both conditions are True
# or  → True if at least one condition is True
# not → Reverses the Boolean value (True → False, False → True)

# Example variables
x = 10
y = 20
z = 5

# -------------------------------
# AND Operator
# -------------------------------
print("--- AND Operator ---")
print("(x < y) and (y < 30):", (x < y) and (y < 30))   # True and True → True
print("(x < y) and (y > 30):", (x < y) and (y > 30))   # True and False → False
print("(x > y) and (z < x):", (x > y) and (z < x))     # False and True → False

# -------------------------------
# OR Operator
# -------------------------------
print("\n--- OR Operator ---")
print("(x < y) or (y > 30):", (x < y) or (y > 30))     # True or False → True
print("(x > y) or (z < x):", (x > y) or (z < x))       # False or True → True
print("(x > y) or (z > y):", (x > y) or (z > y))       # False or False → False

# -------------------------------
# NOT Operator
# -------------------------------
print("\n--- NOT Operator ---")
print("not(x < y):", not (x < y))  # not(True) → False
print("not(x > y):", not (x > y))  # not(False) → True

# -------------------------------
# Combining Logical Operators
# -------------------------------
print("\n--- Combining Logical Operators ---")
print("(x < y) and (y < 30) or (z > 10):", (x < y) and (y < 30) or (z > 10))
# Step-by-step: (True and True) → True, then True or False → True

print("not(x < y) or (z < y):", not (x < y) or (z < y))
# Step-by-step: not(True) → False, then False or True → True

# -------------------------------
# Logical Operators in Conditions
# -------------------------------
print("\n--- Logical Operators in Conditions ---")
age = 25
country = "USA"

if (age >= 18) and (country == "USA"):
    print("Eligible to vote in the USA.")
else:
    print("Not eligible to vote in the USA.")

if (age < 18) or (country != "USA"):
    print("Either too young or not from the USA.")
else:
    print("Meets both criteria.")

# -------------------------------
# Short-Circuit Behavior
# -------------------------------
print("\n--- Short-Circuit Evaluation ---")
# In 'and', if the first condition is False, Python won't check the second.
# In 'or', if the first condition is True, Python won't check the second.
print("(x > y) and (z < x):", (x > y) and (z < x))  # Stops at first False
print("(x < y) or (z > y):", (x < y) or (z > y))    # Stops at first True
