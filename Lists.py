# -------------------------------
# Python Lists & List Operations
# -------------------------------

# Lists are ordered, changeable (mutable) collections that can store mixed data types
my_list = [10, 20, 30, 40, 50]
mixed_list = [1, "Hello", 3.14, True]

print("List:", my_list)
print("Mixed List:", mixed_list)

# -------------------------------
# Accessing List Elements
# -------------------------------
print("\n--- Accessing Elements ---")
print("First element:", my_list[0])   # Index starts at 0
print("Last element:", my_list[-1])   # Negative index from end

# -------------------------------
# Slicing Lists
# -------------------------------
print("\n--- Slicing ---")
print("Elements from index 1 to 3:", my_list[1:4])   # [20, 30, 40]
print("From start to index 2:", my_list[:3])         # [10, 20, 30]
print("From index 2 to end:", my_list[2:])           # [30, 40, 50]
print("Every 2nd element:", my_list[::2])            # [10, 30, 50]

# -------------------------------
# Modifying Lists
# -------------------------------
print("\n--- Modifying Lists ---")
my_list[0] = 100  # Change first element
print("After modifying first element:", my_list)

# -------------------------------
# Adding Elements
# -------------------------------
print("\n--- Adding Elements ---")
my_list.append(60)                # Add at end
print("After append:", my_list)
my_list.insert(2, 25)              # Insert at index 2
print("After insert:", my_list)
my_list.extend([70, 80])           # Add multiple elements
print("After extend:", my_list)

# -------------------------------
# Removing Elements
# -------------------------------
print("\n--- Removing Elements ---")
my_list.remove(25)                 # Remove first occurrence of value
print("After remove:", my_list)
popped_item = my_list.pop()        # Remove last element
print("After pop (last element):", my_list, "| Popped:", popped_item)
my_list.pop(1)                     # Remove element at index 1
print("After pop index 1:", my_list)
del my_list[0]                     # Delete element at index 0
print("After del index 0:", my_list)

# -------------------------------
# List Functions
# -------------------------------
numbers = [5, 2, 9, 1, 5, 6]
print("\n--- List Functions ---")
print("Length:", len(numbers))
print("Min value:", min(numbers))
print("Max value:", max(numbers))
print("Sum:", sum(numbers))
print("Count of 5:", numbers.count(5))
print("Reverse list:",numbers.reverse())
# -------------------------------
# Sorting Lists
# -------------------------------
print("\n--- Sorting ---")
numbers.sort()       # Ascending sort
print("Ascending:", numbers)
numbers.sort(reverse=True)  # Descending sort
print("Descending:", numbers)

# -------------------------------
# Looping Through Lists
# -------------------------------
print("\n--- Looping ---")
for item in numbers:
    print(item, end=" ")

# -------------------------------
# List Comprehension
# -------------------------------
print("\n\n--- List Comprehension ---")
squares = [x**2 for x in range(5)]
print("Squares:", squares)
