import heapq

class Coord(object):
    def __init__(self, coord):
        self.x, self.y = coord
    
    def __lt__(self, other):
        return (self.x**2 + self.y**2) > (other.x**2 + other.y**2)

    def __repr__(self):
        return '(%d, %d)' % (self.x, self.y)


def to_tuple(coords):
    return [(o.x, o.y) for o in coords]


def k_smallest_dist(points, K):
    result = []
    for p in points:
        heapq.heappush(result, Coord(p))
        if len(result) > K: heapq.heappop(result)

    return to_tuple(result)

points = [[3,3],[5,-1],[-2,4], [0,0], [1, 3], [-2, -2]]
K = 4
res = k_smallest_dist(points, K)
print(res)


