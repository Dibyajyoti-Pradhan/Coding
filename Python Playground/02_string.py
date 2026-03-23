"""
STRINGS - Complete Guide for Interview Preparation
===================================================

CORE CONCEPTS:
--------------
1. Strings are IMMUTABLE in Python (cannot modify in place)
2. String operations create new strings (O(n) space)
3. UTF-8 encoded by default in Python 3
4. String concatenation in loop is O(n²) - use join() instead!
5. Strings are sequences - support indexing, slicing, iteration

TRICKY PARTS:
-------------
1. String immutability: s[0] = 'a' raises TypeError
2. String interning: 'a' is 'a' is True, but 'abc!' is 'abc!' may be False
3. r"raw\nstring" - backslash not escaped
4. f"f-string {var}" - formatted string literals (Python 3.6+)
5. Unicode handling: len('é') may be 1 or 2 depending on normalization
6. String multiplication: 'ab' * 3 = 'ababab'

COMMON PATTERNS:
----------------
1. Two Pointers (palindrome, reverse)
2. Sliding Window (substrings)
3. Character Frequency (hashmap/array)
4. String Builder (list for mutable operations)
5. KMP / Rabin-Karp (pattern matching)
6. Trie (prefix matching)
"""

from typing import List, Dict, Set
from collections import Counter, defaultdict
import re


# ============================================================================
# PATTERN 1: CHARACTER FREQUENCY / HASHMAP
# ============================================================================

def is_anagram(s: str, t: str) -> bool:
    """
    LeetCode 242 - Check if two strings are anagrams.

    Time: O(n), Space: O(1) - max 26 letters
    """
    if len(s) != len(t):
        return False

    # Approach 1: Using Counter
    return Counter(s) == Counter(t)

    # Approach 2: Using array (slightly faster)
    # count = [0] * 26
    # for char in s:
    #     count[ord(char) - ord('a')] += 1
    # for char in t:
    #     count[ord(char) - ord('a')] -= 1
    # return all(c == 0 for c in count)


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    LeetCode 49 - Group anagrams together.

    Time: O(n * k log k) where k is max string length, Space: O(n*k)
    Tricky: Use sorted string as key OR character count tuple
    """
    anagram_groups = defaultdict(list)

    for s in strs:
        # Approach 1: Sorted string as key
        key = ''.join(sorted(s))
        anagram_groups[key].append(s)

        # Approach 2: Character count as key (faster for long strings)
        # count = [0] * 26
        # for char in s:
        #     count[ord(char) - ord('a')] += 1
        # key = tuple(count)
        # anagram_groups[key].append(s)

    return list(anagram_groups.values())


def first_unique_char(s: str) -> int:
    """
    LeetCode 387 - Find first non-repeating character.

    Time: O(n), Space: O(1)
    """
    count = Counter(s)

    for i, char in enumerate(s):
        if count[char] == 1:
            return i

    return -1


# ============================================================================
# PATTERN 2: TWO POINTERS
# ============================================================================

def is_palindrome(s: str) -> bool:
    """
    LeetCode 125 - Valid palindrome (alphanumeric only, case-insensitive).

    Time: O(n), Space: O(1)
    """
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


def longest_palindrome_two_pointers(s: str) -> str:
    """
    LeetCode 5 - Longest palindromic substring (expand around center).

    Time: O(n²), Space: O(1)
    Tricky: Check both odd and even length palindromes
    """
    if not s:
        return ""

    def expand_around_center(left: int, right: int) -> int:
        """Returns length of palindrome expanded from center."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    start = end = 0

    for i in range(len(s)):
        # Odd length palindrome (center is single character)
        len1 = expand_around_center(i, i)
        # Even length palindrome (center is between two characters)
        len2 = expand_around_center(i, i + 1)

        max_len = max(len1, len2)

        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]


