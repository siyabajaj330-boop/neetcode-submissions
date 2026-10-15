class Solution:
    def encode(self, strs: List[str]) -> str:
        if (len(strs) == 0):
            return "EMPTY"

        print('END'.join(strs))
        return 'END'.join(strs)
        

    def decode(self, s: str) -> List[str]:
        print(s)
        if (s == "EMPTY"):
            return []
        return s.split('END')
