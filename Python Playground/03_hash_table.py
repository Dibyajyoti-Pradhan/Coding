"""
HASH TABLE - Complete Guide for Interview Preparation
======================================================

CORE CONCEPTS:
--------------
1. Hash tables provide O(1) average case lookup, insert, delete
2. Python dict and set are implemented as hash tables
3. Hash function maps keys to indices in underlying array
4. Collision resolution: chaining (Python uses open addressing)
5. Load factor: n/capacity (Python resizes at ~2/3 full)

TRICKY PARTS:
-------------
1. Hash collisions can degrade performance to O(n) worst case
2. Keys must be hashable (immutable): str, int, tuple OK; list, dict NOT OK
3. Dictionary order is PRESERVED in Python 3.7+ (insertion order)
4. get() vs [] for access: get() returns None, [] raises KeyError
5. defaultdict vs dict: defaultdict auto-creates missing keys
6. Counter is a subclass of dict for counting hashable objects

COMMON PATTERNS:
----------------
1. Frequency counting
2. Two-sum type problems (complement lookup)
3. Grouping/categorization
4. Caching/memoization
5. Deduplication
6. Prefix sum with hash map
"""

from typing import List, Dict, Optional, Set
from collections import defaultdict, Counter, OrderedDict
import heapq


# ============================================================================
# PATTERN 1: FREQUENCY COUNTING
# ============================================================================

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    LeetCode 1 - Find two numbers that add up to target.

    Time: O(n), Space: O(n)
    Tricky: Use hashmap to store complement
    """
    num_map = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

    return []


def top_k_frequent_elements(nums: List[int], k: int) -> List[int]:
    """
    LeetCode 347 - Find k most frequent elements.

    Time: O(n log k) with heap, O(n) with bucket sort
    Space: O(n)
    """
    # Approach 1: Using heap
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

    # Approach 2: Bucket sort (O(n) time)
    # count = Counter(nums)
    # buckets = [[] for _ in range(len(nums) + 1)]
    #
    # for num, freq in count.items():
    #     buckets[freq].append(num)
    #
    # result = []
    # for i in range(len(buckets) - 1, 0, -1):
    #     result.extend(buckets[i])
    #     if len(result) >= k:
    #         return result[:k]
    #
    # return result


def frequency_sort(s: str) -> str:
    """
    LeetCode 451 - Sort characters by frequency.

    Time: O(n log n), Space: O(n)
    """
    count = Counter(s)

    # Sort by frequency (descending), then by character
    sorted_chars = sorted(count.items(), key=lambda x: -x[1])

    return ''.join(char * freq for char, freq in sorted_chars)


# ============================================================================
# PATTERN 2: GROUPING / CATEGORIZATION
# ============================================================================

def group_shifted_strings(strings: List[str]) -> List[List[str]]:
    """
    LeetCode 249 - Group strings that are shifts of each other.

    Time: O(n * k) where k is max string length, Space: O(n*k)
    Tricky: Create hash key based on shift pattern
    """
    def get_hash(s: str) -> tuple:
        """Generate hash based on shift differences."""
        if not s:
            return ()

        # Calculate differences between consecutive characters
        diffs = []
        for i in range(1, len(s)):
            diff = (ord(s[i]) - ord(s[i-1])) % 26
            diffs.append(diff)

        return tuple(diffs)

    groups = defaultdict(list)

    for s in strings:
        key = get_hash(s)
        groups[key].append(s)

    return list(groups.values())


def find_duplicate_subtrees(root):
    """
    LeetCode 652 - Find duplicate subtrees.

    Tricky: Use serialization as hash key
    """
    from collections import defaultdict

    def serialize(node):
        if not node:
            return "#"

        serial = f"{node.val},{serialize(node.left)},{serialize(node.right)}"

        subtrees[serial].append(node)
        return serial

    subtrees = defaultdict(list)
    serialize(root)

    return [nodes[0] for nodes in subtrees.values() if len(nodes) > 1]


# ============================================================================
# PATTERN 3: PREFIX SUM WITH HASH MAP
# ============================================================================

def subarray_sum_equals_k(nums: List[int], k: int) -> int:
    """
    LeetCode 560 - Count subarrays with sum equals k.

    Time: O(n), Space: O(n)
    Tricky: prefix_sum[j] - prefix_sum[i] = k means subarray[i+1:j+1] sums to k
    """
    count = 0
    prefix_sum = 0
    sum_freq = {0: 1}  # Handle case when prefix_sum itself equals k

    for num in nums:
        prefix_sum += num

        # Check if there exists a prefix with sum = prefix_sum - k
        if prefix_sum - k in sum_freq:
            count += sum_freq[prefix_sum - k]

        sum_freq[prefix_sum] = sum_freq.get(prefix_sum, 0) + 1

    return count


def continuous_subarray_sum(nums: List[int], k: int) -> bool:
    """
    LeetCode 523 - Check if subarray with sum multiple of k exists (length >= 2).

    Time: O(n), Space: O(min(n, k))
    Tricky: Use modulo arithmetic and store remainders
    """
    if len(nums) < 2:
        return False

    # Store remainder -> index
    remainder_map = {0: -1}  # Handle case when prefix sum itself is multiple of k
    prefix_sum = 0

    for i, num in enumerate(nums):
        prefix_sum += num

        if k != 0:
            remainder = prefix_sum % k
        else:
            remainder = prefix_sum

        if remainder in remainder_map:
            # Check if length >= 2
            if i - remainder_map[remainder] >= 2:
                return True
        else:
            remainder_map[remainder] = i

    return False


def max_subarray_sum_divisible_by_k(nums: List[int], k: int) -> int:
    """
    LeetCode 974 - Count subarrays divisible by k.

    Time: O(n), Space: O(k)
    """
    prefix_sum = 0
    # Remainder -> count
    remainder_count = {0: 1}
    result = 0

    for num in nums:
        prefix_sum += num
        remainder = prefix_sum % k

        # Python's modulo can be negative, normalize to [0, k)
        if remainder < 0:
            remainder += k

        # Add count of previous subarrays with same remainder
        result += remainder_count.get(remainder, 0)
        remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

    return result


# ============================================================================
# PATTERN 4: DEDUPLICATION
# ============================================================================

def contains_duplicate(nums: List[int]) -> bool:
    """
    LeetCode 217 - Check if array contains duplicates.

    Time: O(n), Space: O(n)
    """
    return len(nums) != len(set(nums))


def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    """
    LeetCode 219 - Check if duplicate exists within k distance.

    Time: O(n), Space: O(min(n, k))
    """
    seen = {}

    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i

    return False


def contains_nearby_almost_duplicate(nums: List[int], index_diff: int, value_diff: int) -> bool:
    """
    LeetCode 220 - Check if |nums[i] - nums[j]| <= value_diff and |i - j| <= index_diff.

    Time: O(n), Space: O(min(n, k))
    Tricky: Use buckets based on value_diff
    """
    if value_diff < 0 or index_diff < 0:
        return False

    # Bucket size is value_diff + 1
    bucket_size = value_diff + 1
    buckets = {}

    for i, num in enumerate(nums):
        bucket_id = num // bucket_size

        # Check same bucket
        if bucket_id in buckets:
            return True

        # Check adjacent buckets
        if bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) <= value_diff:
            return True
        if bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) <= value_diff:
            return True

        buckets[bucket_id] = num

        # Maintain sliding window of size index_diff
        if i >= index_diff:
            del buckets[nums[i - index_diff] // bucket_size]

    return False


# ============================================================================
# PATTERN 5: HASH MAP FOR OPTIMIZATION
# ============================================================================

def four_sum_count(nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    """
    LeetCode 454 - Count tuples (i,j,k,l) where nums1[i] + ... + nums4[l] = 0.

    Time: O(n²), Space: O(n²)
    Tricky: Split into two groups
    """
    # Store all possible sums of first two arrays
    sum_count = Counter()
    for a in nums1:
        for b in nums2:
            sum_count[a + b] += 1

    # Check complement in remaining two arrays
    count = 0
    for c in nums3:
        for d in nums4:
            count += sum_count[-(c + d)]

    return count


def longest_consecutive_sequence(nums: List[int]) -> int:
    """
    LeetCode 128 - Longest consecutive sequence.

    Time: O(n), Space: O(n)
    Tricky: Only start counting from sequence start
    """
    if not nums:
        return 0

    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # Only start counting if it's the start of sequence
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            max_length = max(max_length, length)

    return max_length


# ============================================================================
# PATTERN 6: LRU CACHE / ORDERED DICT
# ============================================================================

class LRUCache:
    """
    LeetCode 146 - LRU Cache implementation.

    Time: O(1) for get and put
    Tricky: Use OrderedDict or implement doubly linked list + hashmap
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # Move to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update and move to end
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                # Remove least recently used (first item)
                self.cache.popitem(last=False)

        self.cache[key] = value


