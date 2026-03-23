"""
LOOP INCREMENT PATTERNS - Quick Reference
==========================================

Common increment patterns used in coding interviews and algorithms.
Focus: i = i*i, i = i*2, and other custom increments
"""

print("="*70)
print("CUSTOM INCREMENT PATTERNS IN PYTHON")
print("="*70)

# ============================================================================
# PATTERN 1: i = i * 2 (Doubling)
# ============================================================================

print("\n" + "─"*70)
print("PATTERN 1: i *= 2 (Doubling - Binary Search, Powers of 2)")
print("─"*70)

print("\n📌 C++ Code:")
print("""
for (int i = 1; i <= 100; i *= 2) {
    cout << i << endl;
}
""")

print("📌 Python Code:")
print("""
i = 1
while i <= 100:
    print(i)
    i *= 2
""")

print("📌 Output:")
i = 1
while i <= 100:
    print(i, end=' ')
    i *= 2
print(f"\n\n✅ Total iterations: {i.bit_length()} (log₂ of upper bound)")

# Real-world use case
print("\n🔍 Use Case: Binary search iteration")
n = 1000000
i = 1
count = 0
while i < n:
    i *= 2
    count += 1
print(f"To reach {n}, needed {count} doublings (approximately log₂({n}))")


# ============================================================================
# PATTERN 2: i = i * i (Squaring)
# ============================================================================

print("\n" + "─"*70)
print("PATTERN 2: i *= i (Squaring - Exponential Growth)")
print("─"*70)

print("\n📌 C++ Code:")
print("""
for (int i = 2; i < 1000; i *= i) {
    cout << i << endl;
}
""")

print("📌 Python Code:")
print("""
i = 2
while i < 1000:
    print(i)
    i *= i
""")

print("📌 Output:")
i = 2
while i < 1000:
    print(i, end=' ')
    i *= i
print(f"\n\n✅ Grows VERY fast: 2 → 4 → 16 → 256 → 65536...")

# Real-world use case
print("\n🔍 Use Case: Checking if number is power of 2")
def is_power_of_square(n):
    """Check if n can be reached by squaring."""
    i = 2
    while i <= n:
        if i == n:
            return True
        if i > n:
            return False
        i *= i
    return False

print(f"Is 16 a perfect square power? {is_power_of_square(16)}")
print(f"Is 256 a perfect square power? {is_power_of_square(256)}")


# ============================================================================
# PATTERN 3: i = i // 2 (Halving)
# ============================================================================

print("\n" + "─"*70)
print("PATTERN 3: i //= 2 (Halving - Binary Search, Divide & Conquer)")
print("─"*70)

print("\n📌 C++ Code:")
print("""
for (int i = 100; i > 0; i /= 2) {
    cout << i << endl;
}
""")

print("📌 Python Code (use // for integer division):")
print("""
i = 100
while i > 0:
    print(i)
    i //= 2
""")

print("📌 Output:")
i = 100
while i > 0:
    print(i, end=' ')
    i //= 2
print()

# Real-world use case
print("\n🔍 Use Case: Binary search, finding log₂(n)")
def log2_floor(n):
    """Find floor of log₂(n)."""
    count = 0
    while n > 1:
        n //= 2
        count += 1
    return count

print(f"log₂(100) ≈ {log2_floor(100)}")
print(f"log₂(1024) ≈ {log2_floor(1024)}")


# ============================================================================
# PATTERN 4: i = i * i <= n (Check up to sqrt)
# ============================================================================

print("\n" + "─"*70)
print("PATTERN 4: i * i <= n (Check divisors up to sqrt)")
print("─"*70)

print("\n📌 C++ Code:")
print("""
for (int i = 1; i * i <= n; i++) {
    if (n % i == 0) {
        cout << i << ", " << n/i << endl;
    }
}
""")

print("📌 Python Code:")
print("""
i = 1
while i * i <= n:
    if n % i == 0:
        print(f'{i} and {n//i}')
    i += 1
""")

