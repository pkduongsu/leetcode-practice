#Complexity: O(n)
#can be improved
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        chars = [char for char in str(x)]
        rev = []
        for i in range(0, len(chars)):
            rev.append(chars[(len(chars) - 1) - i])

        if chars == rev:
            return True

        return False
        