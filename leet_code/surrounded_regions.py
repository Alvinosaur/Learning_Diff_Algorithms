class Solution:
    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        unseen = set([(row, col) for row in range(len(board))
                                for col in range(len(board[row]))])
        while(len(unseen) > 0):
            (r, c) = unseen.pop()
            if board[r][c] == 'O':
                surrounded = ((r > 0) and (r < len(board)-1) and
                              (c > 0) and (c < len(board[r])-1))
                # connected: all neighboring 0's whose status needs
                # to still be changed if surrounded
                # surrounded: overall status of that entire group
                connected = [(r, c)]
                surrounded = Solution.dfs(board, unseen, connected,
                    r, c, surrounded)

                if surrounded:
                    for (r, c) in connected:
                        board[r][c] = 'X'
                
    @staticmethod    
    def dfs(board, unseen, connected, r, c, surrounded):
        surrounded &= ((r > 0) and (r < len(board)-1) and
                        (c > 0) and (c < len(board[r])-1))
        for dr, dc in Solution.moves:
            if (r+dr,c+dc) in unseen and board[r+dr][c+dc] == 'O':
                unseen.remove((r+dr, c+dc))
                connected.append((r+dr, c+dc))
                surrounded &= Solution.dfs(board, unseen, connected, r+dr, c+dc, surrounded)
        return surrounded

class Solution2:
    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        save = []
        m, n = len(board), len(board[0])
        for i in range(m): 
            save.append((i, 0))
            save.append((i, n-1))
        for j in range(1, n-1):
            save.append((0, j))
            save.append((m-1, j))
        
        while len(save) > 0:
            r, c = save.pop()
            if r >= 0 and r < m and c >=0 and c < n:
                if board[r][c] == 'O': 
                    board[r][c] = 'S'
                    save += [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        
        board[:] = [['X0'[c == 'S'] for c in row] for row in board]

A = Solution2()
grid = [["O","O","O","O","X","X"],
        ["O","O","O","O","O","O"],
        ["O","X","O","X","O","O"],
        ["O","X","O","O","X","O"],
        ["O","X","O","X","O","O"],
        ["O","X","O","O","O","O"]]

sol = [["O","O","O","O","X","X"],
        ["O","O","O","O","O","O"],
        ["O","X","O","X","O","O"],
        ["O","X","O","O","X","O"],
        ["O","X","O","X","O","O"],
        ["O","X","O","O","O","O"]]
A.solve(grid)
# assert(grid == sol)
for row in grid: print(row)