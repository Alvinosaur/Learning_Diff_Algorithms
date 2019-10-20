from sys import maxsize as MAX

class Solution():
    def __init__(self, start, end, N):
        self.N = N  # board size N x N
        self.x1, self.y1 = start
        self.x2, self.y2 = end
        self.path = [[(0, 0, MAX) for i in range(N)] for j in range(N)]
        self.moves = [(-1, 2), (1, 2), (-2, 1), (-2, -1), (2, 1), (2, -1),
                      (-1, -2), (1, -2)]

    def is_valid(self, x, y):
        # check if position is within bounds of board
        return (0 <= x and x < self.N) and (0 <= y and y < self.N)

    def solve(self):
        # keep track of all places we've been so don't go back to a spot we've 
        # been to before... start at x2, y2 which we will mark as moves = 0 
        # from goal... as we move towards x1, y1, we increase moves by 1 each 
        # time
        self.path[self.x2][self.y2] = (self.x2, self.y2, 0)
        self.bfs(self.x2, self.y2)
        result = [(self.x1, self.y1)]
        self.retrace_steps(result)
        return result
        # always start at starting point

    def retrace_steps(self, result):
        x, y = result[-1]
        next_pos = (0, 0)
        min_dist = MAX
        # look at all neighboring moves, see which is shortest
        for (dx, dy) in self.moves:
            if not self.is_valid(x + dx, y + dy): continue
            (xn, yn, dist) = self.path[x + dx][y + dy]
            if dist < min_dist:
                min_dist = dist
                next_pos = (x + dx, y + dy)
        
        result.append(next_pos)
        if next_pos == (self.x2, self.y2): return
        else: self.retrace_steps(result)

    def bfs(self, x, y, steps=0):
        # print('Update(%d, %d)' % (x, y), self.path[x][y])
        if (x == self.x1) and (y == self.y1): return
        for (dx, dy) in self.moves:
            # if out of bounds, just skip
            if not self.is_valid(x + dx, y + dy): continue

            # if path to this position longer than current path, update
            # new path length and point where this came from
            if self.path[x + dx][y + dy][2] > steps + 1:
                self.path[x + dx][y + dy] = (x, y, steps+1)
                self.bfs(x + dx, y + dy, steps+1)

start = (7, 0)
end =  (0, 7)
N = 8
A = Solution(start, end, N)
print(A.solve())
