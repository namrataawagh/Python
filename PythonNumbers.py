## -------------------------------
# Python Numbers & Math Examples
# -------------------------------

# Python has three main numeric types:
# 1. int   -> Whole numbers
# 2. float -> Decimal numbers
# 3. complex -> Complex numbers (a + bj)

# Integer
x = 10
print("Integer:", x, "| Type:", type(x))

# Float
y = 3.14
print("Float:", y, "| Type:", type(y))

# Complex number
z = 2 + 3j
print("Complex:", z, "| Type:", type(z))


# -------------------------------
# Basic Arithmetic Operations
# -------------------------------

a = 15
b = 4

print("\n--- Arithmetic Operations ---")
print("Addition:", a + b)        # 15 + 4 = 19
print("Subtraction:", a - b)     # 15 - 4 = 11
print("Multiplication:", a * b)  # 15 * 4 = 60
print("Division:", a / b)        # 15 / 4 = 3.75 (quotient)
print("Floor Division:", a // b) # 15 // 4 = 3 (removes decimal)
print("Modulus:", a % b)         # 15 % 4 = 3 (remainder)
print("Exponent:", a ** b)       # 15^4 = 50625


# -------------------------------
# Using Python's math module
# -------------------------------
import math

print("\n--- Math Module Functions ---")
print("Square root of 16:", math.sqrt(16))     # 4.0
print("Power (2^3):", math.pow(2, 3))          # 8.0
print("Absolute value:", math.fabs(-7.5))      # 7.5
print("Factorial of 5:", math.factorial(5))    # 120
print("Value of Pi:", math.pi)                 # 3.141592...
print("Value of e:", math.e)                   # 2.718281...

# -------------------------------
# Rounding Numbers
# -------------------------------
print("\n--- Rounding Examples ---")
num = 5.6789
print("Round to 2 decimal places:", round(num, 2))  # 5.68
print("Round to nearest integer:", round(num))      # 6
