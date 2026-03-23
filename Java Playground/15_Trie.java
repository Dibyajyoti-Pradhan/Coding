import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;

/**
 * Trie (Prefix Tree) problems and implementations.
 *
 * <p>A Trie is a tree-like data structure that efficiently stores and retrieves strings by
 * their prefixes. Each node branches represent characters, allowing for fast prefix-based
 * queries.
 *
 * <p><b>Key Properties:</b>
 * <ul>
 *   <li><b>Time Complexity:</b> O(L) for insert, search, and prefix queries where L is
 *       string length.
 *   <li><b>Space Complexity:</b> O(n·L) for n strings of average length L.
 *   <li><b>Children Storage:</b> Can use TrieNode[26] for English letters (fixed) or
 *       HashMap<Character, TrieNode> (flexible for Unicode).
 *   <li><b>Efficiency:</b> More efficient than HashSet for prefix matching.
 * </ul>
 *
 * <p><b>Common Use Cases:</b>
 * <ul>
 *   <li>Autocomplete systems and search suggestions
 *   <li>Spell checking and word validation
 *   <li>Longest common prefix queries
 *   <li>IP routing tables
 *   <li>Pattern matching with wildcards
 *   <li>Word games (Scrabble, Boggle)
 * </ul>
 */
public class TrieProblems {

  private static final int ALPHABET_SIZE = 26;
  private static final char WILDCARD = '.';
  private static final char VISITED_MARKER = '#';
  private static final int TOP_K_RESULTS = 3;

  /**
   * TrieNode represents a single node in the Trie structure.
   *
   * <p>Stores children nodes and metadata about words ending at this node.
   */
  public static class TrieNode {
    /** Children nodes for each lowercase letter a-z. */
    public TrieNode[] children = new TrieNode[ALPHABET_SIZE];

    /** Marks if this node is the end of a valid word. */
    public boolean isEndOfWord = false;

    /** Stores the full word for optimization in Word Search II. */
    public String word = null;

    /**
     * Gets the child node for a character.
     *
     * @param c the character (must be lowercase a-z)
     * @return the child TrieNode or null if not present
     */
    public TrieNode getChild(char c) {
      if (c < 'a' || c > 'z') {
        return null;
      }
      return children[c - 'a'];
    }

    /**
     * Sets the child node for a character.
     *
     * @param c the character (lowercase a-z)
     * @param node the TrieNode to set
     */
    public void setChild(char c, TrieNode node) {
      if (c >= 'a' && c <= 'z') {
        children[c - 'a'] = node;
      }
    }
  }

  /**
   * Basic Trie implementation supporting insert, search, and prefix matching.
   *
   * <p><b>LeetCode 208 (Medium)</b>
   */
  public static class Trie {
    private TrieNode root;

    /**
     * Initializes an empty Trie.
     */
    public Trie() {
      this.root = new TrieNode();
    }

    /**
     * Inserts a word into the Trie.
     *
     * <p><b>Time:</b> O(L) where L is word length <b>Space:</b> O(L) in worst case
     *
     * @param word the word to insert
     * @throws IllegalArgumentException if word is null or empty
     */
    public void insert(String word) {
      if (word == null || word.isEmpty()) {
        throw new IllegalArgumentException("Word cannot be null or empty");
      }

      TrieNode node = root;
      for (char c : word.toCharArray()) {
        if (node.getChild(c) == null) {
          node.setChild(c, new TrieNode());
        }
        node = node.getChild(c);
      }
      node.isEndOfWord = true;
    }

    /**
     * Searches for an exact word in the Trie.
     *
     * <p><b>Time:</b> O(L) <b>Space:</b> O(1)
     *
     * @param word the word to search
     * @return true if word exists in Trie
     */
    public boolean search(String word) {
      TrieNode node = findNode(word);
      return node != null && node.isEndOfWord;
    }

    /**
     * Checks if any word in Trie starts with the given prefix.
     *
     * <p><b>Time:</b> O(L) <b>Space:</b> O(1)
     *
     * @param prefix the prefix to search
     * @return true if prefix exists in Trie
     */
    public boolean startsWith(String prefix) {
      return findNode(prefix) != null;
    }

