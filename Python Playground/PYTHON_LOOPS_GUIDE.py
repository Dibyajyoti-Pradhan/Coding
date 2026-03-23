"""
PYTHON LOOPS - Complete Guide (with C++ Comparisons)
=====================================================

Python loops are simpler and more Pythonic than C++.
Key differences:
- No semicolons
- No parentheses around conditions (unless needed for clarity)
- No do-while (use while True with break)
- Indentation matters!
"""

# ============================================================================
# 1. FOR LOOPS
# ============================================================================

print("="*60)
print("FOR LOOPS")
print("="*60)

# -----------------------------------------------------------------------------
# Basic for loop - iterating over range
# -----------------------------------------------------------------------------

# C++ equivalent:
# for (int i = 0; i < 5; i++) {
#     cout << i << endl;
# }

print("\n1. Basic for loop (0 to 4):")
for i in range(5):
    print(i, end=' ')
print()

# -----------------------------------------------------------------------------
# For loop with start and end
# -----------------------------------------------------------------------------

# C++ equivalent:
# for (int i = 2; i < 10; i++) {
#     cout << i << endl;
# }

print("\n2. For loop with start and end (2 to 9):")
for i in range(2, 10):
    print(i, end=' ')
print()

# -----------------------------------------------------------------------------
# For loop with step
# -----------------------------------------------------------------------------

# C++ equivalent:
# for (int i = 0; i < 20; i += 2) {
#     cout << i << endl;
# }

print("\n3. For loop with step (even numbers 0 to 18):")
for i in range(0, 20, 2):
    print(i, end=' ')
print()

# -----------------------------------------------------------------------------
# For loop counting backwards
# -----------------------------------------------------------------------------

# C++ equivalent:
# for (int i = 10; i >= 0; i--) {
#     cout << i << endl;
# }

print("\n4. For loop counting backwards (10 to 0):")
for i in range(10, -1, -1):
    print(i, end=' ')
print()

# -----------------------------------------------------------------------------
# For loop with custom increment (like i = i * 2)
# -----------------------------------------------------------------------------

# C++ equivalent:
# for (int i = 1; i <= 100; i *= 2) {
#     cout << i << endl;
# }

print("\n5. Custom increment (i *= 2) - PYTHON WAY:")
i = 1
for _ in range(7):  # Need to know max iterations
    print(i, end=' ')
    i *= 2
print()

# Alternative: Use while loop for this (better approach)
print("\n5b. Custom increment (i *= 2) - WHILE LOOP (better):")
i = 1
while i <= 100:
    print(i, end=' ')
    i *= 2
print()

# -----------------------------------------------------------------------------
# For loop - iterating over list
# -----------------------------------------------------------------------------

print("\n6. Iterating over list:")
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit, end=' ')
print()

# -----------------------------------------------------------------------------
# For loop with index (enumerate)
# -----------------------------------------------------------------------------

# C++ equivalent:
# for (int i = 0; i < fruits.size(); i++) {
#     cout << i << ": " << fruits[i] << endl;
# }

print("\n7. For loop with index (enumerate):")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Start index from 1
print("\n7b. Enumerate starting from 1:")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

# -----------------------------------------------------------------------------
# For loop - iterating over dictionary
# -----------------------------------------------------------------------------

print("\n8. Iterating over dictionary:")
person = {'name': 'Alice', 'age': 25, 'city': 'NYC'}

# Keys only
for key in person:
    print(key, end=' ')
print()

# Keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# Values only
for value in person.values():
    print(value, end=' ')
print()

# -----------------------------------------------------------------------------
# For loop - list comprehension (advanced)
# -----------------------------------------------------------------------------

print("\n9. List comprehension (Pythonic way):")
squares = [x**2 for x in range(10)]
print(squares)

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)


# ============================================================================
# 2. WHILE LOOPS
# ============================================================================

print("\n" + "="*60)
print("WHILE LOOPS")
print("="*60)

# -----------------------------------------------------------------------------
# Basic while loop
# -----------------------------------------------------------------------------

# C++ equivalent:
# int i = 0;
# while (i < 5) {
#     cout << i << endl;
#     i++;
# }

print("\n1. Basic while loop (0 to 4):")
i = 0
while i < 5:
    print(i, end=' ')
    i += 1
print()

# -----------------------------------------------------------------------------
# While loop with custom increment
# -----------------------------------------------------------------------------

# C++ equivalent:
# int i = 1;
# while (i <= 100) {
#     cout << i << endl;
#     i *= 2;
# }

print("\n2. While loop with i *= 2:")
i = 1
while i <= 100:
    print(i, end=' ')
    i *= 2
print()

print("\n3. While loop with i *= i (i squared):")
i = 2
while i < 1000:
    print(i, end=' ')
    i = i * i  # or i *= i
print()

# -----------------------------------------------------------------------------
# While loop with break
# -----------------------------------------------------------------------------

