#input: sorted numbers - increasing: List[int], targegt: int
#def twoSum(numbers: List[int], target: int)
#return indics of 2 numbers so that they add up to the target
#and index 1 < index 2 -> return List[int] : [index1, index2]
#what will be the expected return when there is no solution? / more than 1 solution? 
#-> can assume there will be one valid solution

#must use o(1) additional space
#because, say we use a hash map, it will be o(n)

#solution 1: hash map
#hashMap solution is just gonna be using the difference
#Time: O(n) where n is the length of the input array
#Space: O(n) where n is the legnth of the input array - worst case, the hashMap will have all the elements of input and their indexes

from typing import List

class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        hashMap = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]

            if diff in hashMap:
                return [hashMap[diff] + 1, i + 1]
            hashMap[numbers[i]] = i 
        
        return []


#solution 2: two pointers

class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #so this case the interviewer asks if we can use O(1) additional space
        #when thinking of O(1) then we think of using pointers in the input array

        l, r = 0, len(numbers) - 1

        while l < r: #no same indices
            currentSum = numbers[l] + numbers[r]

            if currentSum < target:
                #its smaller -> to increase, we need to move our left pointer because it leads towards
                #higher potential sum, since the array is sorted in an ascending order from left to right
                l += 1
            elif currentSum > target:
                #same logic, smaller means right pointer have to move towards the left hand side
                r -= 1
            else: 
                #if its equal, return
                return [l + 1, r + 1] #plus 1 because its 1-indexed

        return []