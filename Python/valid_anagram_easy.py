#my first solution
#Complexity: O(nlogn) -> not good, but easy to understand and very readable
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

#second solution: using dictionary
#Complexity: O(n) -> good
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        count[char] = count.get(char, 0) - 1
        if count[char] == 0:
            del count[char]
    
    return len(count) == 0

#using hashtable: 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}

        if (len(s) != len(t)):
            return False

        #in the hashmap, map to key value pairs where key = a character in the word, value = unique count of that character
        for i in range(len(s)): #O(n) where n is the length of the input word
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        return countS == countT #comparison -> worst case, all chars are unique, and dict have the len = len(s) -> O(n)

        #-> Time complexity(O(n) + O(n) = O(2n) => O(n)) - as in time analysis, constants are removed.
        #-> Space complexity : O(k), where k is the number of unique characters . for english, lowercase char, k <= 26 -> treated as O(1)
                
        
        
    