    /**
     * Helper to find the TrieNode corresponding to a string.
     *
     * @param s the string to find
     * @return the TrieNode at end of s, or null if not found
     */
    private TrieNode findNode(String s) {
      if (s == null || s.isEmpty()) {
        return root;
      }

      TrieNode node = root;
      for (char c : s.toCharArray()) {
        node = node.getChild(c);
        if (node == null) {
          return null;
        }
      }
      return node;
    }
  }

  /**
   * Word Dictionary with wildcard support (. matches any character).
   *
   * <p><b>LeetCode 211 (Medium)</b>
   */
  public static class WordDictionary {
    private TrieNode root;

    /**
     * Initializes the word dictionary.
     */
    public WordDictionary() {
      this.root = new TrieNode();
    }

    /**
     * Adds a word to the dictionary.
     *
     * <p><b>Time:</b> O(L) <b>Space:</b> O(L)
     *
     * @param word the word to add
     */
    public void addWord(String word) {
      if (word == null || word.isEmpty()) {
        throw new IllegalArgumentException("Word cannot be null or empty");
      }

      TrieNode node = root;
      for (char c : word.toCharArray()) {
        if (node.getChild(c) == null) {
          node.setChild(c, new TrieNode());
        }
        node = node.getChild(c);
      }
      node.isEndOfWord = true;
    }

    /**
     * Searches for a word supporting '.' wildcard matching.
     *
     * <p>The '.' character matches any single character.
     *
     * <p><b>Time:</b> O(n·26^L) worst case <b>Space:</b> O(L) recursion depth
     *
     * @param word the pattern to search (may contain '.')
     * @return true if pattern matches a word in dictionary
     */
    public boolean search(String word) {
      if (word == null || word.isEmpty()) {
        return false;
      }
      return dfsSearch(word, 0, root);
    }

    /**
     * DFS helper for wildcard matching.
     *
     * @param word the word pattern
     * @param index current position in word
     * @param node current TrieNode
     * @return true if remaining word matches remaining Trie
     */
    private boolean dfsSearch(String word, int index, TrieNode node) {
      if (index == word.length()) {
        return node.isEndOfWord;
      }

      char c = word.charAt(index);
      if (c == WILDCARD) {
        // Try all 26 letters
        for (int i = 0; i < ALPHABET_SIZE; i++) {
          if (node.children[i] != null && dfsSearch(word, index + 1, node.children[i])) {
            return true;
          }
        }
        return false;
      } else {
        // Match exact character
        if (node.getChild(c) == null) {
          return false;
        }
        return dfsSearch(word, index + 1, node.getChild(c));
      }
    }
  }

