class Solution:
    from collections import defaultdict
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1freq = defaultdict(int)
        for char in s1:
            s1freq[char] += 1

        for l in range (len(s2) - len(s1) + 1):
            
            s2freq = defaultdict(int)
            r = l + len(s1) - 1

            broken = False
            print(f" Examining window from {l} to {r}")
            while l <= r and (not broken):
                char = s2[l]
                if char not in s1freq:
                    broken = True 
                else: 
                    s2freq[char] += 1
                l += 1
            print(f"At end of window scan, s2freq: {s2freq}, s1freq: {s1freq}")
            if (not broken) and (s2freq == s1freq):
                return True 

        return False 

            
            
