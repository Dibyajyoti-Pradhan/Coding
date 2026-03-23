"""
SLIDING WINDOW - Complete Guide for Interview Preparation
==========================================================

CORE CONCEPTS:
--------------
1. Sliding window maintains a contiguous subarray/substring
2. Two types: Fixed size and Variable size
3. Reduces time from O(n²) to O(n) by avoiding recomputation
4. Common for substring, subarray problems with constraints

TRICKY PARTS:
-------------
1. When to expand vs shrink the window
2. What to store in window state (hashmap, counter, sum, etc.)
3. Fixed vs variable size - different templates
4. When the answer is updated (during expand or shrink)

COMMON PATTERNS:
----------------
1. Fixed Size Window
2. Variable Size - Maximum Window
3. Variable Size - Minimum Window
4. Distinct Elements Constraint
5. At Most K Pattern
"""

from typing import List, Dict
from collections import Counter, defaultdict


# ============================================================================
# PATTERN 1: FIXED SIZE WINDOW
# ============================================================================

def max_sum_subarray_size_k(nums: List[int], k: int) -> int:
    """
    Maximum sum of subarray of size k.

    Time: O(n), Space: O(1)
    Template: Fixed size sliding window
    """
    if len(nums) < k:
        return 0

    # Initial window
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide window
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)

    return max_sum


def max_avg_subarray(nums: List[int], k: int) -> float:
    """
    LeetCode 643 - Maximum average of subarray of size k.

    Time: O(n), Space: O(1)
    """
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)

    return max_sum / k


def count_good_substrings(s: str) -> int:
    """
    LeetCode 1876 - Count substrings of length 3 with distinct characters.

    Time: O(n), Space: O(1)
    """
    if len(s) < 3:
        return 0

    count = 0

    for i in range(len(s) - 2):
        window = s[i:i+3]
        if len(set(window)) == 3:
            count += 1

    return count


def num_of_subarrays(arr: List[int], k: int, threshold: int) -> int:
    """
    LeetCode 1343 - Number of subarrays of size k with average >= threshold.

    Time: O(n), Space: O(1)
    """
    count = 0
    target_sum = k * threshold

    window_sum = sum(arr[:k])
    if window_sum >= target_sum:
        count += 1

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        if window_sum >= target_sum:
            count += 1

    return count


# ============================================================================
# PATTERN 2: VARIABLE SIZE - MAXIMUM WINDOW
# ============================================================================

