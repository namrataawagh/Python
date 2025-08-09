# -------------------------------
# Python Strings & String Operations
# -------------------------------

# Strings are sequences of characters enclosed in single (' '), double (" "), or triple quotes (''' ''' or """ """)
str1 = 'Hello'
str2 = "Python"
str3 = """This is
a multi-line
string."""

print("String 1:", str1)
print("String 2:", str2)
print("Multi-line String:\n", str3)

# -------------------------------
# String Indexing & Slicing
# -------------------------------
text = "Python"

print("\n--- Indexing ---")
print("First character:", text[0])     # Index 0 → 'P'
print("Last character:", text[-1])     # Index -1 → 'n'

print("\n--- Slicing ---")
print("Characters 0 to 3:", text[0:4]) # 'Pyth' (end index is excluded)
print("From index 2 onwards:", text[2:]) # 'thon'
print("From start to index 3:", text[:4]) # 'Pyth'
print("Every second character:", text[::2]) # 'Pto' [start:stop:step] method

# -------------------------------
# String Operations
# -------------------------------
str_a = "Hello"
str_b = "World"

print("\n--- String Operations ---")
print("Concatenation:", str_a + " " + str_b) # Joining strings
print("Repetition:", str_a * 3)             # Repeat string

# -------------------------------
# Common String Methods
# -------------------------------
msg = "  python programming  "

print("\n--- String Methods ---")
print("Uppercase:", msg.upper())
print("Lowercase:", msg.lower())
print("Title Case:", msg.title())  # first letter of the word to uppercase
print("Strip (remove spaces):", msg.strip())
print("Replace:", msg.replace("python", "java"))
print("Split into list:", msg.split())  # By default splits on spaces
print("Join list into string:", "-".join(["I", "love", "Python"]))

# -------------------------------
# Searching in Strings
# -------------------------------
print("\n--- Searching ---")
print("Find 'pro':", msg.find("pro"))    # Returns index of first match
print("Count 'm':", msg.count("m"))      # Counts occurrences
print("Starts with 'py':", msg.startswith("py"))
print("Ends with 'ing':", msg.endswith("ing"))

# -------------------------------
# f-Strings (String Formatting)
# -------------------------------
name = "Alice"
age = 25
print(f"\nMy name is {name} and I am {age} years old.")

# -------------------------------
# Escape Characters : "\"
# -------------------------------
print("\n--- Escape Characters ---")
print("Line break:\nHello")         # \n → new line
print("Tab space:\tPython")         # \t → tab space
print("Quote inside string: \"Hi\"") # \" → double quote inside

# Length of the string
fruit = "My favourite fruit is Mango"
print("The length of this string is:",len(fruit))