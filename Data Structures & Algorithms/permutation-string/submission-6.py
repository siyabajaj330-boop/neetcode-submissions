class Solution:
    from collections import defaultdict
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        # as we parse through each character of s2, 
        # if that character is in s1, 
        # then for the next len(s1)-1 characters, start
        # looking for other matches
        # if we get to the end and have seen all the letters from s1, 
        # with correct frequencies, we can return true
        # otherwise, if we hit a letter we know isn't in s1, or
        # a letter with different frequency, 
        # we can restore the hash map and continue looking from that
        # letter onwards 

        # eg:
        # s1 = abc, s2 = lecabee
        #                  ^^^ -> True 
        # s1 = abc, s2 = lecaabee
        #                  ^^^^^
        s1freq = dict()
        for char in s1:
            if s1freq.get(char) is None:
                s1freq[char] = 1
            else:
                s1freq[char] += 1

        for r in range (len(s2)):
            # is it still possible to find s1? 
            if len(s2) - (r) < len(s1):
                return False 
            char = s2[r]

            if char in s1freq:
                # print(f"Found starting char {char}")
                s2freq = defaultdict(int)
                s2freq[char] += 1

                nextCharIndex = r + 1
                broken = False 
                while (nextCharIndex < len(s2)) and (not broken) and (nextCharIndex - r < len(s1)):

                      nextChar = s2[nextCharIndex]
                    #   print(f"nextChar: {nextChar}, nextIndex: {nextCharIndex}, r: {r}")
                      if (nextChar in s1freq):
                        s2freq[nextChar] += 1
                        if s2freq[nextChar] > s1freq[nextChar]:
                            broken = True
                      else:
                        broken = True 
                      nextCharIndex += 1

                # print(f"After searching len(s1)-1 chars, have: s2freq: {s2freq}, s1freq: {s1freq}")
                if (not broken) and (s2freq == s1freq):
                    return True

        return False 




