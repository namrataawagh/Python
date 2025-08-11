# -------------------------------
# Python Comparison Operators
# -------------------------------
# Comparison operators are used to compare values.
# They return a Boolean value (True or False).

a = 10
b = 20

# -------------------------------
# Equal to (==)
# -------------------------------
print("--- Equal to (==) ---")
print("a == b:", a == b)  # False because 10 is not equal to 20
print("10 == 10:", 10 == 10)  # True

# -------------------------------
# Not equal to (!=)
# -------------------------------
print("\n--- Not equal to (!=) ---")
print("a != b:", a != b)  # True because 10 is not equal to 20
print("20 != 20:", 20 != 20)  # False

# -------------------------------
# Greater than (>)
# -------------------------------
print("\n--- Greater than (>) ---")
print("a > b:", a > b)  # False because 10 is not greater than 20
print("b > a:", b > a)  # True

# -------------------------------
# Less than (<)
# -------------------------------
print("\n--- Less than (<) ---")
print("a < b:", a < b)  # True because 10 is less than 20
print("b < a:", b < a)  # False

# -------------------------------
# Greater than or equal to (>=)
# -------------------------------
print("\n--- Greater than or equal to (>=) ---")
print("a >= b:", a >= b)  # False
print("10 >= 10:", 10 >= 10)  # True

# -------------------------------
# Less than or equal to (<=)
# -------------------------------
print("\n--- Less than or equal to (<=) ---")
print("a <= b:", a <= b)  # True
print("20 <= 10:", 20 <= 10)  # False

# -------------------------------
# Comparing Strings (Lexicographical Order)
# -------------------------------
print("\n--- Comparing Strings ---")
print("'apple' == 'apple':", "apple" == "apple")  # True
print("'apple' != 'banana':", "apple" != "banana")  # True
print("'apple' < 'banana':", "apple" < "banana")  # True ('a' comes before 'b')

# -------------------------------
# Comparing Different Data Types
# -------------------------------
print("\n--- Comparing Different Data Types ---")
print("True == 1:", True == 1)   # True because True is treated as 1
print("False == 0:", False == 0) # True because False is treated as 0
print("10 == 10.0:", 10 == 10.0) # True (int and float with same value are equal)

# -------------------------------
# Using Comparison in Conditions
# -------------------------------
print("\n--- Comparison in Conditions ---")
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
