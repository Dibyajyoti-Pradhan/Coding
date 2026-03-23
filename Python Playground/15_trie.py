"""
TRIE (Prefix Tree) - Complete Guide
====================================

CORE CONCEPTS:
--------------
1. Tree-like data structure for storing strings
2. Each node represents a character
3. Root represents empty string
4. Edges represent characters
5. Special flag marks end of word

OPERATIONS:
-----------
- insert(word): Add word to trie - O(L) where L is word length
- search(word): Check if exact word exists - O(L)
- startsWith(prefix): Check if any word starts with prefix - O(L)

STRUCTURE:
----------
Each TrieNode has:
- children: dict/array of child nodes (26 letters or hashmap)
- is_end: boolean flag marking end of word

WHEN TO USE:
------------
- Autocomplete/search suggestions
- Spell checker
- Word games (Boggle, Scrabble)
- IP routing (longest prefix match)
- Pattern matching with wildcards

TRICKY PARTS:
-------------
1. Need to mark end of word (not just existence of path)
2. DFS for finding all words with prefix
3. Memory intensive (26 pointers per node if using array)
4. Use dict for children if sparse (few words)
"""

from typing import List, Optional, Set
from collections import defaultdict


# ============================================================================
# BASIC TRIE IMPLEMENTATION
# ============================================================================

class TrieNode:
    """
    Node in a Trie.

    Each node stores:
    - children: dictionary mapping character to child TrieNode
    - is_end: boolean indicating if this node marks end of a word
    """
    def __init__(self):
        self.children = {}  # char -> TrieNode
        self.is_end = False


class Trie:
    """
    PROBLEM: Implement Trie (Prefix Tree) - LeetCode 208

    A trie (pronounced as "try") or prefix tree is a tree data structure used
    to efficiently store and retrieve keys in a dataset of strings.

    Implement the Trie class:
    - Trie() Initializes the trie object.
    - void insert(String word) Inserts the string word into the trie.
    - boolean search(String word) Returns true if the string word is in the trie.
    - boolean startsWith(String prefix) Returns true if there is a previously
      inserted string word that has the prefix prefix.

    Example 1:
        Input:
            ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
            [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
        Output:
            [null, null, true, false, true, null, true]
        Explanation:
            Trie trie = new Trie();
            trie.insert("apple");
            trie.search("apple");   // return True
            trie.search("app");     // return False
            trie.startsWith("app"); // return True
            trie.insert("app");
            trie.search("app");     // return True

    Constraints:
        - 1 <= word.length, prefix.length <= 2000
        - word and prefix consist only of lowercase English letters.
        - At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.

    Time: O(L) for all operations where L is word/prefix length
    Space: O(N * L) where N is number of words
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word into the trie."""
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True

    def search(self, word: str) -> bool:
        """Returns True if the word is in the trie."""
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        """Returns True if there is any word in the trie that starts with the given prefix."""
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True


# ============================================================================
# PROBLEM 1: DESIGN ADD AND SEARCH WORDS DATA STRUCTURE
# ============================================================================

class WordDictionary:
    """
    PROBLEM: Design Add and Search Words Data Structure (LeetCode 211)

    Design a data structure that supports adding new words and finding if a
    string matches any previously added string.

    Implement the WordDictionary class:
    - WordDictionary() Initializes the object.
    - void addWord(word) Adds word to the data structure.
    - bool search(word) Returns true if there is any string in the data structure
      that matches word or false otherwise. word may contain dots '.' where dots
      can be matched with any letter.

    Example:
        Input:
            ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
            [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
        Output:
            [null,null,null,null,false,true,true,true]
        Explanation:
            WordDictionary wordDictionary = new WordDictionary();
            wordDictionary.addWord("bad");
            wordDictionary.addWord("dad");
            wordDictionary.addWord("mad");
            wordDictionary.search("pad"); // return False
            wordDictionary.search("bad"); // return True
            wordDictionary.search(".ad"); // return True
            wordDictionary.search("b.."); // return True

    Constraints:
        - 1 <= word.length <= 25
        - word in addWord consists of lowercase English letters.
        - word in search consist of '.' or lowercase English letters.
        - There will be at most 2 dots in word for search queries.
        - At most 10^4 calls will be made to addWord and search.

    Time: addWord O(L), search O(L) best case, O(26^L) worst with wildcards
    Space: O(N * L)
    """

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        """Search with wildcard support (. matches any letter)."""
        def dfs(index: int, node: TrieNode) -> bool:
            if index == len(word):
                return node.is_end

            char = word[index]

            if char == '.':
                # Try all possible children
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(index + 1, node.children[char])

        return dfs(0, self.root)


