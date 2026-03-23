"""
PYTHON IN-PLACE VS EXTERNAL MODIFICATION GUIDE
==============================================

This guide explains how Python handles in-place modification versus external (out-of-place)
modification, covering mutable vs immutable types, memory implications, and common pitfalls.

TABLE OF CONTENTS:
1. Mutable vs Immutable Types
2. In-Place Modification
3. External/Out-of-Place Modification
4. Function Parameters and Mutability
5. Common Pitfalls and Gotchas
6. Memory Implications
7. Best Practices
"""

# ============================================================================
# 1. MUTABLE VS IMMUTABLE TYPES
# ============================================================================

"""
IMMUTABLE TYPES (Cannot be modified in-place):
- int, float, bool, complex
- str (strings)
- tuple
- frozenset
- bytes

MUTABLE TYPES (Can be modified in-place):
- list
- dict
- set
- bytearray
- custom objects (usually)
"""

def demonstrate_immutability():
    """Strings and tuples cannot be modified in-place."""

    # STRINGS - Immutable
    s = "hello"
    original_id = id(s)
    s = s + " world"  # Creates NEW string object
    new_id = id(s)
    print(f"String IDs different: {original_id != new_id}")  # True

    # TUPLES - Immutable
    t = (1, 2, 3)
    original_id = id(t)
    # t[0] = 10  # TypeError: 'tuple' object does not support item assignment
    t = t + (4,)  # Creates NEW tuple
    new_id = id(t)
    print(f"Tuple IDs different: {original_id != new_id}")  # True

    # INTEGERS - Immutable
    x = 5
    original_id = id(x)
    x += 1  # Creates NEW integer object
    new_id = id(x)
    print(f"Integer IDs different: {original_id != new_id}")  # True


def demonstrate_mutability():
    """Lists and dicts can be modified in-place."""

    # LISTS - Mutable
    lst = [1, 2, 3]
    original_id = id(lst)
    lst.append(4)  # Modifies SAME list object
    new_id = id(lst)
    print(f"List ID same after append: {original_id == new_id}")  # True

    # DICTIONARIES - Mutable
    d = {"a": 1}
    original_id = id(d)
    d["b"] = 2  # Modifies SAME dict object
    new_id = id(d)
    print(f"Dict ID same after adding key: {original_id == new_id}")  # True

    # SETS - Mutable
    s = {1, 2, 3}
    original_id = id(s)
    s.add(4)  # Modifies SAME set object
    new_id = id(s)
    print(f"Set ID same after add: {original_id == new_id}")  # True


# ============================================================================
# 2. IN-PLACE MODIFICATION
# ============================================================================

"""
IN-PLACE MODIFICATION:
- Modifies the original object directly
- Does not create a new object
- Memory efficient for large objects
- Typically returns None (methods like append, sort)
- Changes affect all references to the object
"""

def in_place_list_operations():
    """Common in-place list operations."""

    # append() - adds element at end
    lst = [1, 2, 3]
    result = lst.append(4)  # Modifies lst, returns None
    print(f"After append: {lst}, returned: {result}")  # [1, 2, 3, 4], None

    # extend() - adds all elements from iterable
    lst.extend([5, 6])  # Modifies lst
    print(f"After extend: {lst}")  # [1, 2, 3, 4, 5, 6]

    # insert() - inserts at specific index
    lst.insert(0, 0)  # Modifies lst
    print(f"After insert: {lst}")  # [0, 1, 2, 3, 4, 5, 6]

    # remove() - removes first occurrence
    lst.remove(3)  # Modifies lst
    print(f"After remove: {lst}")  # [0, 1, 2, 4, 5, 6]

    # pop() - removes and returns element
    val = lst.pop()  # Modifies lst, returns value
    print(f"After pop: {lst}, returned: {val}")  # [0, 1, 2, 4, 5], 6

    # reverse() - reverses in-place
    lst.reverse()  # Modifies lst
    print(f"After reverse: {lst}")  # [5, 4, 2, 1, 0]

    # sort() - sorts in-place
    lst.sort()  # Modifies lst
    print(f"After sort: {lst}")  # [0, 1, 2, 4, 5]

    # clear() - removes all elements
    lst.clear()  # Modifies lst
    print(f"After clear: {lst}")  # []

    # Direct indexing - modifies element
    lst = [1, 2, 3]
    lst[0] = 10  # Modifies lst
    print(f"After index assignment: {lst}")  # [10, 2, 3]

    # Slice assignment - modifies slice
    lst[1:3] = [20, 30, 40]  # Modifies lst
    print(f"After slice assignment: {lst}")  # [10, 20, 30, 40]


