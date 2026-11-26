class Solution:
    def isValid(self, s: str) -> bool:

        parenMap = dict()
        parenMap[')'] = '('
        parenMap['}'] = '{'
        parenMap[']'] = '['

        seen = []
        for char in s:
            if char in parenMap:
                if (len(seen) == 0) or (seen[-1] != parenMap[char]):
                    return False
                else:
                    seen.pop(-1)
            else:
                seen.append(char)

        return len(seen) == 0

        