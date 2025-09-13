#my first solution: using set
#Complexity: Time: O(n)- worst case where n is the length of input list -> each insertion (hasing to a set) is O(1) -> for length n, O(n)
#Space: O(n) - worst case where every char is unique, and nums_set length = len(nums) = n
#there is a better solution using hashmap
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #convert it into a set, and see if the len changes (less than the original) -> duplicate
        nums_set = set(nums)
        return (len(nums_set) < len(nums))
    
#using hashmap:
#Time Complexity: O(n) - n is length of the input list 
#Space Complexity: O(n) - worst case where every number is unique -> size of dict is O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashCount = {}

        for i in range(len(nums)):
            hashCount[nums[i]] = hashCount.get(nums[i], 0) + 1
            if hashCount[nums[i]] > 1:
                return True

        return False
