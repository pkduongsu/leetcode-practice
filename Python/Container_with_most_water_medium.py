#Brute force:
#Time complexity: go through array twice in a nested loop -> O(n^2) where n is the maximum length of the heights array
#Space complexity: sotring only maxArea, current Area -> O(1)

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #define in the problem: output is the maximum area that we can achieve
        #Area of a rectangle: height * width
        #height: constrained by the lower bar -> get the lower bar using min func
        #width: distance between 2 bars -> index of the further, rightmost bar - index of leftmost one (or just use abs)
        maxArea = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                currentArea = min(heights[i], heights[j]) * (j - i)
                maxArea = max(maxArea, currentArea)

        return maxArea

    
#optimize: use two pointers, with the idea of maximizing the possible area by finding a higher height if one col is being the constraint (lower height -> lower min(r, l) -> smaller area)
#iterate through array once -> O(n)
#Space: O(1)
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