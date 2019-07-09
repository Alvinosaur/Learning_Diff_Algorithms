# Time Limit Exceeded
def seen_before(n1, n2, results):
    for res in results:
        if n1 in res:
            res.remove(n1)
            if n2 in res:
                res.append(n1)
                return True
            res.append(n1)
    return False

class Solution:
    def threeSum(self, nums):
        result = []
        num_map = dict()
        for num in nums:
            if num not in num_map: num_map[num] = 0
            num_map[num] += 1
        
        print(num_map)
        
        for n1 in num_map:
            # that number is being used temporarily
            num_map[n1] -= 1
            
            for n2 in num_map:
                if num_map[n2] == 0: continue
                num_map[n2] -= 1
                
                n3 = 0 - n1 - n2

                if (n3 in num_map and num_map[n3] > 0
                    and not seen_before(n1, n2, result)):
                    result.append([n1, n2, n3])
                
                num_map[n2] += 1
            
            num_map[n1] += 1
        return result 


# O(N^2)
"""
General strategy: start with one number, then try to find two other 
numbers that help bring sum to 0. Given that number, we know the numbers 
to the right of it will be >= since nums sorted. Then pick highest and closest 
next larger number. Then taking adv of sorted, we can try reducing the largest number or increasing
next smaller number to try to get a sum of 0.

One optimization: if first number we pick > 0, then any other two numbers
will be > 0 too so impossible to get sum = 0. 

"""
class Solution_Better:
    def threeSum(self, nums):
        result = []
        nums.sort()

        # pick first number, have to stop at len()-2 since need at least 3 nums
        for i in range(len(nums)-2):
            # get rid of duplicates that would produce same answer
            if i > 0 and nums[i] == nums[i-1]:
                continue

            if nums[i] > 0: continue

            l, r = i+1, len(nums)-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                # too small, need to increase lower bound
                if total < 0: l += 1

                # too big, decrease upper bound
                elif total > 0: r -= 1

                # found an answer
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    # ignore other duplicates, use l < r as a safety limit
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return result

test = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
a = Solution()
b = Solution_Better()
print(b.threeSum(test))
print(a.threeSum(test))
