# -------------------------------
# Python Variables & Naming Rules
# -------------------------------

# Variables store data values in Python.
# You don't need to declare a type, Python decides it automatically.
# Python uses Dynamic typing: meaning you can reassign variables to different data types

# Example of assigning variables
x = 10                # Integer
name = "Alice"        # String
is_active = True      # Boolean

print("x:", x)
print("name:", name)
print("is_active:", is_active)

# -------------------------------
# Rules for Variable Names:
# -------------------------------
# 1. Must start with a letter or underscore (_)
# 2. Cannot start with a number
# 3. Can only contain letters, numbers, and underscores (A-Z, a-z, 0-9, _)
# 4. Case-sensitive (age, Age, and AGE are different variables)
# 5. Cannot be a Python keyword (like 'class', 'for', 'if', etc.)

my_var = 100
_var123 = "Python"
name1 = "John"
AGE = 25  # Uppercase is fine, often used for constants

# Invalid variable names (will cause errors if uncommented)
# 2name = "Invalid"   # Starts with a number
# my-var = 10         # Hyphen not allowed
# for = "loop"        # 'for' is a reserved keyword

# -------------------------------
# Multiple Assignments
# -------------------------------
a, b, c = 1, 2, 3
print("a:", a, "b:", b, "c:", c)

# Assign the same value to multiple variables
x = y = z = 0
print("x:", x, "y:", y, "z:", z)

# -------------------------------
# Constants (by convention)
# -------------------------------
# Python has no true constants, but we use uppercase to indicate they shouldn't change
PI = 3.14159
GRAVITY = 9.8
print("PI:", PI)
print("Gravity:", GRAVITY)