  /**
   * Finds all words from a dictionary on a board using DFS and Trie optimization.
   *
   * <p><b>LeetCode 212 (Hard)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * board = [['o','a','a'],
   *          ['e','t','a'],
   *          ['t','r','ou']]
   * words = ["oath","pea","eat","rain"]
   * Output: ["eat","oath"]
   * </pre>
   *
   * <p><b>Constraints:</b> m, n ≤ 12, words.length ≤ 3, word length ≤ 10
   *
   * <p><b>Time:</b> O(m·n·4^L) where L is max word length <b>Space:</b> O(n·k) for Trie
   *
   * <p><b>Tricky:</b> Build Trie from words, DFS on board matching Trie paths. Mark board
   * cells visited with '#'. Set node.word = null after finding to avoid duplicates.
   *
   * @param board 2D character grid
   * @param words list of words to find
   * @return list of words found in board
   */
  public static List<String> findWords(char[][] board, String[] words) {
    List<String> result = new ArrayList<>();

    if (board == null || board.length == 0 || words == null || words.length == 0) {
      return result;
    }

    // Build Trie
    Trie trie = new Trie();
    TrieNode root = new TrieNode();
    for (String word : words) {
      TrieNode node = root;
      for (char c : word.toCharArray()) {
        if (node.getChild(c) == null) {
          node.setChild(c, new TrieNode());
        }
        node = node.getChild(c);
      }
      node.isEndOfWord = true;
      node.word = word;
    }

    int m = board.length;
    int n = board[0].length;

    // DFS from each cell
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        dfsWords(board, i, j, root, result, m, n);
      }
    }

    return result;
  }

  /**
   * DFS helper to find words on board.
   *
   * @param board the game board
   * @param row current row
   * @param col current column
   * @param node current Trie node
   * @param result list to collect found words
   * @param m number of rows
   * @param n number of columns
   */
  private static void dfsWords(
      char[][] board, int row, int col, TrieNode node, List<String> result, int m, int n) {

    char c = board[row][col];
    if (c == VISITED_MARKER) {
      return;
    }

    TrieNode child = node.getChild(c);
    if (child == null) {
      return;
    }

    if (child.word != null) {
      result.add(child.word);
      child.word = null; // Mark as found to avoid duplicates
    }

    // Mark as visited
    board[row][col] = VISITED_MARKER;

    int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    for (int[] dir : directions) {
      int newRow = row + dir[0];
      int newCol = col + dir[1];
      if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n) {
        dfsWords(board, newRow, newCol, child, result, m, n);
      }
    }

    // Restore cell
    board[row][col] = c;
  }

  /**
   * Replaces words in a sentence with their dictionary roots.
   *
   * <p><b>LeetCode 648 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * dictionary = ["cat","bat","rat"]
   * sentence = "the cattle was rattled by the bat"
   * Output: "the cat was rat by the bat"
   * </pre>
   *
   * <p><b>Constraints:</b> dictionary.length ≤ 1000, sentence.length ≤ 2000
   *
   * <p><b>Time:</b> O(n·L) where n = sentence length, L = max word length
   * <b>Space:</b> O(d·L) for Trie from dictionary
   *
   * <p><b>Tricky:</b> Build Trie from dictionary, for each word in sentence find shortest
   * prefix that exists in dictionary.
   *
   * @param dictionary list of word roots
   * @param sentence input sentence
   * @return sentence with words replaced by roots
   */
  public static String replaceWords(List<String> dictionary, String sentence) {
    if (sentence == null || sentence.isEmpty() || dictionary == null
        || dictionary.isEmpty()) {
      return sentence;
    }

    // Build Trie
    TrieNode root = new TrieNode();
    for (String root_word : dictionary) {
      TrieNode node = root;
      for (char c : root_word.toCharArray()) {
        if (node.getChild(c) == null) {
          node.setChild(c, new TrieNode());
        }
        node = node.getChild(c);
      }
      node.isEndOfWord = true;
    }

    String[] words = sentence.split(" ");
    StringBuilder result = new StringBuilder();

    for (int i = 0; i < words.length; i++) {
      String word = words[i];
      String replacement = findShortestRoot(word, root);
      result.append(replacement);
      if (i < words.length - 1) {
        result.append(" ");
      }
    }

    return result.toString();
  }

  /**
   * Finds the shortest root of a word in the Trie.
   *
   * @param word the word to find root for
   * @param root the Trie root
   * @return shortest root if exists, otherwise the original word
   */
  private static String findShortestRoot(String word, TrieNode root) {
    TrieNode node = root;
    for (int i = 0; i < word.length(); i++) {
      char c = word.charAt(i);
      if (node.getChild(c) == null) {
        return word;
      }
      node = node.getChild(c);
      if (node.isEndOfWord) {
        return word.substring(0, i + 1);
      }
    }
    return word;
  }

  /**
   * Finds the longest word in the list that is built from other words in the list.
   *
   * <p><b>LeetCode 720 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * words = ["w","wo","wor","worl", "world"]
   * Output: "world"
   * </pre>
   *
   * <p><b>Constraints:</b> 1 ≤ words.length ≤ 1000, 1 ≤ word length ≤ 30
   *
   * <p><b>Time:</b> O(n·L^2) <b>Space:</b> O(n·L)
   *
   * <p><b>Tricky:</b> Sort words by length, use Trie to check if all prefixes of a word
   * exist in previous words.
   *
   * @param words array of words
   * @return longest word buildable from others, lexicographically smallest if tie
   */
  public static String longestWord(String[] words) {
    if (words == null || words.length == 0) {
      return "";
    }

    // Sort by length, then lexicographically
    java.util.Arrays.sort(words, (a, b) -> {
      if (a.length() != b.length()) {
        return Integer.compare(a.length(), b.length());
      }
      return a.compareTo(b);
    });

    TrieNode root = new TrieNode();
    String result = "";

    for (String word : words) {
      // Check if all prefixes exist
      TrieNode node = root;
      boolean canBuild = true;
      for (char c : word.toCharArray()) {
        if (node.getChild(c) == null || !node.getChild(c).isEndOfWord) {
          canBuild = false;
          break;
        }
        node = node.getChild(c);
      }

      if (canBuild) {
        result = word;
      }

      // Add word to Trie
      node = root;
      for (char c : word.toCharArray()) {
        if (node.getChild(c) == null) {
          node.setChild(c, new TrieNode());
        }
        node = node.getChild(c);
      }
      node.isEndOfWord = true;
    }

    return result;
  }

  /**
   * Magic Dictionary supporting add and search with exactly 1 character difference.
   *
   * <p><b>LeetCode 676 (Medium)</b>
   */
  public static class MagicDictionary {
    private TrieNode root;

    /**
     * Initializes the magic dictionary.
     */
    public MagicDictionary() {
      this.root = new TrieNode();
    }

    /**
     * Builds the dictionary from a list of words.
     *
     * <p><b>Time:</b> O(n·L) where n = words.length <b>Space:</b> O(n·L)
     *
     * @param dictionary array of words
     */
    public void buildDict(String[] dictionary) {
      if (dictionary == null) {
        return;
      }

      for (String word : dictionary) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
          if (node.getChild(c) == null) {
            node.setChild(c, new TrieNode());
          }
          node = node.getChild(c);
        }
        node.isEndOfWord = true;
      }
    }

    /**
     * Searches for a word that differs by exactly 1 character.
     *
     * <p><b>Time:</b> O(L·25) = O(L) <b>Space:</b> O(L)
     *
     * @param searchWord the word to search for
     * @return true if word with exactly 1 char difference exists
     */
    public boolean search(String searchWord) {
      if (searchWord == null || searchWord.isEmpty()) {
        return false;
      }

      return dfsMagic(searchWord, 0, root, 0);
    }

    /**
     * DFS to find word with exactly 1 character mismatch.
     *
     * @param word the search word
     * @param index current index
     * @param node current Trie node
     * @param mismatches number of character mismatches so far
     * @return true if found path with exactly 1 mismatch
     */
    private boolean dfsMagic(String word, int index, TrieNode node, int mismatches) {
      if (mismatches > 1) {
        return false;
      }

      if (index == word.length()) {
        return mismatches == 1 && node.isEndOfWord;
      }

      char c = word.charAt(index);
      for (int i = 0; i < ALPHABET_SIZE; i++) {
        char tryChar = (char) ('a' + i);
        if (node.children[i] != null) {
          int newMismatches = mismatches + (tryChar == c ? 0 : 1);
          if (dfsMagic(word, index + 1, node.children[i], newMismatches)) {
            return true;
          }
        }
      }

      return false;
    }
  }

  /**
   * Autocomplete system returning top 3 sentences by frequency then lexicographic order.
   *
   * <p><b>LeetCode 642 (Hard)</b>
   */
  public static class AutocompleteSystem {
    private TrieNode root;
    private TrieNode currentNode;
    private StringBuilder currentInput;
    private Map<String, Integer> sentenceFreq;

    /**
     * Initializes the autocomplete system.
     *
     * @param sentences initial list of sentences
     * @param times frequency of each sentence
     */
    public AutocompleteSystem(String[] sentences, int[] times) {
      this.root = new TrieNode();
      this.currentNode = root;
      this.currentInput = new StringBuilder();
      this.sentenceFreq = new HashMap<>();

      for (int i = 0; i < sentences.length; i++) {
        sentenceFreq.put(sentences[i], times[i]);
        insertSentence(sentences[i], times[i]);
      }
    }

    /**
     * Inserts a sentence into the Trie with frequency count.
     *
     * @param sentence the sentence
     * @param freq the frequency
     */
    private void insertSentence(String sentence, int freq) {
      TrieNode node = root;
      for (char c : sentence.toCharArray()) {
        if (node.getChild(c) == null) {
          node.setChild(c, new TrieNode());
        }
        node = node.getChild(c);
        if (node.word == null) {
          node.word = sentence;
        }
      }
      node.isEndOfWord = true;
    }

    /**
     * Processes an input character and returns top 3 autocomplete suggestions.
     *
     * <p><b>Time:</b> O(n + m log 3) where n = Trie traversal, m = results
     * <b>Space:</b> O(1) for top 3
     *
     * @param c input character ('#' marks end of sentence)
     * @return list of top 3 sentences, or empty list at sentence end
     */
    public List<String> input(char c) {
      if (c == '#') {
        String sentence = currentInput.toString();
        sentenceFreq.put(sentence, sentenceFreq.getOrDefault(sentence, 0) + 1);
        insertSentence(sentence, sentenceFreq.get(sentence));
        currentInput = new StringBuilder();
        currentNode = root;
        return new ArrayList<>();
      }

      currentInput.append(c);
      if (currentNode == null) {
        return new ArrayList<>();
      }

      currentNode = currentNode.getChild(c);
      if (currentNode == null) {
        return new ArrayList<>();
      }

      // Collect sentences from current Trie position
      List<String> suggestions = new ArrayList<>();
      collectSentences(currentNode, suggestions);

      // Sort by frequency (desc) then lexicographically, take top 3
      PriorityQueue<String> pq =
          new PriorityQueue<>(
              (a, b) -> {
                int freqCmp = sentenceFreq.get(b) - sentenceFreq.get(a);
                if (freqCmp != 0) {
                  return freqCmp;
                }
                return a.compareTo(b);
              });

      for (String s : suggestions) {
        pq.offer(s);
        if (pq.size() > TOP_K_RESULTS) {
          pq.poll();
        }
      }

      List<String> result = new ArrayList<>();
      while (!pq.isEmpty()) {
        result.add(0, pq.poll());
      }
      return result;
    }

    /**
     * Collects all sentences under a Trie node.
     *
     * @param node the Trie node
     * @param results list to collect sentences into
     */
    private void collectSentences(TrieNode node, List<String> results) {
      if (node == null) {
        return;
      }

      if (node.isEndOfWord && node.word != null) {
        results.add(node.word);
      }

      for (int i = 0; i < ALPHABET_SIZE; i++) {
        if (node.children[i] != null) {
          collectSentences(node.children[i], results);
        }
      }
    }
  }

  /**
   * Main method demonstrating all Trie problems.
   *
   * @param args unused
   */
  public static void main(String[] args) {
    System.out.println("=== Trie Problems ===\n");

    // Trie basic operations
    System.out.println("1. Basic Trie:");
    Trie trie = new Trie();
    trie.insert("apple");
    System.out.println("Search 'apple': " + trie.search("apple"));
    System.out.println("StartsWith 'app': " + trie.startsWith("app"));

    // WordDictionary with wildcards
    System.out.println("\n2. Word Dictionary (Wildcards):");
    WordDictionary dict = new WordDictionary();
    dict.addWord("bad");
    dict.addWord("dad");
    dict.addWord("mad");
    System.out.println("Search 'pad': " + dict.search("pad"));
    System.out.println("Search '.ad': " + dict.search(".ad"));

    // Longest word
    System.out.println("\n3. Longest Word:");
    String[] words = {"w", "wo", "wor", "worl", "world"};
    System.out.println("Longest word: " + longestWord(words));

    // Replace words
    System.out.println("\n4. Replace Words:");
    List<String> dictionary = List.of("cat", "bat", "rat");
    String sentence = "the cattle was rattled by the bat";
    System.out.println("Original: " + sentence);
    System.out.println("Replaced: " + replaceWords(dictionary, sentence));

    // Magic Dictionary
    System.out.println("\n5. Magic Dictionary:");
    MagicDictionary md = new MagicDictionary();
    md.buildDict(new String[]{"hello", "hallo", "leetcode"});
    System.out.println("Search 'hello' (1 diff): " + md.search("hello"));
    System.out.println("Search 'hallo' (1 diff): " + md.search("hallo"));

    // Autocomplete System
    System.out.println("\n6. Autocomplete System:");
    String[] sentences = {"hello world", "how are you", "hello"};
    int[] times = {3, 2, 5};
    AutocompleteSystem system = new AutocompleteSystem(sentences, times);
    System.out.println("Input 'h': " + system.input('h'));
    System.out.println("Input 'e': " + system.input('e'));
    System.out.println("Input 'l': " + system.input('l'));
  }
}