# ============================================================================
# PROBLEM 2: WORD SEARCH II
# ============================================================================

def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    """
    PROBLEM: Word Search II (LeetCode 212)

    Given an m x n board of characters and a list of strings words, return all
    words on the board.

    Each word must be constructed from letters of sequentially adjacent cells,
    where adjacent cells are horizontally or vertically neighboring. The same
    letter cell may not be used more than once in a word.

    Example 1:
        Input: board = [["o","a","a","n"],
                        ["e","t","a","e"],
                        ["i","h","k","r"],
                        ["i","f","l","v"]]
               words = ["oath","pea","eat","rain"]
        Output: ["eat","oath"]

    Example 2:
        Input: board = [["a","b"],
                        ["c","d"]]
               words = ["abcb"]
        Output: []

    Constraints:
        - m == board.length
        - n == board[i].length
        - 1 <= m, n <= 12
        - board[i][j] is a lowercase English letter.
        - 1 <= words.length <= 3 * 10^4
        - 1 <= words[i].length <= 10
        - words[i] consists of lowercase English letters.
        - All the strings of words are unique.

    Time: O(M * N * 4^L) where L is max word length
    Space: O(N * L) for trie
    """
    # Build trie from words
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    m, n = len(board), len(board[0])
    result = set()

    def backtrack(i: int, j: int, node: TrieNode, path: str):
        """DFS to find words in board."""
        if node.is_end:
            result.add(path)
            # Don't return - might have longer words with this prefix

        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if board[i][j] not in node.children:
            return

        char = board[i][j]
        board[i][j] = '#'  # Mark visited

        # Explore 4 directions
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            backtrack(i+di, j+dj, node.children[char], path + char)

        board[i][j] = char  # Restore

    # Try starting from each cell
    for i in range(m):
        for j in range(n):
            if board[i][j] in root.children:
                backtrack(i, j, root, '')

    return list(result)


# ============================================================================
# PROBLEM 3: REPLACE WORDS
# ============================================================================

def replace_words(dictionary: List[str], sentence: str) -> str:
    """
    PROBLEM: Replace Words (LeetCode 648)

    In English, we have a concept called root, which can be followed by some
    other word to form another longer word - let's call this word successor.
    For example, when the root "an" is followed by the successor word "other",
    we can form a new word "another".

    Given a dictionary consisting of many roots and a sentence consisting of
    words separated by spaces, replace all the successors in the sentence with
    the root forming it. If a successor can be replaced by more than one root,
    replace it with the root that has the shortest length.

    Return the sentence after the replacement.

    Example 1:
        Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
        Output: "the cat was rat by the bat"

    Example 2:
        Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
        Output: "a a b c"

    Constraints:
        - 1 <= dictionary.length <= 1000
        - 1 <= dictionary[i].length <= 100
        - dictionary[i] consists of only lowercase letters.
        - 1 <= sentence.length <= 10^6
        - sentence consists of only lowercase letters and spaces.

    Time: O(D + S) where D is total chars in dictionary, S is sentence length
    Space: O(D)
    """
    # Build trie
    root = TrieNode()
    for word in dictionary:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def find_root(word: str) -> str:
        """Find shortest root for word, or return word if no root found."""
        node = root
        for i, char in enumerate(word):
            if char not in node.children:
                return word
            node = node.children[char]
            if node.is_end:
                return word[:i+1]  # Found root
        return word

    words = sentence.split()
    return ' '.join(find_root(word) for word in words)