def reverse_words(s: str) -> str:
    """
    LeetCode 151 - Reverse words in a string.

    Time: O(n), Space: O(n)
    """
    # Python way: split and reverse
    return ' '.join(s.split()[::-1])

    # Manual approach (if string was mutable)
    # 1. Reverse entire string
    # 2. Reverse each word individually


# ============================================================================
# PATTERN 3: SLIDING WINDOW
# ============================================================================

def longest_substring_without_repeating(s: str) -> int:
    """
    LeetCode 3 - Longest substring without repeating characters.

    Time: O(n), Space: O(min(m,n)) where m is charset size
    Tricky: Use hashmap to store last seen index
    """
    char_index = {}
    max_length = 0
    start = 0

    for end, char in enumerate(s):
        # If character seen and within current window
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1

        char_index[char] = end
        max_length = max(max_length, end - start + 1)

    return max_length


def min_window_substring(s: str, t: str) -> str:
    """
    LeetCode 76 - Minimum window substring containing all characters of t.

    Time: O(|s| + |t|), Space: O(|s| + |t|)
    Tricky: Use two hashmaps, track formed characters
    """
    if not s or not t:
        return ""

    # Frequency of characters in t
    target_count = Counter(t)
    required = len(target_count)

    # Window counters
    window_count = {}
    formed = 0  # Number of unique chars in window with desired frequency

    left = 0
    min_len = float('inf')
    min_window = (0, 0)

    for right, char in enumerate(s):
        # Add character to window
        window_count[char] = window_count.get(char, 0) + 1

        # Check if frequency matches
        if char in target_count and window_count[char] == target_count[char]:
            formed += 1

        # Try to shrink window
        while left <= right and formed == required:
            # Update result if smaller window
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = (left, right)

            # Remove leftmost character
            char = s[left]
            window_count[char] -= 1
            if char in target_count and window_count[char] < target_count[char]:
                formed -= 1

            left += 1

    return s[min_window[0]:min_window[1] + 1] if min_len != float('inf') else ""


def character_replacement(s: str, k: int) -> int:
    """
    LeetCode 424 - Longest repeating character replacement.

    Time: O(n), Space: O(1) - max 26 letters
    Tricky: Window length - max_freq <= k (replacements allowed)
    """
    count = {}
    max_freq = 0
    max_length = 0
    left = 0

    for right, char in enumerate(s):
        count[char] = count.get(char, 0) + 1
        max_freq = max(max_freq, count[char])

        # If replacements needed > k, shrink window
        window_size = right - left + 1
        if window_size - max_freq > k:
            count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


# ============================================================================
# PATTERN 4: STRING BUILDER (for mutable operations)
# ============================================================================

def compress_string(s: str) -> str:
    """
    LeetCode 443 - String compression (modify array in-place for chars).

    Time: O(n), Space: O(1) excluding output
    Tricky: Use list as string builder in Python
    """
    if not s:
        return ""

    result = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1])
            if count > 1:
                result.append(str(count))
            count = 1

    # Don't forget last group
    result.append(s[-1])
    if count > 1:
        result.append(str(count))

    compressed = ''.join(result)
    return compressed if len(compressed) < len(s) else s


def encode_decode_strings():
    """
    LeetCode 271 - Encode and decode strings.

    Tricky: Handle delimiter that might appear in strings
    """
    class Codec:
        def encode(self, strs: List[str]) -> str:
            """Encode list of strings to a single string."""
            # Format: "length:string"
            return ''.join(f"{len(s)}:{s}" for s in strs)

        def decode(self, s: str) -> List[str]:
            """Decode single string to list of strings."""
            result = []
            i = 0

            while i < len(s):
                # Find delimiter
                colon = s.index(':', i)
                length = int(s[i:colon])

                # Extract string of given length
                i = colon + 1
                result.append(s[i:i + length])
                i += length

            return result

    return Codec()


# ============================================================================
# PATTERN 5: STRING MATCHING
# ============================================================================

