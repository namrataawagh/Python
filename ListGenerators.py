# Generator: Lazy sequence
'''
A generator is like a list, but it doesn’t store everything in memory at once.
👉 Instead, it generates values one at a time, on demand (lazy evaluation).

Example with a list:
nums = [x**2 for x in range(5)]
print(nums)

> Python creates the entire list in memory immediately.
> If range(5) were range(1_000_000), that would be a huge list sitting in RAM.

Example with a generator:
nums = (x**2 for x in range(5))
print(nums)

Output: "<generator object <genexpr> at 0x7f...>"

⚡ Instead of creating a list, Python creates a generator object.
   This object can be iterated over to produce values one by one.

Why is it "lazy"?
- Lists → eager (everything at once)
- Generators → lazy (on demand, values computed only when requested)
'''

nums = (x**2 for x in range(10**6))
print(next(nums))  # 0
print(next(nums))  # 1
print(next(nums))  # 4

# Even though it’s range(1,000,000), Python only calculates the next value when asked.

# -------------------------------
# Ways to make generators
# -------------------------------

# 1. Generator expression
gen = (x**2 for x in range(5))
print(gen)

# 2. Generator function with 'yield'
#    'yield' makes the function pause and resume, producing one value at a time.
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)

# 👉 Think of 'yield' as:
#    "return this value, but I’ll wait here so you can come back and continue".

# -------------------------------
# Example: alternating case function
# -------------------------------
def myfunc(a):
    return ''.join(
        char.lower if i % 2 == 0 else char.upper
        for i, char in enumerate(a)
    )

