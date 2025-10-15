from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #input: array of distinct integers nums, sorted in ascending order -> nums: List[int]
        #and an int: target
        #output: search for target within nums, if exists return index: int
        #else return -1

        #def search(nums: List[int], target: int) -> int
        #Time complexity: O(log n) where n is the length of the input array
        #its log n because we're searching half of the input array every iteration till we find the value
        #instead of n^2 (searching the entire array for every element)
        #Space complexity: O(1) - just spaces for pointers, not considerable
        l, r = 0, len(nums) - 1

        while l <= r:
            midPoint = (l + r) // 2
            if nums[midPoint] < target:
                l = midPoint + 1
            elif nums[midPoint] > target:
                r = midPoint - 1
            else:
                return midPoint

        return -1