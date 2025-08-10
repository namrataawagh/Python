# -------------------------------
# Python Tuples & Operations
# -------------------------------

# Tuples are ordered, immutable collections
# Can store mixed data types and allow duplicates
# Once created, items cannot be changed or removed

# Creating tuples
my_tuple = (10, 20, 30, 40, 50,10)
mixed_tuple = (1, "Hello", 3.14, True)
single_element_tuple = (5,)  # NOTE: comma is required for single-element tuple

print("Tuple:", my_tuple)
print("Mixed Tuple:", mixed_tuple)
print("Single Element Tuple:", single_element_tuple)
print("Type:", type(my_tuple))

# -------------------------------
# Accessing Tuple Elements
# -------------------------------
print("\n--- Accessing Elements ---")
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])



# -------------------------------
# Slicing Tuples
# -------------------------------
print("\n--- Slicing ---")
print("Elements from index 1 to 3:", my_tuple[1:4])
print("From start to index 2:", my_tuple[:3])
print("From index 2 to end:", my_tuple[2:])
print("Every 2nd element:", my_tuple[::2])

# -------------------------------
# Tuple Methods - Tuples have very few methods associated with them,namely:
# -------------------------------
numbers = (5, 2, 9, 5, 6)
print("\n--- Tuple Methods ---")
print("Count of 5:", numbers.count(5))
print("Index of 9:", numbers.index(9))

# -------------------------------
# Looping Through Tuples
# -------------------------------
print("\n--- Looping ---")
for item in my_tuple:
    print(item, end=" ")

# -------------------------------
# Tuple Packing & Unpacking
# -------------------------------
print("\n\n--- Packing & Unpacking ---")
packed_tuple = ("Alice", 25, "New York")
name, age, city = packed_tuple  # Unpacking tuple
print("Name:", name)
print("Age:", age)
print("City:", city)

# -------------------------------
# Nested Tuples
# -------------------------------
print("\n--- Nested Tuples ---")
nested_tuple = ((1, 2, 3), (4, 5, 6))
print("Nested Tuple:", nested_tuple)
print("First element of first tuple:", nested_tuple[0][0])

# -------------------------------
# Tuple Immutability
# -------------------------------
# Tuples cannot be modified directly, but you can create a new tuple
print("\n--- Immutability ---")
new_tuple = my_tuple + (60, 70)  # Concatenation
print("After adding elements:", new_tuple)

# Tuples can contain mutable elements like lists, which can be modified
tuple_with_list = (1, [2, 3, 4], 5)
tuple_with_list[1].append(6)  # Modifying the list inside tuple
print("Tuple with modified list:", tuple_with_list)
