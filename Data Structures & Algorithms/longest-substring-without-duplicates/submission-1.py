class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # starting from the first letter, begin adding letters
        # in forming a substring
        # for each letter added, 
        # add it to the "seen" set
        # if we find a duplicate, begin removing letters from the 
        # beginning of the substring until its not in our set anymore 
        # and continue
        # keep a running max count 

        seen = set()
        maxLen = 0

        substring = ""
        for char in s:
            # if this char is a duplicate, 
            # remove letters from the beginning until its
            # first occurence is gone
            while char in seen:
                # print(char)
                # print(seen)
                letter = substring[0]
                seen.discard(letter)
                substring = substring[1:]

            substring += char
            seen.add(char)
            maxLen = max(maxLen, len(substring))

        return maxLen


