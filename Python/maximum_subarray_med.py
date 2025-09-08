#Brute force: compute all possible subarrays combination (save previous current sum value) and compare
#Time complexity: O(n^2)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]
        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur += nums[j]
                res = max(res, cur)
        
        return res




#Linear solution: only compute and take positive contributors to the max array, if current subarray sum is negative, omit immediately as we're aiming for a max
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currentSum = 0

        for num in nums:
            if currentSum < 0: currentSum = 0
            currentSum += num
            maxSub = max(maxSub, currentSum)
        
        return maxSub