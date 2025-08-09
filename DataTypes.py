# -------------------------------
# Python Basic Data Types Example
# -------------------------------

# 1. Integers (Whole numbers, no decimal point)
my_int = 10
print("Integer:", my_int, "| Type:", type(my_int))

# 2. Float (Decimal numbers)
my_float = 3.14
print("Float:", my_float, "| Type:", type(my_float))

# 3. String (Sequence of characters)
my_str = "Hello, Python!"
print("String:", my_str, "| Type:", type(my_str))

# 4. Boolean (True or False values)
my_bool = True
print("Boolean:", my_bool, "| Type:", type(my_bool))

# Data structures

# 5. List (Ordered, changeable collection, allows duplicates)
my_list = [1, 2, 3, 4, 5]
print("List:", my_list, "| Type:", type(my_list))

# 6. Tuple (Ordered, unchangeable collection, allows duplicates)
my_tuple = (10, 20, 30)
print("Tuple:", my_tuple, "| Type:", type(my_tuple))

# 7. Set (Unordered, no duplicates)
my_set = {1, 2, 3, 4, 4}  # Duplicate 4 will be removed
print("Set:", my_set, "| Type:", type(my_set))

# 8. Dictionary (Key-value pairs, unordered)
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print("Dictionary:", my_dict, "| Type:", type(my_dict))

# 9. NoneType (Represents absence of a value)
my_none = None
print("NoneType:", my_none, "| Type:", type(my_none))

# -------------------------------
# Type Casting (Changing data type)
# -------------------------------
num_str = "123"            # String
num_int = int(num_str)     # Convert string to integer
num_float = float(num_str) # Convert string to float
print("String to Int:", num_int, "| String to Float:", num_float)
