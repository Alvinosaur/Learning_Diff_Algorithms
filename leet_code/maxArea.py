# Failed b/c time limit exceeded
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # naive: O(N^2)
        max_height = 0
        for i in range(len(height)):
            j = len(height) - 1
            while (j > i):
                max_possible = height[i] * (j - i)
                if (max_possible < max_height): break
                    
                guess = min(height[i], height[j]) * (j - i)
                if guess > max_height:
                    max_height = guess
                j -= 1
        return max_height
                    

# Smarter solution: the limiting wall is the smaller one, so there's no point in keep looking at 
# that wall since changing the other wall won't matter b/c still limited by wall
# change the smaller wall
import math
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # naive: O(N^2)
        max_height = 0
        i, j = 0, len(height) - 1
        while (i < j):
            max_height = max(max_height, 
                        min(height[i], height[j]) * (j - i))
            if (height[i] < height[j]):
                i += 1
            else:
                j -= 1
        return max_height
