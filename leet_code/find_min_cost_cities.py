# https://leetcode.com/discuss/interview-question/256806/Amazon-or-OA-or-Min-cost-to-add-new-roads
import heapq

class UF(object):
    def __init__(self):
        self.parents = {}
        self.count = 0  # total number of unconnected

    def insert(self, x):
        # if node not in graph, add it and init itself as alone parent
        if x not in self.parents:
            self.parents[x] = x  # handles cases of unions of single-node graphs
            self.count += 1  # new node not connected to anything yet

    def find(self, x):
        if self.parents[x] != x:
            # recursively get root parent
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        if self.find(x) != self.find(y):
            self.parents[y] = self.parents[x]
            self.count -= 1  # two unconnected graphs now connected

    def exist(self, x):
        return x in self.parents

def find_min_cost_cities(numTotalAvailableCities, 
    numTotalAvailableRoads, roadsAvailable, numNewRoadsConstruct, 
    costNewRoadsConstruct):
    uf = UF()
    total_cost = 0
    for (i, j) in roadsAvailable:
        uf.insert(i)
        uf.insert(j)
        uf.union(i, j)
    
    yet_to_add = []
    for (i, j, cost) in costNewRoadsConstruct:
        # use heap to sort costs
        heapq.heappush(yet_to_add, (cost, i, j))

    # while some cities haven't been added or not all cities connected
    while (len(uf.parents) != numTotalAvailableCities or uf.count > 1):
        cost, i, j = heapq.heappop(yet_to_add)
        if (not uf.exist(i)) or (not uf.exist(j)) or (uf.find(i) != uf.find(j)):
            if not uf.exist(i):
                uf.insert(i)
            elif not uf.exist(j):
                uf.insert(j)
            uf.union(i, j)
            total_cost += cost

    return total_cost

numTotalAvailableCities = 6
numTotalAvailableRoads = 3
roadsAvailable = [[1, 4], [4, 5], [2, 3]]
numNewRoadsConstruct = 4
costNewRoadsConstruct = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]


min_cost = find_min_cost_cities(numTotalAvailableCities, 
    numTotalAvailableRoads, roadsAvailable, numNewRoadsConstruct, 
    costNewRoadsConstruct)

print(min_cost)