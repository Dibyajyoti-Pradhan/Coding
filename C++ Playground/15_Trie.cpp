/// @file 15_Trie.cpp
/// @brief Trie data structure for efficient string search and matching.
///
/// `children[26]` array (O(1) access by char - 'a') faster than
/// unordered_map for lowercase; store `word` in end-node for Word Search II
/// (avoids path reconstruction); prune found words from trie during DFS to
/// prevent duplicates without extra set; `std::array<TrieNode*, 26>`
/// initialised to nullptr.
///
/// Time Complexity: O(m) per operation (m = word length)
/// Space Complexity: O(n * m) for n words of length m

#include <algorithm>
#include <array>
#include <iostream>
#include <string>
#include <string_view>
#include <vector>

namespace trie_playground {

/// @brief TrieNode structure with zero-initialised children.
struct TrieNode {
  std::array<TrieNode*, 26> children{};  ///< Zero-initialised to nullptr
  bool is_end{false};
  std::string word{};  ///< Non-empty only at end nodes
};

/// @brief LC 208: Trie class for exact string matching.
/// @details Insert, Search, StartsWith all O(m) where m = word length.
class Trie {
 public:
  Trie() noexcept : root_(new TrieNode()) {}

  /// @brief Insert word into trie.
  /// @param word String to insert (lowercase a-z).
  /// @return void
  /// @details Time: O(m), Space: O(m) for new path.
  void Insert(std::string_view word) noexcept {
    TrieNode* node = root_;
    for (char c : word) {
      int idx = c - 'a';
      if (!node->children[idx]) {
        node->children[idx] = new TrieNode();
      }
      node = node->children[idx];
    }
    node->is_end = true;
  }

  /// @brief Search for exact word match.
  /// @param word Word to search.
  /// @return true if word exists in trie.
  /// @details Time: O(m).
  [[nodiscard]] bool Search(std::string_view word) const noexcept {
    TrieNode* node = root_;
    for (char c : word) {
      int idx = c - 'a';
      if (!node->children[idx]) return false;
      node = node->children[idx];
    }
    return node->is_end;
  }

  /// @brief Check if any word starts with prefix.
  /// @param prefix Prefix to search.
  /// @return true if prefix exists.
  /// @details Time: O(m).
  [[nodiscard]] bool StartsWith(std::string_view prefix) const noexcept {
    TrieNode* node = root_;
    for (char c : prefix) {
      int idx = c - 'a';
      if (!node->children[idx]) return false;
      node = node->children[idx];
    }
    return true;
  }

 private:
  TrieNode* root_;
};

/// @brief LC 211: WordDictionary with wildcard matching.
/// @details Search with '.' wildcard (matches any letter).
class WordDictionary {
 public:
  WordDictionary() noexcept : root_(new TrieNode()) {}

  /// @brief Add word to dictionary.
  /// @param word String to add (lowercase a-z).
  /// @return void
  /// @details Time: O(m).
  void AddWord(std::string_view word) noexcept {
    TrieNode* node = root_;
    for (char c : word) {
      int idx = c - 'a';
      if (!node->children[idx]) {
        node->children[idx] = new TrieNode();
      }
      node = node->children[idx];
    }
    node->is_end = true;
  }

  /// @brief Search for word with '.' wildcard support.
  /// @param word Word pattern (a-z and '.').
  /// @return true if match exists.
  /// @details Time: O(26^m) worst case (all wildcards).
  /// Example: word="a.c" matches "abc", "adc".
  [[nodiscard]] bool Search(std::string_view word) const noexcept {
    return DfsSearch(root_, word, 0);
  }

 private:
  TrieNode* root_;

  /// @brief DFS helper for wildcard search.
  /// @param node Current trie node.
  /// @param word Pattern to match.
  /// @param idx Current index in word.
  /// @return true if word matches from this point.
  static bool DfsSearch(const TrieNode* node,
                        std::string_view word, int idx) noexcept {
    if (idx == static_cast<int>(word.size())) {
      return node->is_end;
    }
    char c = word[idx];
    if (c == '.') {
      for (int i = 0; i < 26; ++i) {
        if (node->children[i] && DfsSearch(node->children[i], word, idx + 1)) {
          return true;
        }
      }
      return false;
    } else {
      int c_idx = c - 'a';
      if (!node->children[c_idx]) return false;
      return DfsSearch(node->children[c_idx], word, idx + 1);
    }
  }
};

/// @brief Backtracking DFS for word search on board.
/// @param board 2D grid (modified in-place with '#' markers).
/// @param node Current trie node.
/// @param row Current row.
/// @param col Current column.
/// @param result Output vector of found words.
/// @param m Grid height.
/// @param n Grid width.
/// @return void
/// @details Prunes found words (sets is_end=false) to avoid duplicates.
static void Backtrack(std::vector<std::vector<char>>& board,
                      TrieNode* node, int row, int col,
                      std::vector<std::string>& result, int m,
                      int n) noexcept;

/// @brief LC 212: Find words in board using trie.
/// @param board 2D grid of characters.
/// @param words List of words to find.
/// @return Words found in board.
/// @details Example: board=[["o","a","b"],["r","t","a"],["t","a","r"]],
///          words=["oath","pea","eat","rain"] → ["eat","oath"].
/// @constraints Time: O(m*n*4^l), Space: O(sum of word lengths).
/// @note Tricky: Build trie, DFS with '#' marker, prune found words to avoid
///       duplicates.
[[nodiscard]] std::vector<std::string> FindWords(
    std::vector<std::vector<char>>& board,
    const std::vector<std::string>& words) noexcept {
  if (board.empty()) return {};
  TrieNode* root = new TrieNode();

  // Build trie with words stored in end nodes
  for (const auto& word : words) {
    TrieNode* node = root;
    for (char c : word) {
      int idx = c - 'a';
      if (!node->children[idx]) {
        node->children[idx] = new TrieNode();
      }
      node = node->children[idx];
    }
    node->is_end = true;
    node->word = word;
  }

  std::vector<std::string> result;
  int m = board.size(), n = board[0].size();

  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      Backtrack(board, root, i, j, result, m, n);
    }
  }

  return result;
}

