package java_datastructures;
/*
 * TrieNode has any number of children(26 for 26 possible letters)
*/
class TrieNode {
  public TrieNode[] children = new TrieNode[26];
  public String item = "";

  // Constructor
  public TrieNode() {}
}

public class Trie {
  public TrieNode root;
  public Trie() {
    root = new TrieNode();
  }

  // insert
  public void insert(String word) {
    TrieNode node = root;
    for (char c : word.toCharArray()) {
      if (node.children[c - 'a'] == null) {
        node.children[c - 'a'] = new TrieNode();
      }
      node = node.children[c - 'a'];
    }
    node.item = word;
  }

  // search
  public boolean search(String word) {
    TrieNode node = root;
    for (char c : word.toCharArray()) {
      if (node.children[c - 'a'] == null) return false;
      node = node.children[c - 'a'];
    }
    return node.item.equals(word);
  }
}