def longest_substring_without_repeating(s: str) -> int:
    """
    LeetCode 3 - Longest substring without repeating characters.

    Time: O(n), Space: O(min(m, n)) where m is charset size
    Template: Variable size, maximize window
    """
    char_index = {}
    max_length = 0
    left = 0

    for right, char in enumerate(s):
        # If character seen and within current window
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1

        char_index[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length


def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    """
    LeetCode 340 - Longest substring with at most k distinct characters.

    Time: O(n), Space: O(k)
    """
    if k == 0:
        return 0

    char_count = {}
    max_length = 0
    left = 0

    for right, char in enumerate(s):
        # Expand window
        char_count[char] = char_count.get(char, 0) + 1

        # Shrink window if constraint violated
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


def character_replacement(s: str, k: int) -> int:
    """
    LeetCode 424 - Longest repeating character replacement.

    Time: O(n), Space: O(1) - max 26 letters
    Tricky: window_length - max_freq <= k
    """
    char_count = {}
    max_freq = 0
    max_length = 0
    left = 0

    for right, char in enumerate(s):
        char_count[char] = char_count.get(char, 0) + 1
        max_freq = max(max_freq, char_count[char])

        # If replacements needed > k, shrink window
        window_size = right - left + 1
        if window_size - max_freq > k:
            char_count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


def max_consecutive_ones_iii(nums: List[int], k: int) -> int:
    """
    LeetCode 1004 - Max consecutive 1s after flipping at most k zeros.

    Time: O(n), Space: O(1)
    """
    left = 0
    zero_count = 0
    max_length = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


def length_of_longest_subarray_at_most_k(nums: List[int], k: int) -> int:
    """
    Longest subarray with sum <= k.

    Time: O(n), Space: O(1)
    """
    left = 0
    current_sum = 0
    max_length = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum > k:
            current_sum -= nums[left]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


# ============================================================================
# PATTERN 3: VARIABLE SIZE - MINIMUM WINDOW
# ============================================================================

def min_size_subarray_sum(target: int, nums: List[int]) -> int:
    """
    LeetCode 209 - Minimum size subarray sum >= target.

    Time: O(n), Space: O(1)
    Template: Variable size, minimize window
    """
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0


def min_window_substring(s: str, t: str) -> str:
    """
    LeetCode 76 - Minimum window substring containing all characters of t.

    Time: O(|s| + |t|), Space: O(|s| + |t|)
    Tricky: Track formed characters count
    """
    if not s or not t:
        return ""

    target_count = Counter(t)
    required = len(target_count)

    window_count = defaultdict(int)
    formed = 0  # Number of unique chars with desired frequency

    left = 0
    min_len = float('inf')
    result = (0, 0)

    for right, char in enumerate(s):
        # Expand window
        window_count[char] += 1

        if char in target_count and window_count[char] == target_count[char]:
            formed += 1

        # Shrink window
        while left <= right and formed == required:
            # Update result
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = (left, right)

            # Remove leftmost character
            char = s[left]
            window_count[char] -= 1
            if char in target_count and window_count[char] < target_count[char]:
                formed -= 1

            left += 1

    return s[result[0]:result[1] + 1] if min_len != float('inf') else ""


def min_consecutive_cards_to_pick_up(cards: List[int]) -> int:
    """
    LeetCode 2260 - Minimum consecutive cards to pick up a pair.

    Time: O(n), Space: O(n)
    """
    last_seen = {}
    min_length = float('inf')

    for i, card in enumerate(cards):
        if card in last_seen:
            min_length = min(min_length, i - last_seen[card] + 1)
        last_seen[card] = i

    return min_length if min_length != float('inf') else -1


# ============================================================================
# PATTERN 4: PERMUTATION IN STRING
# ============================================================================

def check_inclusion(s1: str, s2: str) -> bool:
    """
    LeetCode 567 - Permutation in string (is s1 permutation in s2).

    Time: O(n), Space: O(1)
    Tricky: Fixed window of len(s1), check if counts match
    """
    if len(s1) > len(s2):
        return False

    s1_count = Counter(s1)
    window_count = Counter(s2[:len(s1)])

    if s1_count == window_count:
        return True

    for i in range(len(s1), len(s2)):
        # Add new character
        window_count[s2[i]] += 1

        # Remove old character
        old_char = s2[i - len(s1)]
        window_count[old_char] -= 1
        if window_count[old_char] == 0:
            del window_count[old_char]

        if s1_count == window_count:
            return True

    return False


def find_anagrams(s: str, p: str) -> List[int]:
    """
    LeetCode 438 - Find all anagrams of p in s.

    Time: O(n), Space: O(1)
    """
    if len(p) > len(s):
        return []

    result = []
    p_count = Counter(p)
    window_count = Counter(s[:len(p)])

    if p_count == window_count:
        result.append(0)

    for i in range(len(p), len(s)):
        # Add new character
        window_count[s[i]] += 1

        # Remove old character
        old_char = s[i - len(p)]
        window_count[old_char] -= 1
        if window_count[old_char] == 0:
            del window_count[old_char]

        if p_count == window_count:
            result.append(i - len(p) + 1)

    return result


# ============================================================================
# PATTERN 5: AT MOST K PATTERN
# ============================================================================

def subarrays_with_k_different(nums: List[int], k: int) -> int:
    """
    LeetCode 992 - Subarrays with exactly k different integers.

    Time: O(n), Space: O(k)
    Tricky: exactly k = at_most(k) - at_most(k-1)
    """
    def at_most_k(k: int) -> int:
        count = {}
        left = 0
        result = 0

        for right in range(len(nums)):
            count[nums[right]] = count.get(nums[right], 0) + 1

            while len(count) > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1

            # All subarrays ending at right with at most k distinct
            result += right - left + 1

        return result

    return at_most_k(k) - at_most_k(k - 1)


def num_subarrays_with_sum(nums: List[int], goal: int) -> int:
    """
    LeetCode 930 - Number of subarrays with sum equal to goal.

    Time: O(n), Space: O(1)
    Tricky: exactly goal = at_most(goal) - at_most(goal-1)
    """
    def at_most(goal: int) -> int:
        if goal < 0:
            return 0

        left = 0
        current_sum = 0
        count = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum > goal:
                current_sum -= nums[left]
                left += 1

            count += right - left + 1

        return count

    return at_most(goal) - at_most(goal - 1)


# ============================================================================
# PATTERN 6: STRING PALINDROME WINDOW
# ============================================================================

def longest_palindrome_substring(s: str) -> str:
    """
    LeetCode 5 - Longest palindromic substring.

    Time: O(n²), Space: O(1)
    Not traditional sliding window, but expand around center
    """
    def expand_around_center(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    if not s:
        return ""

    start = end = 0

    for i in range(len(s)):
        # Odd length palindrome
        len1 = expand_around_center(i, i)
        # Even length palindrome
        len2 = expand_around_center(i, i + 1)

        max_len = max(len1, len2)

        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]


# ============================================================================
# PATTERN 7: FRUIT BASKET / AT MOST K TYPES
# ============================================================================

def total_fruit(fruits: List[int]) -> int:
    """
    LeetCode 904 - Fruit into baskets (at most 2 types).

    Time: O(n), Space: O(1)
    Same as: longest subarray with at most 2 distinct elements
    """
    fruit_count = {}
    max_fruits = 0
    left = 0

    for right in range(len(fruits)):
        fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1

        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1

        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits


# ============================================================================
# ADVANCED PROBLEMS
# ============================================================================

def max_sliding_window(nums: List[int], k: int) -> List[int]:
    """
    LeetCode 239 - Sliding window maximum.

    Time: O(n), Space: O(k)
    Tricky: Use monotonic deque
    """
    from collections import deque

    dq = deque()  # Store indices
    result = []

    for i, num in enumerate(nums):
        # Remove indices outside window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller elements (maintain decreasing order)
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        # Add to result when window is formed
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


# ============================================================================
# PRACTICE PROBLEMS
# ============================================================================
"""
EASY:
- Maximum Average Subarray I (643)
- Minimum Consecutive Cards (2260)

MEDIUM:
- Longest Substring Without Repeating Characters (3)
- Longest Repeating Character Replacement (424)
- Permutation in String (567)
- Find All Anagrams (438)
- Fruit Into Baskets (904)
- Max Consecutive Ones III (1004)
- Minimum Size Subarray Sum (209)

HARD:
- Minimum Window Substring (76)
- Sliding Window Maximum (239)
- Subarrays with K Different Integers (992)
"""

if __name__ == "__main__":
    # Test examples
    print("Max Sum K:", max_sum_subarray_size_k([1, 2, 3, 4, 5], 3))
    print("Longest Unique:", longest_substring_without_repeating("abcabcbb"))
    print("Min Window:", min_window_substring("ADOBECODEBANC", "ABC"))
    print("Check Inclusion:", check_inclusion("ab", "eidbaooo"))
    print("Max Sliding Window:", max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
