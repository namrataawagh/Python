# -------------------------------
# Python Sets & Operations
# -------------------------------

# Sets are unordered collections of unique elements
# Mutable (can add/remove items), but cannot contain mutable items like lists
# Duplicate values are automatically removed

# Creating sets
my_set = {10, 20, 30, 40, 50}
mixed_set = {1, "Hello", 3.14, True}  # True counts as 1, so avoid mixing with integers
duplicate_set = {1, 2, 2, 3, 3, 3}    # Duplicates removed automatically

print("Set:", my_set)
print("Mixed Set:", mixed_set)
print("Duplicate removal:", duplicate_set)
print("Type:", type(my_set))

# -------------------------------
# Creating a set using set() function
# -------------------------------
new_set = set([5, 6, 7, 7, 8])
print("Set from list:", new_set)

# -------------------------------
# Adding & Removing Elements
# -------------------------------
print("\n--- Adding & Removing ---")
my_set.add(60)          # Add single element
print("After add:", my_set)

my_set.update([70, 80]) # Add multiple elements
print("After update:", my_set)

my_set.remove(20)       # Remove specific element (error if not found)
print("After remove:", my_set)

my_set.discard(100)     # Discard element (no error if not found)
print("After discard:", my_set)

popped_item = my_set.pop()  # Remove and return random element
print("After pop:", my_set, "| Popped:", popped_item)

# -------------------------------
# Set Operations
# -------------------------------
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("\n--- Set Operations ---")
print("Union:", set_a | set_b)           # OR operator
print("Intersection:", set_a & set_b)    # AND operator
print("Difference (A - B):", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)  # Elements not in both

# -------------------------------
# Checking Membership
# -------------------------------
print("\n--- Membership ---")
print("Is 3 in set_a?", 3 in set_a)
print("Is 7 not in set_b?", 7 not in set_b)

# -------------------------------
# Looping Through a Set
# -------------------------------
print("\n--- Looping ---")
for item in set_a:
    print(item, end=" ")

# -------------------------------
# Frozen Set (Immutable Set)
# -------------------------------
print("\n\n--- Frozen Set ---")
frozen = frozenset([1, 2, 3, 4])
print("Frozen Set:", frozen)
# frozen.add(5)  #  This will cause an error because frozen sets are immutable
