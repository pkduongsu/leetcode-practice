class Solution:

    def encode(self, strs: List[str]) -> str:
        new_strs = ""
        
        for i in range(len(strs)):
            new_word = ""
            for j in range(len(strs[i])):
                new_word += chr(ord(strs[i][j]) + 1)
            new_word += "/" #add a word separator
            new_strs += new_word
        return new_strs


    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0

        while i < len(s):
            new_word = ""
            while i < len(s) and s[i] != "/": #order in python condition does matter
                decoded_char = chr(ord(s[i]) - 1) 
                new_word += decoded_char
                i += 1
            decoded_strs.append(new_word)
            i += 1 #skip separator

        return decoded_strs
    
    