def in_place_dict_operations():
    """Common in-place dict operations."""

    d = {"a": 1, "b": 2}

    # Direct key assignment
    d["c"] = 3  # Modifies d
    print(f"After adding key: {d}")  # {'a': 1, 'b': 2, 'c': 3}

    # update() - merges another dict
    d.update({"d": 4, "e": 5})  # Modifies d
    print(f"After update: {d}")  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

    # pop() - removes and returns value
    val = d.pop("c")  # Modifies d
    print(f"After pop: {d}, returned: {val}")  # {'a': 1, 'b': 2, 'd': 4, 'e': 5}, 3

    # popitem() - removes and returns arbitrary item
    item = d.popitem()  # Modifies d
    print(f"After popitem: {d}, returned: {item}")

    # clear() - removes all items
    d.clear()  # Modifies d
    print(f"After clear: {d}")  # {}


def in_place_set_operations():
    """Common in-place set operations."""

    s = {1, 2, 3}

    # add() - adds single element
    s.add(4)  # Modifies s
    print(f"After add: {s}")  # {1, 2, 3, 4}

    # update() - adds multiple elements
    s.update([5, 6])  # Modifies s
    print(f"After update: {s}")  # {1, 2, 3, 4, 5, 6}

    # remove() - removes element (raises error if not found)
    s.remove(3)  # Modifies s
    print(f"After remove: {s}")  # {1, 2, 4, 5, 6}

    # discard() - removes element (no error if not found)
    s.discard(10)  # Modifies s, no error
    print(f"After discard: {s}")  # {1, 2, 4, 5, 6}

    # Set operations with update variants (in-place)
    s.intersection_update({1, 2, 7})  # Modifies s
    print(f"After intersection_update: {s}")  # {1, 2}


# ============================================================================
# 3. EXTERNAL/OUT-OF-PLACE MODIFICATION
# ============================================================================

"""
EXTERNAL/OUT-OF-PLACE MODIFICATION:
- Creates and returns a new object
- Original object remains unchanged
- Less memory efficient (creates copy)
- Returns the new object (can be assigned to variable)
- Safe when you need to preserve original
"""

def out_of_place_operations():
    """Operations that create new objects."""

    # STRING OPERATIONS (always out-of-place)
    s = "hello"
    s_upper = s.upper()  # Creates new string
    print(f"Original: {s}, New: {s_upper}")  # hello, HELLO

    s_replaced = s.replace("l", "x")  # Creates new string
    print(f"Original: {s}, New: {s_replaced}")  # hello, hexxo

    s_concat = s + " world"  # Creates new string
    print(f"Original: {s}, New: {s_concat}")  # hello, hello world

    # LIST OPERATIONS (some create new lists)
    lst = [3, 1, 2]

    # sorted() - returns new sorted list
    sorted_lst = sorted(lst)  # Creates new list
    print(f"Original: {lst}, Sorted: {sorted_lst}")  # [3, 1, 2], [1, 2, 3]

    # List concatenation - creates new list
    new_lst = lst + [4, 5]  # Creates new list
    print(f"Original: {lst}, New: {new_lst}")  # [3, 1, 2], [3, 1, 2, 4, 5]

    # List slicing - creates new list
    sliced = lst[1:3]  # Creates new list
    print(f"Original: {lst}, Slice: {sliced}")  # [3, 1, 2], [1, 2]

    # List comprehension - creates new list
    doubled = [x * 2 for x in lst]  # Creates new list
    print(f"Original: {lst}, Doubled: {doubled}")  # [3, 1, 2], [6, 2, 4]

    # reversed() - returns iterator (can convert to list)
    reversed_lst = list(reversed(lst))  # Creates new list
    print(f"Original: {lst}, Reversed: {reversed_lst}")  # [3, 1, 2], [2, 1, 3]

    # DICT OPERATIONS (some create new dicts)
    d = {"a": 1, "b": 2}

    # dict comprehension - creates new dict
    doubled_dict = {k: v * 2 for k, v in d.items()}  # Creates new dict
    print(f"Original: {d}, Doubled: {doubled_dict}")  # {'a': 1, 'b': 2}, {'a': 2, 'b': 4}

    # Unpacking into new dict - creates new dict
    new_d = {**d, "c": 3}  # Creates new dict
    print(f"Original: {d}, New: {new_d}")  # {'a': 1, 'b': 2}, {'a': 1, 'b': 2, 'c': 3}

    # SET OPERATIONS (non-update variants create new sets)
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}

    # union() - creates new set
    union = s1.union(s2)  # Creates new set
    print(f"s1: {s1}, s2: {s2}, Union: {union}")  # {1, 2, 3}, {3, 4, 5}, {1, 2, 3, 4, 5}

    # intersection() - creates new set
    intersection = s1.intersection(s2)  # Creates new set
    print(f"Intersection: {intersection}")  # {3}


