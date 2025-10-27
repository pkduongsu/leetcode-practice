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
                
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #input: string s, string t
        #output: bool: true if is anagram, not false

        #anagram: a string that has exact same characters as another string

        #def isAnagram(s: str, t: str) -> bool

        #easiest solution is just to check equality of the sorted strings
        #-> Time complexity depends on the complexity of sorting algo
        
        #return sorted(s) == sorted(t)
        #Time: nlogn: where n is the length of string 
        #worst case its not equal -> nlogn + mlogm : len of string s and len of string t
        #space: n + m , len of 2 strings

        #better, solution:
        #use a hashmap and store the count of each strings

        charMapS = {}
        charMapT = {}
        if len(s) != len(t):
            return False

        #we are sure that both have same length now
        for i in range(len(s)):
            charMapS[s[i]] = charMapS.get(s[i], 0) + 1
            charMapT[t[i]] = charMapT.get(t[i], 0) + 1

        return charMapS == charMapT

        #Time: O(n) length of the string s (same for string t if anagram)
        #Space: O(n + m): worst case where every char in both strings are unique

        

    

            
        
        
    