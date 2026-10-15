class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramsDict = {}

        for string in strs:
            #print(string)
            sortedWord = sorted(string) # O(logn)
            sortedWord = ''.join(sortedWord) #O(n)
            #print(sortedWord)
            if (sortedWord in anagramsDict):
                anagramsDict[sortedWord].append(string)
            else:
                anagramsDict[sortedWord] = [string]

        final = []
        for word, anagrams in anagramsDict.items():
            final.append(anagrams)
        return final
        