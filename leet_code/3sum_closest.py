# Similar Logic to 3sum, O(N^2)
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        started = False
        closest = 0
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                print(i, l, r, total)
                if not started: 
                    started = True
                    closest = total
                else:
                    # if found a closer one
                    if abs(target - total) < abs(target - closest):
                        closest = total
                        
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    return total
        return closest
                
                    

A = Solution()
print(A.threeSumClosest([1, 1, 1, 0], -100))