# ============================================================================
# 4. FUNCTION PARAMETERS AND MUTABILITY
# ============================================================================

"""
CRITICAL CONCEPT: Python passes objects by reference (object reference is passed by value)

For IMMUTABLE objects:
- Reassignment inside function doesn't affect original
- Creates new local object

For MUTABLE objects:
- Modifications inside function AFFECT the original
- Same object is being modified
"""

def immutable_parameter_example():
    """Demonstrates immutable parameters."""

    def try_modify_string(s):
        print(f"Inside function, before: {s}, id: {id(s)}")
        s = s + " modified"  # Creates NEW string, rebinds local variable
        print(f"Inside function, after: {s}, id: {id(s)}")
        return s

    original = "hello"
    original_id = id(original)
    print(f"Before function call: {original}, id: {original_id}")

    result = try_modify_string(original)

    print(f"After function call: {original}, id: {id(original)}")  # Unchanged!
    print(f"Returned value: {result}")  # Modified version
    print(f"Original unchanged: {original == 'hello'}")  # True


def mutable_parameter_example():
    """Demonstrates mutable parameters - DANGEROUS!"""

    def modify_list(lst):
        print(f"Inside function, before: {lst}, id: {id(lst)}")
        lst.append(4)  # Modifies ORIGINAL list
        print(f"Inside function, after: {lst}, id: {id(lst)}")

    original = [1, 2, 3]
    original_id = id(original)
    print(f"Before function call: {original}, id: {original_id}")

    modify_list(original)

    print(f"After function call: {original}, id: {id(original)}")  # CHANGED!
    print(f"Original modified: {original == [1, 2, 3, 4]}")  # True


def safe_function_patterns():
    """Safe patterns to avoid unintended mutations."""

    # PATTERN 1: Create a copy inside function
    def safe_modify_list_v1(lst):
        lst_copy = lst.copy()  # or lst[:]
        lst_copy.append(4)
        return lst_copy

    original = [1, 2, 3]
    result = safe_modify_list_v1(original)
    print(f"Original: {original}, Result: {result}")  # [1, 2, 3], [1, 2, 3, 4]

    # PATTERN 2: Use default parameter carefully
    # WRONG - mutable default argument (common pitfall!)
    def wrong_default(lst=[]):  # DANGER! Same list reused across calls
        lst.append(1)
        return lst

    print(wrong_default())  # [1]
    print(wrong_default())  # [1, 1] - UNEXPECTED!

    # CORRECT - use None as default
    def correct_default(lst=None):
        if lst is None:
            lst = []  # Create new list each time
        lst.append(1)
        return lst

    print(correct_default())  # [1]
    print(correct_default())  # [1] - EXPECTED!

    # PATTERN 3: Explicitly copy when calling
    original = [1, 2, 3]

    def modify_list(lst):
        lst.append(4)
        return lst

    result = modify_list(original.copy())  # Pass a copy
    print(f"Original: {original}, Result: {result}")  # [1, 2, 3], [1, 2, 3, 4]


# ============================================================================
# 5. COMMON PITFALLS AND GOTCHAS
# ============================================================================

def pitfall_list_copy():
    """Shallow copy vs deep copy."""

    # PITFALL: Shallow copy doesn't copy nested objects
    original = [[1, 2], [3, 4]]
    shallow = original.copy()  # or original[:]

    shallow[0].append(99)  # Modifies nested list in BOTH!
    print(f"Original: {original}")  # [[1, 2, 99], [3, 4]]
    print(f"Shallow: {shallow}")    # [[1, 2, 99], [3, 4]]

    # SOLUTION: Use deep copy for nested structures
    import copy
    original = [[1, 2], [3, 4]]
    deep = copy.deepcopy(original)

    deep[0].append(99)  # Only modifies deep copy
    print(f"Original: {original}")  # [[1, 2], [3, 4]]
    print(f"Deep: {deep}")         # [[1, 2, 99], [3, 4]]


def pitfall_list_multiplication():
    """List multiplication with mutable elements."""

    # PITFALL: Multiplying list with mutable objects
    wrong = [[]] * 3  # Creates 3 references to SAME list
    wrong[0].append(1)
    print(f"Wrong: {wrong}")  # [[1], [1], [1]] - all changed!

    # SOLUTION: Use list comprehension
    correct = [[] for _ in range(3)]  # Creates 3 DIFFERENT lists
    correct[0].append(1)
    print(f"Correct: {correct}")  # [[1], [], []]


