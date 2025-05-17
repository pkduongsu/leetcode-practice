#Brute force, O(n^2)
#For each element, we loop through the whole nums list to find its complement to sum up to target, which takes O(n) -> O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if (i != j and nums[i] + nums[j] == target):
                    return [i,j]
            
        return []

#Better Solution Requires Hashmap. Come back with that studied.
        