#Input: nums: List[int], target: int
#Output: [i, j] such as nums[i] + nums[j] == target, i != j
#Question: is it safe to assume that for every input array nums, there will be a pair of indices
#i, j that satisfy the condition? if not, what is the expected output? #if not return None?
#Question: do we have to return the output in any specific order? -> smaller first, or any?

#brute force: 
#Ex 1: nums[0] + nums[1] == target -> return [0, 1]
#Ex 2: nums = [1, 2, 3, 4], target = 6 -> 12 13 14 23 24 ... -> return [2, 4] (not [4, 2])
#however, this solution goes through the input array twice in worst case scenario, where the desired 
#indexes are at the end of the array -> Time: O(n^2), Space: O(1),  where n is the number of elements in the input array.

#hashmap:
#nums = [1, 2, 3, 4], target = 6 
#nums[j] == target - nums[i] -> this (nums[j]) has to exist somewhere in the input array
#Ex 1: nums[0] = 1 -> v = 6 - 1 = 5 -> if v in nums -> return its index as its what we were 
#looking for -> using a hashmap that allows efficient lookups by keys, we can implement this
#(key: desired value, value: index) -> hashNum[desired_value] == index -> return [i, hashNum[desired_value]]
#Since this solution only goes through the input array once (worst case desired_value - index j will be at the end of the input array)
#Time : O(n), Space: O(n), where n is the number of elements in the input array.


#My first solution
#Brute force, O(n^2)
#For each element, we loop through the whole nums list to find its complement to sum up to target, which takes O(n) -> O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if (i != j and nums[i] + nums[j] == target):
                    return [i,j]
            
        return []

#Better Solution Requires Hashmap
#Time: O(n)
#Memory: O(n)
class Solution(object):
        def twoSum(self, nums, target):
            prevMap = {}
                
            for i in range(0, len(nums)):
                #hashmap (value: key, index: value)
                diff = target - nums[i]
                if diff in prevMap: 
                    return [prevMap[diff], i] #first index -> key exists in hashmap, second recent index
                else:
                    prevMap[nums[i]] = i #add the traversed value to the hashmap
                        
            return []      
        
        