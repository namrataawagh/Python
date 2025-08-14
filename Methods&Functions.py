# ---------------------------
# FUNCTIONS IN PYTHON
# ---------------------------
# Functions allow you to create reusable blocks of code 
# that can be executed multiple times without rewriting the whole thing.
# Syntax: Use the 'def' keyword followed by the function name (in snake_case) and parameters.
# Naming convention: Use descriptive names in snake_case for readability.

def name_of_function(name):
    '''
    This is a docstring (multi-line string placed just after a function definition).
    It describes what the function does, its parameters, and (optionally) its return value.
    Docstrings are optional but highly recommended for code clarity.
    
    Parameters:
        name (str): A name to include in the greeting.
        
    Returns:
        str: A greeting message including the given name.
    '''
    return "Hello" + name  # Concatenates "Hello" with the provided name


# The 'return' keyword sends back the result of the function instead of printing it directly.
# This allows you to store the result in a variable or use it later in the program.
c = name_of_function('Namrata')
print(c)  # Outputs: HelloNamrata


# ---------------------------
# FUNCTION WITH DEFAULT ARGUMENT
# ---------------------------
def ur_name(name='Guest'):
    '''
    Prints a greeting message. If no name is provided, defaults to 'Guest'.
    '''
    print(f'hello ' + name)

ur_name()  # Will print 'hello Guest' since no argument is passed.

print(c)  # Still accessible because 'c' stores the earlier returned value.


# ---------------------------
# CHECK IF A NUMBER IS EVEN
# ---------------------------
def even_check(num):
    '''
    Checks if a number is even.

    Parameters:
        num (int): Number to check.

    Returns:
        str: Message stating the number is even (if it is).
    '''
    if num % 2 == 0:
        return f'{num} is even'

result = even_check(2)
print(result)  # Outputs: 2 is even


# ---------------------------
# CHECK ALL EVEN NUMBERS IN A LIST
# ---------------------------
def even_check1(num_list):
    '''
    Checks which numbers in a list are even and prints them.

    Parameters:
        num_list (list): List of integers to check.

    Returns:
        list: A list containing the results of the print() calls (will be None values).
    '''
    list1 = []  # Unused here but kept as in original logic.
    return [list(print(f'{i} is even') for i in num_list if i % 2 == 0)]

even_check1([1, 2, 3, 4])  # Prints "2 is even" and "4 is even"
