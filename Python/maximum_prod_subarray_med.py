#Brute: Time O(n^2)
#Space: O(n)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        #O(n^2)
        for i in range(len(nums)):
            prod = 1
            for j in range(i, len(nums)):
                prod *= nums[j]
                maxProd = max(maxProd, prod)

        return maxProd
    
# Optimal O(n) solution:
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp = curMax * num
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            res = max(res, curMax)
        return res