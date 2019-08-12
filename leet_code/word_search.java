import java.util.List;
import java_datastructures.Trie;

class Solution {
  private TrieNode root;
  private List<String> res;
  public List<String> findWords(char[][] board, String[] words) {
    root = buildTrie(words);
    for (int i = 0; i < board.length; i++) {
      for (int j = 0; j < board[i].length; j++) {
        dfs(board, root, i, j);
      }
    }
    return res;
  }

  private void dfs(char[][] board, TrieNode node, int i, int j) {
    char c = board[i][j];
    if (c == '#') return;
    board[i][j] = '#';  // make move, can't return to prev location
    if (node.children[c - 'a'] != null) node = node.children[c - 'a'];
    if (node.item != "") res.add(node.item);

    // Search in all 4 directions
    if (i > 0) dfs(board, node, i-1, j);
    if (j > 0) dfs(board, node, i, j-1);
    if (i < board.length) dfs(board, node, i+1, j);
    if (j < board[i].length) dfs(board, node, i, j+1);
  }

  private TrieNode buildTrie(String[] words) {
    Trie new_trie = new Trie();
    for (String word : words) {
      new_trie.insert(word);
    }
    return new_trie.root;
  }

}