class LRUCacheManual:
    """
    LRU Cache using doubly linked list + hashmap (without OrderedDict).

    More commonly asked in interviews to implement from scratch.
    """

    class Node:
        def __init__(self, key: int, value: int):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Dummy head and tail
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove node from linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node):
        """Add node right after head."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        # Move to head (most recently used)
        self._remove(node)
        self._add_to_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and move to head
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else:
            if len(self.cache) >= self.capacity:
                # Remove LRU (node before tail)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]

            # Add new node
            new_node = self.Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)


# ============================================================================
# PATTERN 7: ISOMORPHIC / BIJECTION
# ============================================================================

def is_isomorphic(s: str, t: str) -> bool:
    """
    LeetCode 205 - Check if two strings are isomorphic.

    Time: O(n), Space: O(1) - max 256 chars
    Tricky: Need bijection (one-to-one mapping both ways)
    """
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for char_s, char_t in zip(s, t):
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        else:
            s_to_t[char_s] = char_t

        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False
        else:
            t_to_s[char_t] = char_s

    return True


def word_pattern(pattern: str, s: str) -> bool:
    """
    LeetCode 290 - Word pattern matching.

    Time: O(n), Space: O(n)
    """
    words = s.split()

    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}

    for char, word in zip(pattern, words):
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word

        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char

    return True


# ============================================================================
# PYTHON DICT/SET TRICKS
# ============================================================================

def python_hashmap_tricks():
    """Common Python dict and set operations."""

    # Dictionary creation
    d = {'a': 1, 'b': 2}
    d = dict(a=1, b=2)
    d = dict([('a', 1), ('b', 2)])
    d = {k: v for k, v in [('a', 1), ('b', 2)]}  # Dict comprehension

    # Access
    d['a']  # KeyError if not exists
    d.get('a')  # None if not exists
    d.get('a', 0)  # Default value
    d.setdefault('c', 3)  # Set if not exists, return value

    # Modify
    d['a'] = 10
    d.update({'c': 3, 'd': 4})
    d.pop('a')  # Remove and return
    d.popitem()  # Remove and return arbitrary (last in 3.7+) item
    del d['b']

    # Iterate
    for key in d:
        pass
    for key, value in d.items():
        pass
    for key in d.keys():
        pass
    for value in d.values():
        pass

    # defaultdict - auto-create missing keys
    dd = defaultdict(int)  # Default value 0
    dd['count'] += 1  # No KeyError

    dd = defaultdict(list)  # Default value []
    dd['items'].append(1)

    dd = defaultdict(lambda: 'default')  # Custom default

    # Counter - count hashable objects
    c = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
    # Counter({'a': 3, 'b': 2, 'c': 1})

    c.most_common(2)  # [('a', 3), ('b', 2)]
    c['d']  # 0 (returns 0 for missing keys)

    # Counter arithmetic
    c1 = Counter(['a', 'b', 'a'])
    c2 = Counter(['a', 'c'])
    c1 + c2  # Counter({'a': 3, 'b': 1, 'c': 1})
    c1 - c2  # Counter({'a': 1, 'b': 1})
    c1 & c2  # Intersection: min(c1[x], c2[x])
    c1 | c2  # Union: max(c1[x], c2[x])

    # Set operations
    s1 = {1, 2, 3}
    s2 = {2, 3, 4}

    s1 | s2  # Union: {1, 2, 3, 4}
    s1 & s2  # Intersection: {2, 3}
    s1 - s2  # Difference: {1}
    s1 ^ s2  # Symmetric difference: {1, 4}

    s1.add(4)
    s1.remove(1)  # KeyError if not exists
    s1.discard(1)  # No error if not exists

    # Set comprehension
    squares = {x**2 for x in range(10)}

    # Frozen set (immutable)
    fs = frozenset([1, 2, 3])  # Can be used as dict key


# ============================================================================
# PRACTICE PROBLEMS
# ============================================================================
"""
EASY:
- Two Sum (1)
- Valid Anagram (242)
- Contains Duplicate (217)
- Isomorphic Strings (205)

MEDIUM:
- Group Anagrams (49)
- Top K Frequent Elements (347)
- Subarray Sum Equals K (560)
- Longest Consecutive Sequence (128)
- 4Sum II (454)

HARD:
- LRU Cache (146)
- All O(1) Data Structure (432)
- Substring with Concatenation of All Words (30)
"""

if __name__ == "__main__":
    # Test examples
    print("Two Sum:", two_sum([2, 7, 11, 15], 9))
    print("Top K Frequent:", top_k_frequent_elements([1, 1, 1, 2, 2, 3], 2))
    print("Longest Consecutive:", longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))

    # LRU Cache test
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print("LRU Get 1:", cache.get(1))  # 1
    cache.put(3, 3)  # Evicts key 2
    print("LRU Get 2:", cache.get(2))  # -1
