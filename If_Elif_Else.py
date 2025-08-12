# -------------------------------
# Python if, elif, else Statements
# -------------------------------
# These are conditional statements used to control the flow of a program
# based on certain conditions.

# -------------------------------
# Basic if statement
# -------------------------------
x = 10

if x > 5:  # Condition to check
    print("x is greater than 5")  # Runs if condition is True

# -------------------------------
# if-else statement
# -------------------------------
age = 17

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# -------------------------------
# if-elif-else statement
# -------------------------------
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# -------------------------------
# Multiple conditions with and/or
# -------------------------------
temperature = 25
weather = "sunny"

if temperature > 20 and weather == "sunny":
    print("It's a nice warm sunny day!")
elif temperature > 20 and weather != "sunny":
    print("It's warm but not sunny.")
else:
    print("It might be cold today.")

# -------------------------------
# Nested if statements
# -------------------------------
number = 15

if number > 0:
    print("Positive number")
    if number % 2 == 0:
        print("It's even.")
    else:
        print("It's odd.")
else:
    print("Negative number or zero")

# -------------------------------
# Short-hand if (single-line if)
# -------------------------------
y = 7
if y > 5: print("y is greater than 5")

# -------------------------------
# Short-hand if-else (ternary operator)
# -------------------------------
age = 20
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)