def str_str(haystack: str, needle: str) -> int:
    """
    LeetCode 28 - Find first occurrence of substring.

    Time: O(n*m) naive, O(n+m) KMP, Space: O(m) for KMP
    """
    if not needle:
        return 0

    # Built-in
    # return haystack.find(needle)

    # KMP Algorithm
    def build_lps(pattern: str) -> List[int]:
        """Build Longest Prefix Suffix array."""
        lps = [0] * len(pattern)
        length = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    lps = build_lps(needle)
    i = j = 0

    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1

        if j == len(needle):
            return i - j
        elif i < len(haystack) and haystack[i] != needle[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1


def repeated_substring_pattern(s: str) -> bool:
    """
    LeetCode 459 - Check if string can be constructed by repeating substring.

    Time: O(n), Space: O(n)
    Tricky: (s + s)[1:-1] should contain s if pattern exists
    """
    return s in (s + s)[1:-1]


# ============================================================================
# PATTERN 6: PARENTHESES / BRACKETS
# ============================================================================

def is_valid_parentheses(s: str) -> bool:
    """
    LeetCode 20 - Valid parentheses.

    Time: O(n), Space: O(n)
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)

    return not stack


def generate_parentheses(n: int) -> List[str]:
    """
    LeetCode 22 - Generate all valid parentheses combinations.

    Time: O(4^n / sqrt(n)) Catalan number, Space: O(n) recursion depth
    Tricky: Use backtracking with constraints
    """
    result = []

    def backtrack(current: List[str], open_count: int, close_count: int):
        if len(current) == 2 * n:
            result.append(''.join(current))
            return

        # Can add '(' if not reached n
        if open_count < n:
            current.append('(')
            backtrack(current, open_count + 1, close_count)
            current.pop()

        # Can add ')' if it won't exceed '('
        if close_count < open_count:
            current.append(')')
            backtrack(current, open_count, close_count + 1)
            current.pop()

    backtrack([], 0, 0)
    return result


def longest_valid_parentheses(s: str) -> int:
    """
    LeetCode 32 - Longest valid parentheses substring.

    Time: O(n), Space: O(n)
    Tricky: Use stack with indices
    """
    stack = [-1]
    max_length = 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])

    return max_length


# ============================================================================
# PATTERN 7: SUBSEQUENCE / SUBSTRING
# ============================================================================

def is_subsequence(s: str, t: str) -> bool:
    """
    LeetCode 392 - Check if s is subsequence of t.

    Time: O(n), Space: O(1)
    """
    i = 0
    for char in t:
        if i < len(s) and s[i] == char:
            i += 1
    return i == len(s)


def num_distinct_subsequences(s: str, t: str) -> int:
    """
    LeetCode 115 - Distinct subsequences (DP).

    Time: O(m*n), Space: O(n)
    Tricky: dp[i][j] = count of t[:j] in s[:i]
    """
    m, n = len(s), len(t)

    # dp[j] = number of ways to form t[:j] from current prefix of s
    dp = [0] * (n + 1)
    dp[0] = 1  # Empty string has one subsequence (empty)

    for i in range(1, m + 1):
        # Traverse backwards to avoid overwriting needed values
        for j in range(n, 0, -1):
            if s[i-1] == t[j-1]:
                dp[j] += dp[j-1]

    return dp[n]


def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    LeetCode 1143 - Longest common subsequence.

    Time: O(m*n), Space: O(min(m,n))
    """
    if len(text1) < len(text2):
        text1, text2 = text2, text1

    m, n = len(text1), len(text2)
    prev = [0] * (n + 1)

    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                curr[j] = prev[j-1] + 1
            else:
                curr[j] = max(curr[j-1], prev[j])
        prev = curr

    return prev[n]


# ============================================================================
# PATTERN 8: PALINDROME VARIATIONS
# ============================================================================

def longest_palindromic_subsequence(s: str) -> int:
    """
    LeetCode 516 - Longest palindromic subsequence (DP).

    Time: O(n²), Space: O(n)
    Tricky: LPS(s) = LCS(s, reverse(s))
    """
    n = len(s)
    prev = [0] * n

    for i in range(n - 1, -1, -1):
        curr = [0] * n
        curr[i] = 1  # Single character is palindrome

        for j in range(i + 1, n):
            if s[i] == s[j]:
                curr[j] = prev[j-1] + 2
            else:
                curr[j] = max(curr[j-1], prev[j])

        prev = curr

    return prev[n-1]


def count_palindromic_substrings(s: str) -> int:
    """
    LeetCode 647 - Count all palindromic substrings.

    Time: O(n²), Space: O(1)
    """
    def expand_around_center(left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

    total = 0
    for i in range(len(s)):
        # Odd length palindromes
        total += expand_around_center(i, i)
        # Even length palindromes
        total += expand_around_center(i, i + 1)

    return total


# ============================================================================
# PYTHON STRING OPERATIONS & TRICKS
# ============================================================================

def python_string_tricks():
    """Common Python string operations and gotchas."""

    # String concatenation - DON'T do this in loop!
    # result = ""
    # for s in strings:
    #     result += s  # O(n²) because strings are immutable

    # Use join instead - O(n)
    strings = ['hello', 'world']
    result = ''.join(strings)  # 'helloworld'
    result = ' '.join(strings)  # 'hello world'

    # String methods
    s = "  Hello World  "
    s.strip()          # Remove whitespace
    s.lower()          # Lowercase
    s.upper()          # Uppercase
    s.split()          # Split by whitespace
    s.replace('o', '0')  # Replace
    s.startswith('He')  # Check prefix
    s.endswith('ld')    # Check suffix

    # String formatting
    name, age = "Alice", 25
    f"Name: {name}, Age: {age}"  # f-strings (Python 3.6+)
    "Name: {}, Age: {}".format(name, age)  # .format()
    "Name: %s, Age: %d" % (name, age)  # Old style

    # Character operations
    ord('A')  # 65 (ASCII value)
    chr(65)   # 'A' (character from ASCII)

    # Check character types
    'a'.isalpha()   # True
    '1'.isdigit()   # True
    'a1'.isalnum()  # True
    ' '.isspace()   # True

    # String multiplication
    '-' * 50  # '----...' (50 dashes)

    # Raw strings (no escape)
    r"\n"  # Literal backslash-n, not newline

    # Multi-line strings
    text = """
    Line 1
    Line 2
    """

    # String interning
    a = "hello"
    b = "hello"
    a is b  # True (interned)

    c = "hello world"
    d = "hello world"
    c is d  # May be False (not interned if contains space/special chars)
    c == d  # Always True (value comparison)

    # List of characters to string
    chars = ['h', 'e', 'l', 'l', 'o']
    ''.join(chars)  # 'hello'

    # String to list of characters
    list('hello')  # ['h', 'e', 'l', 'l', 'o']


# ============================================================================
# PRACTICE PROBLEMS
# ============================================================================
"""
EASY:
- Valid Anagram (242)
- Valid Palindrome (125)
- First Unique Character (387)
- Reverse String (344)

MEDIUM:
- Longest Substring Without Repeating Characters (3)
- Longest Palindromic Substring (5)
- Group Anagrams (49)
- Decode String (394)
- Longest Repeating Character Replacement (424)

HARD:
- Minimum Window Substring (76)
- Longest Valid Parentheses (32)
- Distinct Subsequences (115)
- Edit Distance (72)
- Regular Expression Matching (10)
"""

if __name__ == "__main__":
    # Test examples
    print("Is Anagram:", is_anagram("anagram", "nagaram"))
    print("Group Anagrams:", group_anagrams(
        ["eat", "tea", "tan", "ate", "nat", "bat"]))
    print("Longest Substring:", longest_substring_without_repeating("abcabcbb"))
    print("Valid Parentheses:", is_valid_parentheses("()[]{}"))
