# -------------------------------
# WHILE LOOPS IN PYTHON
# -------------------------------

# Basic while loop example
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1  # Increment the counter


# --------------------------------
# Using while loop with a condition
# --------------------------------
number = 10
while number > 0:
    print("Number:", number)
    number -= 2  # Decrement by 2


# --------------------------------
# While loop with break statement
# --------------------------------
i = 1
while i <= 10:
    if i == 5:
        print("Breaking loop at i =", i)
        break  # Stop the loop completely
    print(i)
    i += 1


# --------------------------------
# While loop with continue statement
# --------------------------------
j = 0
while j < 5:
    j += 1
    if j == 3:
        print("Skipping 3")
        continue  # Skip this iteration
    print(j)


# --------------------------------
# While loop with else clause
# (Executes when loop ends normally without break)
# --------------------------------
k = 1
while k <= 3:
    print("K =", k)
    k += 1
else:
    print("Loop ended without break")


# --------------------------------
# Infinite loop example (use with caution!)
# --------------------------------
# Uncomment to test — stop with Ctrl+C in terminal
# while True:
#     user_input = input("Type 'exit' to stop: ")
#     if user_input.lower() == "exit":
#         print("Exiting loop...")
#         break


# --------------------------------
# While loop for validating user input
# --------------------------------
user_age = ""
while not user_age.isdigit():  # Keep looping until valid number
    user_age = input("Enter your age: ")

print("Your age is:", user_age)


# --------------------------------
# Nested while loop example
# --------------------------------
x = 1
while x <= 3:
    y = 1
    while y <= 2:
        print(f"x={x}, y={y}")
        y += 1
    x += 1


# --------------------------------
# While loop with a list (pop elements)
# --------------------------------
tasks = ["task1", "task2", "task3"]
while tasks:  # Loop runs while list is not empty
    task = tasks.pop(0)  # Remove first item
    print("Processing:", task)

