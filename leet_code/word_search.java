import java.util.List;
import java_datastructures.Trie;

class Solution {
  private TrieNode root;
  public List<String> findWords(char[][] board, String[] words) {
    List<String> res;
    root = buildTrie(words);
    for (int i = 0; i < board.length; i++) {
      for (int j = 0; j < board[i].length; j++) {
        
      }
    }
  }

  private TrieNode buildTrie(String[] words) {
    Trie new_trie = new Trie();
    for (String word : words) {
      new_trie.insert(word);
    }
    return new_trie.root;
  }

}