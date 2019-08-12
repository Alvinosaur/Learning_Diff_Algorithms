class Solution:
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def numIslands(self, grid) -> int:
        islands = 0
        # all (row, col) that haven't been visited yet
        unseen = set([(row, col) for row in range(len(grid))
                                    for col in range(len(grid[row]))])
        while(len(unseen) > 0):
            r, c = unseen.pop()
            if grid[r][c] == '1':
                # haven't seen this 1 connected to anything, so new island
                islands += 1  
                self.dfs(grid, unseen, r, c)

        return islands
        

    def dfs(self, grid, unseen, r, c):
        for dr, dc in Solution.moves:
            if (r+dr, c+dc) in unseen:
                unseen.remove((r+dr, c+dc))
                if grid[r+dr][c+dc] == '1':
                    self.dfs(grid, unseen, r+dr, c+dc)
                



A = Solution()
grid = [
    '11110',
    '11010',
    '10101',
    '01010'
]
print(A.numIslands(grid))