# ============================================================================
# PROBLEM 4: LONGEST WORD IN DICTIONARY
# ============================================================================

def longest_word(words: List[str]) -> str:
    """
    PROBLEM: Longest Word in Dictionary (LeetCode 720)

    Given an array of strings words representing an English Dictionary, return
    the longest word in words that can be built one character at a time by other
    words in words.

    If there is more than one possible answer, return the longest word with the
    smallest lexicographical order. If there is no answer, return the empty string.

    Example 1:
        Input: words = ["w","wo","wor","worl","world"]
        Output: "world"
        Explanation: "world" can be built one character at a time by "w", "wo", "wor", and "worl".

    Example 2:
        Input: words = ["a","banana","app","appl","ap","apply","apple"]
        Output: "apple"
        Explanation: Both "apply" and "apple" can be built from other words.
        "apple" is lexicographically smaller than "apply".

    Constraints:
        - 1 <= words.length <= 1000
        - 1 <= words[i].length <= 30
        - words[i] consists of lowercase English letters.

    Time: O(N * L) where N is number of words, L is max length
    Space: O(N * L)
    """
    # Build trie
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def can_build(word: str) -> bool:
        """Check if word can be built one char at a time."""
        node = root
        for char in word[:-1]:  # Check all prefixes exist
            if char not in node.children:
                return False
            node = node.children[char]
            if not node.is_end:
                return False
        return True

    valid_words = [w for w in words if can_build(w)]

    if not valid_words:
        return ""

    # Return longest, then lexicographically smallest
    return max(valid_words, key=lambda w: (len(w), -ord(w[0])))


# ============================================================================
# PROBLEM 5: IMPLEMENT MAGIC DICTIONARY
# ============================================================================

class MagicDictionary:
    """
    PROBLEM: Implement Magic Dictionary (LeetCode 676)

    Design a data structure that is initialized with a list of different words.
    Provided a string, you should determine if you can change exactly one character
    in this string to match any word in the data structure.

    Implement the MagicDictionary class:
    - MagicDictionary() Initializes the object.
    - void buildDict(String[] dictionary) Sets the data structure with an array
      of distinct strings dictionary.
    - bool search(String searchWord) Returns true if you can change exactly one
      character in searchWord to match any string in the data structure, otherwise
      returns false.

    Example 1:
        Input:
            ["MagicDictionary", "buildDict", "search", "search", "search", "search"]
            [[], [["hello","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
        Output:
            [null, null, false, true, false, false]
        Explanation:
            MagicDictionary magicDictionary = new MagicDictionary();
            magicDictionary.buildDict(["hello", "leetcode"]);
            magicDictionary.search("hello"); // return False
            magicDictionary.search("hhllo"); // return True (change 'e' to 'h')
            magicDictionary.search("hell"); // return False
            magicDictionary.search("leetcoded"); // return False

    Constraints:
        - 1 <= dictionary.length <= 100
        - 1 <= dictionary[i].length <= 100
        - dictionary[i] consists of only lower-case English letters.
        - All the strings in dictionary are distinct.
        - 1 <= searchWord.length <= 100
        - searchWord consists of only lower-case English letters.

    Time: buildDict O(N*L), search O(L*26)
    Space: O(N*L)
    """

    def __init__(self):
        self.root = TrieNode()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True

    def search(self, searchWord: str) -> bool:
        """Search with exactly one character different."""
        def dfs(index: int, node: TrieNode, changed: bool) -> bool:
            if index == len(searchWord):
                return node.is_end and changed

            char = searchWord[index]

            # Try matching current character
            if char in node.children:
                if dfs(index + 1, node.children[char], changed):
                    return True

            # If haven't changed yet, try all other characters
            if not changed:
                for c, child in node.children.items():
                    if c != char:
                        if dfs(index + 1, child, True):
                            return True

            return False

        return dfs(0, self.root, False)