def pitfall_loop_modification():
    """Modifying list while iterating."""

    # PITFALL: Modifying list during iteration
    lst = [1, 2, 3, 4, 5]
    # for x in lst:
    #     if x % 2 == 0:
    #         lst.remove(x)  # DANGER! Skips elements

    # SOLUTION 1: Iterate over copy
    lst = [1, 2, 3, 4, 5]
    for x in lst[:]:  # Iterate over copy
        if x % 2 == 0:
            lst.remove(x)
    print(f"Solution 1: {lst}")  # [1, 3, 5]

    # SOLUTION 2: Build new list (preferred)
    lst = [1, 2, 3, 4, 5]
    lst = [x for x in lst if x % 2 != 0]
    print(f"Solution 2: {lst}")  # [1, 3, 5]

    # SOLUTION 3: Iterate backwards (for index-based removal)
    lst = [1, 2, 3, 4, 5]
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] % 2 == 0:
            lst.pop(i)
    print(f"Solution 3: {lst}")  # [1, 3, 5]


def pitfall_assignment_vs_copy():
    """Assignment creates reference, not copy."""

    # PITFALL: Assignment doesn't create copy
    original = [1, 2, 3]
    reference = original  # Just another name for same object
    reference.append(4)
    print(f"Original: {original}")  # [1, 2, 3, 4] - modified!
    print(f"Same object: {original is reference}")  # True

    # SOLUTION: Explicitly copy
    original = [1, 2, 3]
    copy_list = original.copy()  # or original[:] or list(original)
    copy_list.append(4)
    print(f"Original: {original}")  # [1, 2, 3]
    print(f"Copy: {copy_list}")     # [1, 2, 3, 4]
    print(f"Different objects: {original is not copy_list}")  # True


# ============================================================================
# 6. MEMORY IMPLICATIONS
# ============================================================================

def memory_comparison():
    """Compare memory usage of in-place vs out-of-place."""
    import sys

    # IN-PLACE: More memory efficient
    lst = list(range(1000000))
    size_before = sys.getsizeof(lst)
    lst.reverse()  # In-place, no new allocation
    size_after = sys.getsizeof(lst)
    print(f"In-place reverse: {size_before} -> {size_after} bytes")

    # OUT-OF-PLACE: Creates copy
    lst = list(range(1000000))
    size_original = sys.getsizeof(lst)
    reversed_lst = lst[::-1]  # Creates new list
    size_new = sys.getsizeof(reversed_lst)
    total = size_original + size_new
    print(f"Out-of-place reverse: original={size_original}, new={size_new}, total={total}")

    # For large data: in-place can be 2x more memory efficient


def when_to_use_each():
    """Guidelines for choosing in-place vs out-of-place."""

    print("""
    USE IN-PLACE MODIFICATION WHEN:
    - Working with large data structures (memory efficiency)
    - You don't need to preserve the original
    - You're sure no other code references the object
    - Performance is critical

    USE OUT-OF-PLACE MODIFICATION WHEN:
    - You need to preserve the original
    - Working with function parameters (safer)
    - Multiple references exist to the object
    - Code clarity is more important than performance
    - Working with immutable types (no choice!)
    - In functional programming style
    """)


# ============================================================================
# 7. BEST PRACTICES
# ============================================================================

def best_practices():
    """Best practices for handling mutability."""

    print("""
    BEST PRACTICES:

    1. DEFAULT TO IMMUTABILITY
       - Use tuples instead of lists when data won't change
       - Use frozenset instead of set for immutable sets
       - Consider namedtuples or dataclasses with frozen=True

    2. EXPLICIT IS BETTER THAN IMPLICIT
       - If you need to modify, use clear in-place methods (append, extend)
       - If you need to preserve, explicitly copy (copy(), [:], deepcopy())
       - Don't rely on subtle behavior

    3. FUNCTION DESIGN
       - Document whether function modifies arguments
       - Prefer returning new objects (functional style)
       - Avoid mutable default arguments
       - Use type hints to clarify expectations

    4. DEFENSIVE COPYING
       - Copy mutable arguments if you'll modify them
       - Copy mutable return values if internal state shouldn't be exposed

    5. USE APPROPRIATE DATA STRUCTURES
       - For append-heavy: list (in-place append)
       - For immutable sequence: tuple
       - For membership testing: set
       - For ordered immutable: tuple
       - For ordered mutable: list

    6. INTERVIEW TIPS
       - Clarify if in-place modification is required
       - Mention space complexity implications
       - State if you're preserving original or modifying
       - Know the difference between sort() and sorted()
    """)


