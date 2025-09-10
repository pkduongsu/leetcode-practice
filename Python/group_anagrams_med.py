#Brute: sort using sorted -> complexity: O(m * nlogn): m being the number of elements in the list, n is the length of the longest string
#space: O(m * n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for i in range(len(strs)):
            sortedString = ''.join(sorted(strs[i])) #sorted returns a list, instead needs to return string -> ''.join(sorted(strs[i]))
            res[sortedString].append(strs[i])


        return list(res.values())
    
#optimal: use a hashmap to map the values by the count of characters stored in a list
#Time: O(m * n)
#Space: O(m * n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 #initialize a count of characters (26 characters in the alphabet) array for each string
            for char in s:
                #update the count of each char in the count
                #we map indexes to characters (ex: 0 - a, 25 - z)
                #we can do that by calculating the offset between current char ASCII value with char a
                count[ord(char) - ord("a")] += 1

            #after we got the count for each char, we use that as the dict key
            #in python, list cannot be keys -> convert to tuple
            res[tuple(count)].append(s)

        return list(res.values())



                    

