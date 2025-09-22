#my first solution:
#Complexity: Time: O(n), Space: O(2n) -> O(n)
#can be improved in terms of space complexity
class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = []
        s_list = [char.lower() for char in s if char.isalnum()]
        print(s_list)
        for i in range(len(s) - 1, -1, -1): #how to loop backwards till the last char in python
            if s[i].isalnum():
                rev.append(s[i].lower())


        print(rev)

#Time: O(n) - looping through every char in the string -> n: maximum length of the string
#Space: O(1) - only storing 2 variables - l, r
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1


        while l <= r:
            if not s[l].isalnum():
                l += 1
                continue
            
            if not s[r].isalnum():
                r -= 1
                continue
            
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        
        return True