def interview_examples():
    """Common interview scenarios."""

    # Example 1: Reverse array in-place (LeetCode style)
    def reverse_in_place(arr):
        """O(n) time, O(1) space - in-place"""
        left, right = 0, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        # Note: modifies original, returns None by convention

    arr = [1, 2, 3, 4, 5]
    reverse_in_place(arr)
    print(f"Reversed in-place: {arr}")  # [5, 4, 3, 2, 1]

    # Example 2: Reverse array out-of-place
    def reverse_new(arr):
        """O(n) time, O(n) space - creates new array"""
        return arr[::-1]

    arr = [1, 2, 3, 4, 5]
    result = reverse_new(arr)
    print(f"Original: {arr}, New: {result}")  # [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]

    # Example 3: Remove duplicates from sorted array (LeetCode 26)
    def remove_duplicates_in_place(nums):
        """Modify nums in-place, return new length."""
        if not nums:
            return 0

        write_idx = 1
        for read_idx in range(1, len(nums)):
            if nums[read_idx] != nums[read_idx - 1]:
                nums[write_idx] = nums[read_idx]
                write_idx += 1

        return write_idx

    nums = [1, 1, 2, 2, 3, 4, 4]
    length = remove_duplicates_in_place(nums)
    print(f"Modified array: {nums[:length]}")  # [1, 2, 3, 4]


# ============================================================================
# SUMMARY CHEAT SHEET
# ============================================================================

SUMMARY = """
╔════════════════════════════════════════════════════════════════════════╗
║                  IN-PLACE vs OUT-OF-PLACE QUICK REFERENCE              ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  IN-PLACE (Modifies Original)           OUT-OF-PLACE (Creates New)    ║
║  ────────────────────────────           ──────────────────────────    ║
║  list.append(x)                          list + [x]                   ║
║  list.extend(other)                      list + other                 ║
║  list.insert(i, x)                       list[:i] + [x] + list[i:]    ║
║  list.remove(x)                          [y for y in list if y != x]  ║
║  list.pop()                              list[:-1]                    ║
║  list.reverse()                          list[::-1] or reversed(list) ║
║  list.sort()                             sorted(list)                 ║
║  list[i] = x                             list[:i] + [x] + list[i+1:]  ║
║  dict[key] = val                         {**dict, key: val}           ║
║  dict.update(other)                      {**dict, **other}            ║
║  set.add(x)                              set | {x}                    ║
║  set.update(other)                       set | other                  ║
║                                                                        ║
║  Returns: Usually None                   Returns: New object          ║
║  Memory: O(1) extra                      Memory: O(n) extra           ║
║  Original: Modified                      Original: Preserved          ║
║                                                                        ║
╠════════════════════════════════════════════════════════════════════════╣
║  IMMUTABLE TYPES         │  MUTABLE TYPES                             ║
║  ────────────────        │  ──────────────                            ║
║  int, float, bool        │  list                                      ║
║  str                     │  dict                                      ║
║  tuple                   │  set                                       ║
║  frozenset               │  bytearray                                 ║
║  bytes                   │  custom objects                            ║
║                          │                                            ║
║  Cannot modify in-place  │  Can modify in-place                       ║
║  All operations create   │  Choice of in-place                        ║
║  new objects             │  or out-of-place                           ║
╚════════════════════════════════════════════════════════════════════════╝

KEY RULES:
1. Immutable types ALWAYS use external modification (create new objects)
2. Mutable types can use EITHER in-place OR external modification
3. In-place methods typically return None
4. Out-of-place operations return new objects
5. Function parameters: mutable objects can be modified by the function!
6. Assignment (=) never copies, use .copy() or [:] explicitly
7. Shallow copy vs deep copy matters for nested structures
"""

if __name__ == "__main__":
    print("=" * 80)
    print("PYTHON IN-PLACE VS EXTERNAL MODIFICATION GUIDE")
    print("=" * 80)

    print("\n1. Demonstrating Immutability")
    demonstrate_immutability()

    print("\n2. Demonstrating Mutability")
    demonstrate_mutability()

    print("\n3. In-place List Operations")
    in_place_list_operations()

    print("\n4. Out-of-place Operations")
    out_of_place_operations()

    print("\n5. Function Parameter Examples")
    immutable_parameter_example()
    print()
    mutable_parameter_example()

    print("\n6. Memory Comparison")
    memory_comparison()

    print("\n7. Interview Examples")
    interview_examples()

    print("\n" + SUMMARY)
