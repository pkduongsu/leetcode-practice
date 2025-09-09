#brute: use hashmap to add key value pair of number and their counts, store in another array to use array.sort, and pop out the top values in a loop ranged k
#-> Time complexity: O(nlogn), space: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNums = {}

        for i in range(len(nums)):
            countNums[nums[i]] = countNums.get(nums[i], 0) + 1
        
        arr = []
        for num, cnt in countNums.items():
            arr.append([cnt, num])

        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

#O(n) solution: use bucket sort with hashmap:
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNums = {}

        for i in range(len(nums)):
            countNums[nums[i]] = countNums.get(nums[i], 0) + 1
        
        arr = [[] for i in range(len(nums) + 1)]

        for n, c in countNums.items(): #return every key value pair in the countNums dict
            arr[c].append(n) #the index now represents the count, and values that has the same count will be in the same subarray at that index

        res = []
        for i in range(len(arr) - 1, 0 , -1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res