class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.graph = graph
        return self.BFS(0)
    def BFS(self, index):
        paths = []
        if len(self.graph[index]) == 0: return [[index]]
        for next_index in self.graph[index]:
            for subpath in self.BFS(next_index):
                paths.append([index] + subpath)
        return paths


graph = [[1,2], [3], [3], []] 
A = Solution()
print(A.allPathsSourceTarget(graph))