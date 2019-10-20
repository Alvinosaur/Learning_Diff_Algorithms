import heapq


def squared_dist(x, y):
    return x**2 + y**2

class Coord():
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __lt__(self, other):
        # when we return true, we are saying self has higher priority than
        # other, so self should be at top of heap... we want maxheap to always
        # remove points with largets magnitude dist from origin, so it makes
        # sense to assign higher priotity to largest dist point so it can be
        # removed
        return squared_dist(self.x, self.y) > squared_dist(other.x, other.y)

class Solution(object):
    def kClosest(self, points, K):
        max_heap = []
        for (x, y) in points:
            heapq.heappush(max_heap, Coord(x, y))
            if len(max_heap) > K: heapq.heappop(max_heap)
        
        return [(c.x, c.y) for c in max_heap]
    

A = Solution()
print(A.kClosest([[1,3],[-2,2], [1, 1], [0, 0], [9, 3]], K = 3))
