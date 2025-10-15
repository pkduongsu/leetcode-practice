from typing import List
import math
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #calculate the total time of eating a pile
        #need a variable to track the total time to eat all bananas
        #in a loop, from 

        #assume that eating rate > 0, always
        #starting from default 1
        # => calculate all possible eating rate until it satisfy the condition
        # => brute force
        
        #Time complexity: O(n * m) where n is the number of piles, and m is the min eating rate
        #becuase with this implementation, we will loop through entire input array for each possible eating rate
        #from 1 till we find the desired eating rate
        #Space: O(1)

        # eating_rate = 1
        
        # while True:
        #     total_time = 0
        #     for pile in piles:
        #         if pile % eating_rate != 0:
        #             pile_time = pile // eating_rate + 1
        #         else:
        #             pile_time = pile // eating_rate
        #         total_time += pile_time

        #     if total_time <= h:
        #         return eating_rate
        #     else:
        #         eating_rate += 1

        #this can work for small pile numbers, but for large numbers like 999999999
        #it would be too inefficient
        #as its looping through the entire input array till it finds the desired eating_rate, which
        #what if it gets to millions, can execute millions time
        #instead, is there anyu ways to determine bounds?

        #what if we look at the number of elements and the desired eating_time
        #to determine the avg time to eat a stack if we want to satisfy that desired eating_time?

        #ex: h = 9 for piles = [1, 4, 3, 2] => on avg each pile takes 9 / 4 = 2.25

        #what about the case of piles=[1,1,1,999999999] and h = 10
       
        #with the same approach as the brute force, what if we reframe this problem
        #to searching for the right value in the range of [1, max(piles)]

        l = 1
        r = max(piles)
        minRate = max(piles)

        while l <= r:
            midRate = (l + r) // 2
            #calculate total time and update?
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / midRate)
            if total_time <= h:
                minRate = min(minRate, midRate)
                r = midRate - 1
            else:
                l = midRate + 1

        return minRate
    
    #With binary search approach, we reduce the time complexity to O(n * logm) 
    #where n is the number of piles, and m is the maximum number of bananas in a pile
    #Space complexity: O(1) - as we're just storing variables for bounds and midpoints



