#Brute: using replace
#time: O(n^2)
#Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''


#optimal
#Time: O(n)
#Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        charStack = []
        closeOpenMap = {')': '(', '}' : '{', ']': '['}


        for i in range(len(s)):
            if s[i] in closeOpenMap:
                if charStack and charStack[-1] == closeOpenMap[s[i]]:
                    charStack.pop()
                else: 
                    return False
            else:
                charStack.append(s[i])
            
            
        if len(charStack) == 0:
            return True
        else: return False
