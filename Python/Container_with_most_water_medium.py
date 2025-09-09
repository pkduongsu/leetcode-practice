#Brute force: go through every possible combinations of columns and find the maximum area possible
#iterate through array twice -> O(n^2)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currentMax = 0
        
        for i in range(0, len(heights)):
            for j in range(i+1, len(heights)):
                #area of rect: width * height
                currentArea = min(heights[i], heights[j]) * (j - i)
                currentMax = max(currentMax, currentArea)

        return currentMax
    
#optimize: use two pointers, with the idea of maximizing the possible area by finding a higher height if one col is being the constraint (lower height -> lower min(r, l) -> smaller area)
#iterate through array once -> O(n)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r: #cant overlap cause we're choosing separate columns to form area
            currentArea = (r - l) * min(heights[l], heights[r])
            res = max(res, currentArea)
            if (heights[l] < heights[r]):
                l += 1
            elif (heights[l] > heights[r]):
                r -= 1
            else:
                l += 1

        return res