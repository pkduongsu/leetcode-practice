class Solution:
    def trap(self, height: List[int]) -> int:
        #input: a list of column heights-> List[int]
        #output: maximum units of water we can store with the given columns -> int

        #def trapRain(self, height: List[int]) -> int:

        #between 2 columns, the amount of water we can trap is min(l, r)
        #need to find the max (highest cols) on the left and right of each position.

        #what about the water that can be trapped at a position?

        #left col is the limiting factor, height of left is the highest we can store
        #when max left and max right pointers are equal, shift anywhere
        #when left is < right, move left
        #right < left -> move right

        if not height:
            return 0

        l, r = 0, len(height) -1

        maxLeft, maxRight = height[l], height[r]
        res = 0
        while l < r:            
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l] #calculate how much water we can store at current pos of the 
                #left pointer, as left is the limiting factor
            else: #if Right > left, move right, if right = left, move anywhere
                r -= 1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]
        return res

#Time: O(n)
#Space: O(1)

            



        