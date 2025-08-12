# -------------------------------
# Python for Loops
# -------------------------------
# A for loop is used for iterating over a sequence (list, tuple, dictionary, set, string, etc.)
# It repeats a block of code for each item in the sequence.

# -------------------------------
# Looping through a list
# -------------------------------
fruits = ["apple", "banana", "cherry"]

print("--- Loop through a list ---")
for fruit in fruits:
    print(fruit)  # Prints each fruit

# -------------------------------
# Looping through a string
# -------------------------------
print("\n--- Loop through a string ---")
for letter in "Python":
    print(letter)

# -------------------------------
# Using range() with for loops
# -------------------------------
print("\n--- Using range() ---")
for i in range(5):  # range(5) gives 0,1,2,3,4
    print(i)

print("\n--- range(start, end) ---")
for i in range(2, 6):  # 2 to 5
    print(i)

print("\n--- range(start, end, step) ---")
for i in range(0, 10, 2):  # Step of 2
    print(i)

# -------------------------------
# Looping through a dictionary
# -------------------------------
person = {"name": "John", "age": 30, "city": "New York"}

print("\n--- Loop through dictionary keys ---")
for key in person:
    print(key, ":", person[key])

print("\n--- Loop through dictionary items ---")
for key, value in person.items():
    print(key, "=", value)

# -------------------------------
# Using else with for loops
# -------------------------------
print("\n--- For loop with else ---")
for num in range(3):
    print(num)
else:
    print("Loop completed without break.")

# -------------------------------
# Break statement in for loops
# -------------------------------
print("\n--- Break in for loop ---")
for num in range(10):
    if num == 5:
        print("Stopping loop at", num)
        break
    print(num)

# -------------------------------
# Continue statement in for loops
# -------------------------------
print("\n--- Continue in for loop ---")
for num in range(5):
    if num == 2:
        continue  # Skip this iteration
    print(num)

# -------------------------------
# Nested for loops
# -------------------------------
print("\n--- Nested for loops ---")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana"]

for color in adj:
    for fruit in fruits:
        print(color, fruit)


# -------------------------------
# Tuple unpacking
# -------------------------------

print("\n--- Tuple unpacking ---")
mylist = [(1,2,3),(5,6,7),(8,9,10)]

for a in mylist:
    print(a)

for a,b,c in mylist:
    print(c)