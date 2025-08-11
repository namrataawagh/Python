# -------------------------------
# Python Basic File I/O (.txt files)
# -------------------------------

# Modes for opening files:
# 'r'  → Read (default, file must exist)
# 'w'  → Write (creates new or overwrites existing file)
# 'a'  → Append (adds to the end of file)
# 'r+' → Read and write

# -------------------------------
# Writing to a file
# -------------------------------
print("---Writing to a File ---")
with open("example.txt","w") as file:
    file.write("Hello,Wolrld!\n")
    file.write("This is a sample text file.\n")
    file.write("Python makes file handling easy!\n")
print("Data written to 'example.txt' successfully")


# -------------------------------
# Reading the entire file
# -------------------------------
print("\n--- Reading Entire File ---")
with open("example.txt","r") as file:
    content = file.read()  # Reads entire file as String
print(content)


# -------------------------------
# Reading line by line
# -------------------------------
print("\n--- Reading line by line ---")
with open("example.txt","r") as file:
    for line in file:
        print(line.strip()) # .strip() removes newline charachter

# -------------------------------
# Appending to a file
# -------------------------------
print("\n--- Appending to a File ---")
with open("example.txt", "a") as file:
    file.write("This line was appended.\n")
print("Data appended successfully.")

# -------------------------------
# Reading lines into a list
# -------------------------------
print("\n--- Reading into a List ---")
with open("example.txt", "r") as file:
    lines = file.readlines()  # Returns list of lines
print(lines)

# -------------------------------
# Writing a list to a file
# -------------------------------
print("\n--- Writing a List to a File ---")
data_list = ["First line\n", "Second line\n", "Third line\n"]
with open("example.txt", "w") as file:
    file.writelines(data_list)  # Writes list items to file
print("List written to file successfully.")

