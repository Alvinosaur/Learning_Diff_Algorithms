# Time Limit Exceeded over input of tons of duplicate entries
class Solution:
    def smallestDistancePair(self, nums, k) -> int:
        N = len(nums)
        distances = []
        for i in range(N):
            for j in range(i+1, N):
                distances.append(abs(nums[i] - nums[j]))
        distances.sort()
        return distances[k-1]

    # Time Limit Also Exceeded
    def smallestDistancePair2(self, nums, k) -> int:
        item_count = {}
        for i in range(len(nums)):
            if nums[i] not in item_count: item_count[nums[i]] = 1
            else: item_count[nums[i]] += 1

        keys = list(item_count.keys())
        distances = []
        for i in range(len(keys)):
            val1 = keys[i]
            N = item_count[val1]
            distances += [0] * (N * (N - 1) // 2)
            for j in range(i+1, len(keys)):
                val2 = keys[j]
                distances += [abs(val2 - val1)] * (item_count[val1] * item_count[val2])
        distances.sort()
        return distances[k-1]

    # Works, based on trial-error: https://leetcode.com/problems/find-k-th-smallest-pair-distance/discuss/109082/Approach-the-problem-using-the-%22trial-and-error%22-algorithm
    def smallestDistancePair3(self, nums, k) -> int:
        """
        Strategy: Apply trial-error approach, so in logN binary search find the correct guess.

        Take advantage of the sorted so when counting num smaller pairs, starting i will always be <= the incremented j so can just count j - i
        """
        nums.sort()  # nlogn
        N = len(nums)
        # binary search to narrow down distance pair
        l, r = 0, nums[N-1] - nums[0]  # min, max possible distances
        while (l < r):
            guess = (l + r) // 2  # binary search
            j = 0
            count = 0
            # search for min j s.t nums[j] > i + guess
            # don't change j in this loop since if it works for i, j, 
            # it should also work for i+1, j and etc..
            for i in range(N):
                while (j < N):
                    # want nums[j] - nums[i] <= guess
                    if nums[j] > nums[i] + guess: 
                        break
                    j += 1
                # -1 since we found nums[j] > i + guess, but want <=
                count += j - i - 1  
                
            if count < k:
                l = guess + 1
            else:
                r = guess
        return l  # this is the smallest possible distance pair


A = Solution()

print(A.smallestDistancePair3([1, 6, 1], 3))