print("\n4. While loop with break:")
i = 0
while True:
    print(i, end=' ')
    i += 1
    if i >= 5:
        break
print()

# -----------------------------------------------------------------------------
# While loop with continue
# -----------------------------------------------------------------------------

print("\n5. While loop with continue (skip odd numbers):")
i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i, end=' ')
print()


# ============================================================================
# 3. DO-WHILE LOOPS (Python doesn't have it!)
# ============================================================================

print("\n" + "="*60)
print("DO-WHILE LOOPS (Python alternatives)")
print("="*60)

# C++ do-while:
# int i = 0;
# do {
#     cout << i << endl;
#     i++;
# } while (i < 5);

# Python equivalent - Method 1: while True with break
print("\n1. Method 1 - while True with break:")
i = 0
while True:
    print(i, end=' ')
    i += 1
    if i >= 5:
        break
print()

# Python equivalent - Method 2: Repeat first iteration
print("\n2. Method 2 - Execute once, then while:")
i = 0
print(i, end=' ')
i += 1
while i < 5:
    print(i, end=' ')
    i += 1
print()

# Python equivalent - Method 3: Use flag variable
print("\n3. Method 3 - Use flag variable:")
i = 0
first_time = True
while first_time or i < 5:
    print(i, end=' ')
    i += 1
    first_time = False
print()


# ============================================================================
# 4. NESTED LOOPS
# ============================================================================

print("\n" + "="*60)
print("NESTED LOOPS")
print("="*60)

# C++ equivalent:
# for (int i = 0; i < 3; i++) {
#     for (int j = 0; j < 3; j++) {
#         cout << i << "," << j << " ";
#     }
#     cout << endl;
# }

print("\n1. Nested for loops:")
for i in range(3):
    for j in range(3):
        print(f"({i},{j})", end=' ')
    print()

print("\n2. Multiplication table:")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end=' ')
    print()


# ============================================================================
# 5. COMMON INCREMENT/DECREMENT PATTERNS
# ============================================================================

print("\n" + "="*60)
print("INCREMENT/DECREMENT PATTERNS")
print("="*60)

print("\n1. i += 1 (increment by 1):")
i = 0
for _ in range(5):
    print(i, end=' ')
    i += 1
print()

print("\n2. i += 2 (increment by 2):")
i = 0
for _ in range(5):
    print(i, end=' ')
    i += 2
print()

print("\n3. i -= 1 (decrement by 1):")
i = 10
for _ in range(5):
    print(i, end=' ')
    i -= 1
print()

print("\n4. i *= 2 (double each time):")
i = 1
for _ in range(7):
    print(i, end=' ')
    i *= 2
print()

print("\n5. i *= i (square each time):")
i = 2
for _ in range(4):
    print(i, end=' ')
    i *= i
print()

print("\n6. i //= 2 (integer division by 2):")
i = 100
while i > 0:
    print(i, end=' ')
    i //= 2
print()

print("\n7. i = i * 3 + 1 (custom formula):")
i = 1
for _ in range(5):
    print(i, end=' ')
    i = i * 3 + 1
print()


# ============================================================================
# 6. LOOP CONTROL STATEMENTS
# ============================================================================

print("\n" + "="*60)
print("LOOP CONTROL STATEMENTS")
print("="*60)

# -----------------------------------------------------------------------------
# break - exit loop immediately
# -----------------------------------------------------------------------------

print("\n1. break - exit when i == 5:")
for i in range(10):
    if i == 5:
        break
    print(i, end=' ')
print()

# -----------------------------------------------------------------------------
# continue - skip current iteration
# -----------------------------------------------------------------------------

print("\n2. continue - skip odd numbers:")
for i in range(10):
    if i % 2 != 0:
        continue
    print(i, end=' ')
print()

# -----------------------------------------------------------------------------
# else clause (Python special!)
# -----------------------------------------------------------------------------

print("\n3. else clause - executes if loop completes without break:")
for i in range(5):
    print(i, end=' ')
else:
    print("\nLoop completed normally!")

print("\n4. else clause - NOT executed when break is used:")
for i in range(10):
    if i == 5:
        break
    print(i, end=' ')
else:
    print("\nLoop completed normally!")
print("\n(else didn't execute because of break)")

# -----------------------------------------------------------------------------
# pass - do nothing (placeholder)
# -----------------------------------------------------------------------------

print("\n5. pass - placeholder for empty loop:")
for i in range(5):
    pass  # TODO: implement later
print("Loop executed (but did nothing)")


# ============================================================================
# 7. COMMON INTERVIEW PATTERNS
# ============================================================================

print("\n" + "="*60)
print("COMMON INTERVIEW PATTERNS")
print("="*60)

# Pattern 1: Binary search increment (i *= 2)
print("\n1. Binary search style increment:")
i = 1
n = 100
while i < n:
    print(i, end=' ')
    i *= 2
