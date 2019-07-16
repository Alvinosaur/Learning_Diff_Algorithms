class Solution:
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def findWords(self, board, words):
        result = set()
        self.char_map = dict()
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                c = board[i][j]
                if c not in self.char_map: self.char_map[c] = {(i, j)}
                else: self.char_map[c].add((i, j))
        
        for word in words:
            try:
              all_starts = self.char_map[word[0]]
            except KeyError:
              continue  # letter not in board
            for pos in all_starts:
                (prev_i, prev_j) = pos
                self.char_map[word[0]].remove((prev_i, prev_j))
                found = self.findWordsHelper(word[1:], prev_i, prev_j)
                self.char_map[word[0]].add((prev_i, prev_j))
                if found: result.add(word)
        return list(result)
                
    def findWordsHelper(self, word, i, j):
        if len(word) == 0: return True
        c = word[0]
        if c not in self.char_map: return False
        for di, dj in Solution.moves:
            if (i + di, j + dj) in self.char_map[c]:
                # make move, can't return to prev position
                self.char_map[c].remove((i + di, j + dj))
                guess = self.findWordsHelper(word[1:], i+di, j+dj)
                self.char_map[c].add((i + di, j + dj))
                if guess: return True
        
        return False

board = [
  ["a", "a"]
]
words = ["aaa"]
A = Solution()
print(A.findWords(board, words))