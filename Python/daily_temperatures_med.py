class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Input: temperatures: List[int] - array of temperatures where each element represents daily temperature on ith day
        #Output: result: List[int] - array of the number of days after ith day before a warmer temperature appears
        #Question: what if there are no days that have higher temperature than the current one?
        # -> result[i] = 0

        #Ex: [19, 20, 18, 21, 30, 35]
        # result: [1, 2, 1, 1, 1, 0]

        #brute force solution: use a nested loop to go through every combinations and calculate the number of days till
        #higher temperature through a variable that is defined for each temperatures array element
        #if result is found (higher temperature date), append to result array

        #This solution will have the time complexity of : O(n^2), where n is the length of the temperature array
        #[19, 19, 19, 19, 21]
        #Space Complexity:  O(n) where n is the length of the temperatures array

        res = []

        for i in range(len(temperatures)):
            cnt = 0
            for j in range(i + 1, len(temperatures)):
                if (temperatures[j] > temperatures[i]):
                    cnt += 1
                    break
                else:
                    cnt += 1
                if j == len(temperatures) - 1:
                    cnt = 0
            res.append(cnt)

        return res   
    
#Using stack:
#for every values in the temperatures array, at index ith:
#Push the current temperature onto the stack, then, if there is a temperature value that is greater than the current stack top, pop the values from the stack and find the difference
#of indexes between the temperatures found
#Ex:  [30,38,30,36,35,40,28]
#Stack: [30]
     
     
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = []

        for i, temp in enumerate(temperatures): #enumerate returns the index first, then the value at that index of a list of values. Ex: [(0, 30), (1, 35), (2, 39)]
            while s and temp > s[-1][0]:
                currentTemp, currentInd = s.pop()
                res[currentInd] = i - currentInd
            s.append([temp, i]) 

        return res
    




        