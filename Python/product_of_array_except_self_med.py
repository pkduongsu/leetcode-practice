#Time O(n^2), Memory O(n) for output array
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j: 
                    continue
                product *= nums[j]
            
            res[i] = product

        return res


#Time O(n), Memory O(n)
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