print("📌 Example: Find divisors of 36:")
n = 36
i = 1
divisors = []
while i * i <= n:
    if n % i == 0:
        divisors.append((i, n // i))
    i += 1

for d1, d2 in divisors:
    print(f"  {d1} × {d2} = {n}")

print(f"\n✅ Only checked up to {int(n**0.5)} instead of {n} (more efficient!)")

# Real-world use case
print("\n🔍 Use Case: Prime number checking")
def is_prime(n):
    """Check if n is prime (optimized)."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2  # Check only odd numbers
    return True

print(f"Is 17 prime? {is_prime(17)}")
print(f"Is 100 prime? {is_prime(100)}")


# ============================================================================
# PATTERN 5: Fibonacci-style (a, b = b, a+b)
# ============================================================================

print("\n" + "─"*70)
print("PATTERN 5: Fibonacci Pattern (Multiple variable update)")
print("─"*70)

print("\n📌 C++ Code:")
print("""
int a = 0, b = 1;
for (int i = 0; i < 10; i++) {
    cout << a << endl;
    int temp = a + b;
    a = b;
    b = temp;
}
""")

print("📌 Python Code (Pythonic way!):")
print("""
a, b = 0, 1
for _ in range(10):
    print(a)
    a, b = b, a + b
""")

print("📌 Output:")
a, b = 0, 1
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b
print()


# ============================================================================
# PATTERN 6: Digit Extraction (n //= 10)
# ============================================================================

print("\n" + "─"*70)
print("PATTERN 6: n //= 10 (Digit Extraction)")
print("─"*70)

print("\n📌 C++ Code:")
print("""
int n = 12345;
while (n > 0) {
    cout << n % 10 << endl;
    n /= 10;
}
""")

print("📌 Python Code:")
print("""
n = 12345
while n > 0:
    print(n % 10)
    n //= 10
""")

print("📌 Output (digits in reverse):")
n = 12345
while n > 0:
    print(n % 10, end=' ')
    n //= 10
print()

# Real-world use case
print("\n🔍 Use Case: Count digits")
def count_digits(n):
    if n == 0:
        return 1
    count = 0
    n = abs(n)
    while n > 0:
        count += 1
        n //= 10
    return count

print(f"12345 has {count_digits(12345)} digits")
print(f"1000000 has {count_digits(1000000)} digits")


# ============================================================================
# PATTERN 7: Custom Formula (i = i * 3 + 1, etc.)
# ============================================================================

print("\n" + "─"*70)
print("PATTERN 7: Custom Formulas (Collatz, etc.)")
print("─"*70)

print("\n📌 Example: Collatz Conjecture (3n+1 problem)")
print("Rule: If even → n/2, if odd → 3n+1")

def collatz_sequence(n):
    """Generate Collatz sequence."""
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    return sequence

seq = collatz_sequence(13)
print(f"Collatz(13): {seq}")
print(f"Length: {len(seq)} steps")


# ============================================================================
# COMPARISON TABLE
# ============================================================================

print("\n" + "="*70)
print("QUICK REFERENCE TABLE")
print("="*70)

table = """
┌────────────────────┬───────────────────┬──────────────────────────────┐
│   Pattern          │   Growth Rate     │   Common Use Case            │
├────────────────────┼───────────────────┼──────────────────────────────┤
│ i += 1             │ Linear            │ Standard iteration           │
│ i += 2             │ Linear            │ Even/odd numbers             │
│ i *= 2             │ Logarithmic       │ Binary search, powers of 2   │
│ i *= i             │ Double exponential│ Very fast growth             │
│ i //= 2            │ Logarithmic       │ Binary search (backwards)    │
│ i * i <= n         │ Square root       │ Prime check, divisors        │
│ a, b = b, a+b      │ Exponential       │ Fibonacci sequence           │
│ n //= 10           │ Logarithmic       │ Digit extraction             │
│ i = i * 3 + 1      │ Custom            │ Collatz conjecture           │
└────────────────────┴───────────────────┴──────────────────────────────┘
"""
print(table)


# ============================================================================
# INTERVIEW PROBLEMS USING THESE PATTERNS
# ============================================================================

print("\n" + "="*70)
print("INTERVIEW PROBLEMS")
print("="*70)

print("\n1. PROBLEM: Find if n is a power of 2")
print("   Pattern: i *= 2")
def is_power_of_two(n):
    if n <= 0:
        return False
    i = 1
    while i < n:
        i *= 2
    return i == n

print(f"   is_power_of_two(16) = {is_power_of_two(16)}")
print(f"   is_power_of_two(18) = {is_power_of_two(18)}")

print("\n2. PROBLEM: Count set bits (1s) in binary")
print("   Pattern: n //= 2")
def count_set_bits(n):
    count = 0
    while n > 0:
        count += n & 1  # Check last bit
        n //= 2
    return count

print(f"   count_set_bits(13) = {count_set_bits(13)} (binary: 1101)")
print(f"   count_set_bits(7) = {count_set_bits(7)} (binary: 111)")

print("\n3. PROBLEM: Reverse a number")
print("   Pattern: n //= 10")
def reverse_number(n):
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + (n % 10)
        n //= 10
    return reversed_num

print(f"   reverse_number(12345) = {reverse_number(12345)}")

print("\n4. PROBLEM: Check if palindrome number")
print("   Pattern: n //= 10")
def is_palindrome_number(n):
    return n == reverse_number(n)

print(f"   is_palindrome_number(12321) = {is_palindrome_number(12321)}")
print(f"   is_palindrome_number(12345) = {is_palindrome_number(12345)}")


# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n" + "="*70)
print("PRACTICE EXERCISES")
print("="*70)

exercises = """
Try implementing these using appropriate increment patterns:

1. Print all powers of 3 less than 1000
   Pattern: i *= 3

2. Find the largest power of 2 less than n
   Pattern: i *= 2

3. Count number of trailing zeros in n!
   Pattern: n //= 5

4. Sum of digits of a number
   Pattern: n //= 10

5. Find nth Fibonacci number
   Pattern: a, b = b, a+b

6. Check if number is perfect square
   Pattern: i * i <= n

7. Binary representation of number
   Pattern: n //= 2

8. GCD using Euclidean algorithm
   Pattern: a, b = b, a % b
"""
print(exercises)

print("\n" + "="*70)
print("🎯 KEY TAKEAWAYS")
print("="*70)
print("""
✅ Use WHILE loops for custom increments (i *= 2, i *= i, etc.)
✅ Use FOR loops when iteration count is known (range-based)
✅ i *= 2 is O(log n) - very efficient!
✅ i * i <= n is how to check up to sqrt(n)
✅ n //= 10 is how to process digits
✅ Python has no i++ or i--, use i += 1 or i -= 1
✅ Python has no do-while, use: while True + break
""")
