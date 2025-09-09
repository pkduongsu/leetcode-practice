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
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    count_s, count_t = {}, {}
    
    for char in s:
        count_s[char] = count_s.get(char, 0) + 1
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1
    
    return count_s == count_t