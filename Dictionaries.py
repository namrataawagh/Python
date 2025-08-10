# -------------------------------
# Python Dictionaries & Operations
# -------------------------------

# Dictionaries store data in key-value pairs
# Keys are unique and immutable (string, number, tuple)
# Values can be of any data type

# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print("Dictionary:", my_dict)
print("Type:", type(my_dict))

# -------------------------------
# Accessing Dictionary Values
# -------------------------------
print("\n--- Accessing Values ---")
print("Name:", my_dict["name"])           # Access using key
print("Age (get method):", my_dict.get("age"))  # get() returns None if key not found

# -------------------------------
# Adding & Updating Values
# -------------------------------
print("\n--- Adding & Updating ---")
my_dict["email"] = "alice@example.com"   # Add new key-value pair
my_dict["age"] = 26                      # Update existing value
print("After adding/updating:", my_dict)

# -------------------------------
# Removing Items
# -------------------------------
print("\n--- Removing Items ---")
my_dict.pop("city")           # Remove key and return value
print("After pop:", my_dict)
del my_dict["email"]          # Delete key-value pair
print("After del:", my_dict)
my_dict.clear()               # Remove all items
print("After clear:", my_dict)

# Restore dictionary for further examples
my_dict = {
    "name": "Alice",
    "age": 26,
    "skills": ["Python", "Data Analysis", "Machine Learning"]
}

# -------------------------------
# Dictionary Methods
# -------------------------------
print("\n--- Dictionary Methods ---")
print("Keys:", my_dict.keys())       # Returns all keys
print("Values:", my_dict.values())   # Returns all values
print("Items:", my_dict.items())     # Returns (key, value) pairs

# -------------------------------
# Looping Through Dictionary
# -------------------------------
print("\n--- Looping ---")
for key in my_dict:
    print("Key:", key, "| Value:", my_dict[key])

for key, value in my_dict.items():
    print(f"{key} → {value}")

# -------------------------------
# Nested Dictionaries
# -------------------------------
print("\n--- Nested Dictionaries ---")
students = {
    "student1": {"name": "John", "age": 20},
    "student2": {"name": "Emma", "age": 22}
}
print(students)
print("Student1 Name:", students["student1"]["name"])