# ============================================================================
# ADVANCED: TRIE WITH AUTOCOMPLETE
# ============================================================================

class AutocompleteSystem:
    """
    PROBLEM: Design Search Autocomplete System (LeetCode 642)

    Design a search autocomplete system for a search engine. Users may input a
    sentence (at least one word and end with a special character '#').

    You are given a string array sentences and an integer array times both of
    length n where sentences[i] is a previously typed sentence and times[i] is
    the corresponding number of times the sentence was typed.

    For each input character except '#', return the top 3 historical hot sentences
    that have the same prefix as the part of the sentence already typed.

    Constraints:
        - n == sentences.length
        - n == times.length
        - 1 <= n <= 100
        - 1 <= sentences[i].length <= 100
        - 1 <= times[i] <= 50
        - c is a lowercase English letter, a hash '#', or space ' '.

    Time: O(N*L) for initialization, O(L + k*log k) per input where k is matching sentences
    Space: O(N*L)
    """

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.keyword = ""
        self.sentence_count = defaultdict(int)

        # Build trie with sentence counts
        for sentence, time in zip(sentences, times):
            self.sentence_count[sentence] = time
            self._add_to_trie(sentence)

    def _add_to_trie(self, sentence: str):
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def input(self, c: str) -> List[str]:
        if c == '#':
            # End of sentence - add to trie
            self.sentence_count[self.keyword] += 1
            self._add_to_trie(self.keyword)
            self.keyword = ""
            return []

        self.keyword += c

        # Find all sentences with current prefix
        matches = []
        node = self.root

        # Navigate to end of prefix
        for char in self.keyword:
            if char not in node.children:
                return []
            node = node.children[char]

        # DFS to find all sentences from this node
        def dfs(node: TrieNode, path: str):
            if node.is_end:
                sentence = self.keyword + path
                matches.append((self.sentence_count[sentence], sentence))

            for char, child in node.children.items():
                dfs(child, path + char)

        dfs(node, "")

        # Sort by count (desc), then lexicographically
        matches.sort(key=lambda x: (-x[0], x[1]))

        return [sentence for _, sentence in matches[:3]]


# ============================================================================
# PRACTICE PROBLEMS
# ============================================================================

"""
EASY:
- Implement Trie (208)
- Longest Word in Dictionary (720)

MEDIUM:
- Design Add and Search Words (211)
- Replace Words (648)
- Implement Magic Dictionary (676)
- Map Sum Pairs (677)
- Concatenated Words (472)

HARD:
- Word Search II (212)
- Design Search Autocomplete System (642)
- Stream of Characters (1032)
"""


if __name__ == "__main__":
    print("="*70)
    print("TRIE - Test Examples")
    print("="*70)

    # Test 1: Basic Trie
    print("\n1. Basic Trie Operations:")
    trie = Trie()
    trie.insert("apple")
    print(f"   search('apple'): {trie.search('apple')}")      # True
    print(f"   search('app'): {trie.search('app')}")          # False
    print(f"   startsWith('app'): {trie.startsWith('app')}")  # True
    trie.insert("app")
    print(f"   After insert('app'), search('app'): {trie.search('app')}")  # True

    # Test 2: Word Dictionary with wildcards
    print("\n2. Word Dictionary (with wildcards):")
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    print(f"   search('pad'): {wd.search('pad')}")  # False
    print(f"   search('.ad'): {wd.search('.ad')}")  # True
    print(f"   search('b..'): {wd.search('b..')}")  # True

    # Test 3: Replace Words
    print("\n3. Replace Words:")
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    print(f"   Input: {sentence}")
    print(f"   Output: {replace_words(dictionary, sentence)}")

    print("\n" + "="*70)
    print("Trie is perfect for prefix-based operations!")
    print("="*70)