/// @brief Backtracking DFS for word search on board (implementation).
static void Backtrack(std::vector<std::vector<char>>& board,
                      TrieNode* node, int row, int col,
                      std::vector<std::string>& result, int m,
                      int n) noexcept {
  char c_char = board[row][col];
  int c_idx = c_char - 'a';

  if (c_char == '#' || !node->children[c_idx]) return;

  node = node->children[c_idx];
  if (node->is_end) {
    result.emplace_back(node->word);
    node->is_end = false;  // Prune to avoid duplicates
  }

  board[row][col] = '#';

  constexpr int kDirs4[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
  for (const auto& dir : kDirs4) {
    int nr = row + dir[0], nc = col + dir[1];
    if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
      Backtrack(board, node, nr, nc, result, m, n);
    }
  }

  board[row][col] = c_char;
}

/// @brief LC 648: Replace words with shortest dictionary root.
/// @param dictionary List of root words.
/// @param sentence String with words to replace.
/// @return Sentence with words replaced by shortest root.
/// @details Example: dict=["cat","bat","rat"], sentence="the cattle..."
///          → "the cat..." (replace "cattle" with "cat").
/// @constraints Time: O(n*l + s*l), Space: O(n*l) where n=dict, s=sentence.
/// @note Tricky: Build trie of roots, split sentence, find shortest prefix
///       match for each word.
[[nodiscard]] std::string ReplaceWords(
    const std::vector<std::string>& dictionary,
    std::string_view sentence) noexcept {
  TrieNode* root = new TrieNode();

  // Build trie from dictionary
  for (const auto& word : dictionary) {
    TrieNode* node = root;
    for (char c : word) {
      int idx = c - 'a';
      if (!node->children[idx]) {
        node->children[idx] = new TrieNode();
      }
      node = node->children[idx];
    }
    node->is_end = true;
  }

  // Split sentence and replace
  std::vector<std::string> words;
  std::string word;
  for (char c : sentence) {
    if (c == ' ') {
      if (!word.empty()) {
        words.emplace_back(std::move(word));
        word.clear();
      }
    } else {
      word += c;
    }
  }
  if (!word.empty()) words.emplace_back(std::move(word));

  std::string result;
  for (int i = 0; i < static_cast<int>(words.size()); ++i) {
    if (i > 0) result += ' ';

    TrieNode* node = root;
    std::string root_word;
    for (char c : words[i]) {
      int idx = c - 'a';
      if (!node->children[idx]) break;
      node = node->children[idx];
      root_word += c;
      if (node->is_end) break;
    }

    result += (node->is_end) ? root_word : words[i];
  }

  return result;
}

/// @brief DFS helper to find longest word.
/// @param node Current trie node.
/// @param path Current path string.
/// @param longest Reference to longest found word.
/// @return void
static void DfsLongest(TrieNode* node, std::string path,
                       std::string& longest) noexcept;

/// @brief LC 720: Find longest word built letter-by-letter.
/// @param words List of words to build trie from.
/// @return Longest word that can be built one letter at a time.
/// @details Example: words=["w","wo","wor","worl","world"]
///          → "world" (can build w→wo→wor→worl→world).
/// @constraints Time: O(n*l), Space: O(n*l).
/// @note Tricky: DFS only through is_end nodes; tracks longest path.
[[nodiscard]] std::string LongestWord(
    const std::vector<std::string>& words) noexcept {
  TrieNode* root = new TrieNode();

  // Build trie
  for (const auto& word : words) {
    TrieNode* node = root;
    for (char c : word) {
      int idx = c - 'a';
      if (!node->children[idx]) {
        node->children[idx] = new TrieNode();
      }
      node = node->children[idx];
    }
    node->is_end = true;
  }

  std::string longest;
  DfsLongest(root, "", longest);

  return longest;
}

/// @brief DFS helper to find longest word (implementation).
static void DfsLongest(TrieNode* node, std::string path,
                       std::string& longest) noexcept {
  if (path.length() > longest.length()) {
    longest = path;
  }
  for (int i = 0; i < 26; ++i) {
    if (node->children[i] && node->children[i]->is_end) {
      DfsLongest(node->children[i], path + char('a' + i), longest);
    }
  }
}

