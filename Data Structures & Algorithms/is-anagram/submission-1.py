
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sDict = dict()
        tDict = dict()

        for i in range (len(s)):
            letterS = s[i]
            letterT = t[i]
            if (letterS not in sDict):
                sDict[letterS] = 1
            else:
                sDict[letterS] += 1

            if (letterT not in tDict):
                tDict[letterT] = 1
            else:
                tDict[letterT] += 1
        
        for key in sDict:
            if (key not in tDict):
                return False
            if (tDict[key] != sDict[key]):
                return False
        return True
            
        