print(f"\nTotal iterations: {i.bit_length()}")  # log₂(n) iterations

# Pattern 2: Square root check (i * i <= n)
print("\n2. Check divisors up to sqrt(n):")
n = 36
i = 1
while i * i <= n:
    if n % i == 0:
        print(f"{i} and {n//i} are divisors")
    i += 1

# Pattern 3: Digit manipulation
print("\n3. Extract digits of number:")
num = 12345
while num > 0:
    digit = num % 10
    print(digit, end=' ')
    num //= 10
print()

# Pattern 4: Power of 2 check
print("\n4. Generate powers of 2:")
power = 1
for i in range(10):
    print(f"2^{i} = {power}")
    power *= 2

# Pattern 5: Fibonacci
print("\n5. Fibonacci sequence:")
a, b = 0, 1
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b
print()


# ============================================================================
# 8. PYTHON vs C++ COMPARISON
# ============================================================================

print("\n" + "="*60)
print("PYTHON vs C++ - Quick Reference")
print("="*60)

comparison = """
┌─────────────────────────────────┬─────────────────────────────────┐
│            C++                  │           Python                │
├─────────────────────────────────┼─────────────────────────────────┤
│ for (int i = 0; i < 10; i++)   │ for i in range(10):             │
│ for (int i = 0; i < 10; i+=2)  │ for i in range(0, 10, 2):       │
│ for (int i = 10; i >= 0; i--)  │ for i in range(10, -1, -1):     │
│ while (i < 10)                  │ while i < 10:                   │
│ do { ... } while (i < 10);      │ # Use: while True + break       │
│ i++                             │ i += 1                          │
│ i--                             │ i -= 1                          │
│ i *= 2                          │ i *= 2                          │
│ i = i * i                       │ i *= i  or  i = i * i           │
│ break;                          │ break                           │
│ continue;                       │ continue                        │
└─────────────────────────────────┴─────────────────────────────────┘
"""
print(comparison)


# ============================================================================
# 9. COMMON MISTAKES TO AVOID
# ============================================================================

print("\n" + "="*60)
print("COMMON MISTAKES")
print("="*60)

print("""
❌ MISTAKE 1: Using i++ or ++i (doesn't exist in Python!)
   C++:    i++
   Python: i += 1

❌ MISTAKE 2: Forgetting to update loop variable
   while i < 10:
       print(i)
       # ← forgot i += 1, infinite loop!

❌ MISTAKE 3: Modifying loop variable in for-range loop
   for i in range(10):
       i += 1  # This doesn't affect the loop!

✅ CORRECT: Use while loop for custom increments
   i = 0
   while i < 10:
       print(i)
       i = i * 2  # Custom increment

❌ MISTAKE 4: Off-by-one errors
   range(5)     → [0, 1, 2, 3, 4]  (5 not included!)
   range(1, 6)  → [1, 2, 3, 4, 5]

❌ MISTAKE 5: Infinite loop with no exit
   while True:
       print("Forever!")
       # ← forgot break statement!
""")


# ============================================================================
# 10. PRACTICE PROBLEMS
# ============================================================================

print("\n" + "="*60)
print("PRACTICE PROBLEMS")
print("="*60)

print("\n1. Sum of numbers 1 to 100:")
total = 0
for i in range(1, 101):
    total += i
print(f"Sum = {total}")

print("\n2. Factorial of 5:")
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")

print("\n3. Count down from 10:")
i = 10
while i >= 0:
    print(i, end=' ')
    i -= 1
print("\nBlastoff!")

print("\n4. Print squares from 1 to 10:")
for i in range(1, 11):
    print(f"{i}² = {i*i}")

print("\n5. Print powers of 2 up to 1024:")
i = 1
while i <= 1024:
    print(i, end=' ')
    i *= 2
print()


# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "="*60)
print("QUICK SUMMARY")
print("="*60)

summary = """
FOR LOOPS (when you know iteration count):
   for i in range(n):              # 0 to n-1
   for i in range(a, b):           # a to b-1
   for i in range(a, b, step):     # a to b-1 with step

WHILE LOOPS (when condition-based or custom increment):
   while condition:
       # code
       i += 1

   while i < n:
       i *= 2                      # Use for i*=2, i*=i, etc.

DO-WHILE (Python equivalent):
   while True:
       # code
       if condition:
           break

INCREMENTING:
   i += 1     # Add 1
   i += 2     # Add 2
   i *= 2     # Double
   i *= i     # Square
   i //= 2    # Halve (integer division)
   i -= 1     # Subtract 1

LOOP CONTROL:
   break      # Exit loop
   continue   # Skip to next iteration
   pass       # Do nothing (placeholder)
"""

print(summary)

print("\n🎯 For interview problems like binary search, use i *= 2")
print("🎯 For sqrt checking, use i * i <= n")
print("🎯 For digit manipulation, use num //= 10")
print("🎯 For custom increments, prefer WHILE over FOR")
