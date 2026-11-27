class Solution:
    from collections import defaultdict

    def findMax(self, charCounts):
        maxCount = 0
        for char in charCounts:
            maxCount = max(maxCount, charCounts[char])
        return maxCount

    def characterReplacement(self, s: str, k: int) -> int:

        # we know a substring is valid if 
        # length of that substring - most frequent character count <= k
        # we can increase a window size until we hit the maximum window
        # possible that allows this -> thus allowing a substring length of 
        # len(window)
        # if we hit a window that doesn't allow it, we can
        # shrink the window

        l = 0
        charCounts = defaultdict(int) # stores the freq of each char in the substring
        maxLen = 0
        currSubstring = ""

        for r in range (0, len(s)):
            
            char = s[r]
            charCounts[char] += 1
            currSubstring += char
            
            if (r + 1 - l) - self.findMax(charCounts) <= k:
                # print(f"r: {r}, l: {l}, currSubstring: {currSubstring}, charCounts: {charCounts}")
                # print("able to replace")
                maxLen = max(maxLen, len(currSubstring))
            else:
                # print("shrinking window size")
                charCounts[currSubstring[0]] -= 1
                currSubstring = currSubstring[1:]
                l += 1

        return maxLen
                



        

        



