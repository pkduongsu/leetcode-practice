#my first solution: using set
#Complexity: O(n) -> good
#there is a better solution using hashmap
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #convert it into a set, and see if the len changes (less than the original) -> duplicate
        nums_set = set(nums)
        if (len(nums_set) < len(nums)):
            return True
        
        return False

#can further impprove this by simple return (len(nums_set) < len(nums))