/// @brief LC 676: MagicDictionary with one-letter difference search.
/// @details Find word differing by exactly one letter.
class MagicDictionary {
 public:
  MagicDictionary() noexcept : root_(new TrieNode()) {}

  /// @brief Build dictionary from word list.
  /// @param dictionary Words to add to dictionary.
  /// @return void
  /// @details Time: O(n*l) where n=words, l=avg length.
  void BuildDict(const std::vector<std::string>& dictionary) noexcept {
    for (const auto& word : dictionary) {
      TrieNode* node = root_;
      for (char c : word) {
        int idx = c - 'a';
        if (!node->children[idx]) {
          node->children[idx] = new TrieNode();
        }
        node = node->children[idx];
      }
      node->is_end = true;
    }
  }

  /// @brief Search for word with exactly one letter different.
  /// @param search_word Word to search for.
  /// @return true if exactly one letter differs from dictionary word.
  /// @details Example: search_word="hello" matches "hallo", "herlo" if in dict.
  /// @constraints Time: O(26^l).
  /// @note Tricky: DFS with boolean flag tracking if one char changed.
  [[nodiscard]] bool Search(std::string_view search_word) const noexcept {
    return Dfs(root_, search_word, 0, false);
  }

 private:
  TrieNode* root_;

  /// @brief DFS helper for one-letter-different search.
  /// @param node Current trie node.
  /// @param word Word to match.
  /// @param idx Current index.
  /// @param changed Whether one char already changed.
  /// @return true if match with exactly one change.
  static bool Dfs(const TrieNode* node, std::string_view word, int idx,
                  bool changed) noexcept {
    if (idx == static_cast<int>(word.size())) {
      return changed && node->is_end;
    }

    char c = word[idx];
    for (int i = 0; i < 26; ++i) {
      if (!node->children[i]) continue;
      if (i == (c - 'a')) {
        // Same character, no change
        if (Dfs(node->children[i], word, idx + 1, changed)) {
          return true;
        }
      } else if (!changed) {
        // Different character, mark as changed
        if (Dfs(node->children[i], word, idx + 1, true)) {
          return true;
        }
      }
    }

    return false;
  }
};

}  // namespace trie_playground

int main() {
  using namespace trie_playground;
  std::cout << "=== Trie Playground ===\n\n";

  std::cout << "--- Trie (LC 208) ---\n";
  {
    Trie t;
    t.Insert("apple");
    std::cout << "Insert: \"apple\"\n";
    std::cout << "Search(\"apple\"): "
              << (t.Search("apple") ? "true" : "false") << "\n";
    std::cout << "Search(\"app\"): " << (t.Search("app") ? "true" : "false")
              << "\n";
    std::cout << "StartsWith(\"app\"): "
              << (t.StartsWith("app") ? "true" : "false") << "\n";
  }

  std::cout << "\n--- WordDictionary (LC 211) ---\n";
  {
    WordDictionary wd;
    wd.AddWord("bad");
    wd.AddWord("dad");
    wd.AddWord("mad");
    std::cout << "Words: bad, dad, mad\n";
    std::cout << "Search(\"bad\"): " << (wd.Search("bad") ? "true" : "false")
              << "\n";
    std::cout << "Search(\".ad\"): " << (wd.Search(".ad") ? "true" : "false")
              << "\n";
    std::cout << "Search(\"b.d\"): " << (wd.Search("b.d") ? "true" : "false")
              << "\n";
  }

  std::cout << "\n--- Replace Words (LC 648) ---\n";
  {
    std::vector<std::string> dict = {"cat", "bat", "rat"};
    std::string sentence = "the cattle was rattled by the cat";
    auto result = ReplaceWords(dict, sentence);
    std::cout << "Dict: cat, bat, rat\n";
    std::cout << "Input: " << sentence << "\n";
    std::cout << "Output: " << result << "\n";
  }

  std::cout << "\n--- Longest Word (LC 720) ---\n";
  {
    std::vector<std::string> words = {"w", "wo", "wor", "worl", "world"};
    auto longest = LongestWord(words);
    std::cout << "Words: w, wo, wor, worl, world\n";
    std::cout << "Longest: " << longest << "\n";
  }

  std::cout << "\n--- MagicDictionary (LC 676) ---\n";
  {
    MagicDictionary md;
    std::vector<std::string> dict = {"hello", "hallo", "leetcode"};
    md.BuildDict(dict);
    std::cout << "Dict: hello, hallo, leetcode\n";
    std::cout << "Search(\"hello\"): "
              << (md.Search("hello") ? "true" : "false")
              << " (differs by 1 from hallo)\n";
    std::cout << "Search(\"hallo\"): "
              << (md.Search("hallo") ? "true" : "false")
              << " (differs by 1 from hello)\n";
    std::cout << "Search(\"leetcoded\"): "
              << (md.Search("leetcoded") ? "true" : "false")
              << " (differs by 2)\n";
  }

  return 0;
}
