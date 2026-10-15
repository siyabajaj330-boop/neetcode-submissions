# Pseudocode:
# two words are anagrams if they have the same count of each letter 


class Solution:
    
    # Worst case - O(n * m). not optimal 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramInfo = dict()

        # O(n)
        for string in strs:

            #O(mlogm)
            sortedStr = sorted(string)
            sortedStr = ''.join(sortedStr)

            if (anagramInfo.get(sortedStr) is None):

                anagramInfo[sortedStr] = [string]
            else:
                anagramInfo[sortedStr].append(string)

        res = []
        # O(n)
        for key, val in anagramInfo.items():
            res.append(val)
        return res
            



        