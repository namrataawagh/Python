# -----------------------------------------
# Beginner way vs List Comprehension way
# -----------------------------------------

# Example 1: Squaring numbers in a list
nums = [1, 2, 3, 4, 5]

# Beginner way
squares = []
for n in nums:
    squares.append(n**2)
print(squares)

# List comprehension way
squares = [n**2 for n in nums]
print(squares)


# Example 2: Filtering even numbers
# Beginner way
evens = []
for n in nums:
    if n % 2 == 0:
        evens.append(n)
print(evens)

# List comprehension way
evens = [n for n in nums if n % 2 == 0]
print(evens)


# Example 3: Creating tuples (number, square)
# Beginner way
num_pairs = []
for n in nums:
    num_pairs.append((n, n**2))
print(num_pairs)

# List comprehension way
num_pairs = [(n, n**2) for n in nums]
print(num_pairs)


# Example 4: Nested loops in list comprehension
# Beginner way
pairs = []
for letter in 'abc':
    for num in range(3):
        pairs.append((letter, num))
print(pairs)

# List comprehension way
pairs = [(letter, num) for letter in 'abc' for num in range(3)]
print(pairs)


# Example 5: Flattening a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Beginner way
flat = []
for row in matrix:
    for val in row:
        flat.append(val)
print(flat)

# List comprehension way
flat = [val for row in matrix for val in row]
print(flat)


