# Pseudocode:
# two words are anagrams if they have the same count of each letter 


class Solution:
    
    # Worst case - O(nlogn * m). not optimal 
    # A word is an anagram of another word if it has the same letters in the same frequency

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        # for each word in the list, get the counts of each letter from the letters list in that word
        # check which words have the same letter counts
        anagramInfo = defaultdict(list)

        for string in strs:

            counts = [0] * 26 # initialize a list of 26 0s (to hold letter counts from alphabet of 26 letters)

            for char in string:
                charIndex = ord(char) - ord('a')
                counts[charIndex] += 1

            anagramInfo[tuple(counts)].append(string)

    
        res = []
        for key, val in anagramInfo.items():
            res.append(val)

        return res
            

