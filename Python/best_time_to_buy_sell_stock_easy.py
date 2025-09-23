#brute force
#Time: O(n^2)
#Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                currentProf = prices[j] - prices[i]
                res = max(res, currentProf)

        return res

#Optimal solution
#note: if there are no profitable transaction to be made, can chose not to trade, in this case return value is 0
#Time: O(n) -> Traversing through prices list once
#Space: O(1) -> Only storing l, r, res -> constant memory
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0

        while r < len(prices):
            currentProf = prices[r] - prices[l]
            if currentProf > 0:
                res = max(res, currentProf)
            else: 
                l = r
            r += 1
        return res

