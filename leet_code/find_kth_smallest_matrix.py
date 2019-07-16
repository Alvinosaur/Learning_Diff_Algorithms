class Solution:
    def kthSmallest(self, matrix, k) -> int:
        rows, cols = len(matrix), len(matrix[0])
        l, r = matrix[0][0], matrix[0][0]
        
        # O(N)
        for i in range(rows):
            l = min(l, matrix[i][0])
            r = max(r, matrix[i][-1])
        
        # O(NlogN)
        while (l < r):
            m = (l + r) // 2  # guess
            print('l, m, r', l, m, r)
            
            # evaluate this guess: count numbers less than it
            count = 0
            for row in matrix:
              j = cols - 1
              while (j >= 0 and row[j] > m): j -= 1
              count += j + 1
            
            # even if count == k, set r = m b/c we want l, the smallest possible
            # 
            if count < k: l = m + 1  
            else: r = m
        
        return l

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
A = Solution()
print(A.kthSmallest(matrix, 8))