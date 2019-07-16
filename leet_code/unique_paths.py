class Solution:
    moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    target_vals = {0, 2}
    
    def uniquePathsIII(self, grid) -> int:
        self.grid = grid
        self.start = None
        self.unseen = set()
        self.memo = dict()
        self.find_unseen_nodes()
        return self.uniquePathsIIIHelper(self.start[0], self.start[1])
        
    
    def find_unseen_nodes(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] in Solution.target_vals:
                    self.unseen.add((i, j))
                elif self.grid[i][j] == 1:
                    self.start = (i, j)
        assert(self.start is not None)
        
        
    def uniquePathsIIIHelper(self, start_row, start_col):
        total = 0
        for drow, dcol in Solution.moves:
            new_row, new_col = start_row + drow, start_col + dcol
            if not self.in_bound(new_row, new_col): continue
            
            # Case 1: visit unvisited node, make move
            if self.grid[new_row][new_col] == 0:
                self.grid[new_row][new_col] = 1
                self.unseen.remove((new_row, new_col))

                result = self.uniquePathsIIIHelper(new_row, new_col)
                total += result
                
                self.grid[new_row][new_col] = 0
                self.unseen.add((new_row, new_col))
            
            # Case 2: visit goal
            elif self.grid[new_row][new_col] == 2:
                if len(self.unseen) == 1 and (new_row, new_col) in self.unseen:
                    total += 1
                    break

        return total
                
    def in_bound(self, row, col):
        return ((0 <= row and row < len(self.grid)) and 
                (0 <= col and col < len(self.grid[row])))

A = Solution()
print(A.uniquePathsIII([[1, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 2, -1]]))