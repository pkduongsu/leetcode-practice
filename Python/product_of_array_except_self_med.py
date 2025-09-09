#Time O(n), Memory O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = postfix = 1
        output = [1] * ((len(nums))) #set the length to be the length exact length of input array

        for i in range(0, len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1): #how the list in python iterates backwards
            output[i] *= postfix
            postfix *= nums[i]

        return output