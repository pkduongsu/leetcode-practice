from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #input: nums: List[int]
        #return length of longest consecutive sequence that can be formed -> output: int
        #def LongestConsecutive(nums: List[int]) -> int
        
        #brute: for each number, find the longest possible consecutive sequence that can be formed
        # for loop for each number in the input array
        # skip duplicates -> use a set

        #store all the unique numbers of the input array in a set

        # maxLength = 0
        # uniqueNums = set(nums)

        # for num in nums:
        #     streak = 0
        #     current = num
        #     while current in uniqueNums:
        #         streak += 1
        #         current += 1 #check if there is a consecutive sequence of this number
        #         #if next number is not in the set, break
        #         #-> we'll loop through every possible sequence that can be formed with this number
        #     #after we break out, update the max length
        #     maxLength = max(maxLength, streak)
        # return maxLength

        #=> with this approach, we got 
        #Time Complexity: O(n^2) - worst case when for a number, a sequence can be formed with the length equal to the length of input array
        #where n is the length of the input array
        #Space: O(n) - where n is the number of unique elements in the array, worst case all are unique => n

        #how can we improve
        #reframe the problem to finding sequences
        #Ex: Input: [100, 4, 200, 1, 3, 2]
        #Sequences: [1, 2, 3, 4] - [100] - [200]
        #finding sequences beginnings -> left of the beginnings (Ex: for 1 its 0, for 100 its 99)
        #doesn't exist in the original input array
        #for those beginnings, we will simply check if the next consecutive number exists in the original array
        #after checking all possible consecutive elements of that sequence, we will just update the max length of sequences
        #so that requires a variable for it - maxLength
        #we'll eventually go through all possible elements of the array
        # and find the final max length

        maxLength = 0
        numSet = set(nums)

        for num in nums:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                maxLength = max(maxLength, length)

        return maxLength
    
           #The major difference is in the guard condition to check for sequences beginnings
       #for the first solution:
       # -> check every possible sequences for every number in the array
       # => complexity O(n^2)
       #for the second solution, the internal loop to find sequences only gets initialize when 
       #a sequence beginning is found
       #-> eventually only go through sequences beginning and its possible consecutive elements, which
       #are also in the input array
       #as a result, will go through every element of the input array only once
       #=> massively reduce complexity to O(n)
       #Space: because we need a set of nums array, complexity will also be O(n)


         


        