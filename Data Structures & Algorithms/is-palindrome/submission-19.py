class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftPtr = 0
        rightPtr = len(s) -1 

        s = s.lower()

        if (len(s) == 0):
            return True 

        while (leftPtr < rightPtr):

            while (not s[leftPtr].isalnum()) and (leftPtr < len(s) - 1) :
                leftPtr += 1
            while (not s[rightPtr].isalnum()) and (rightPtr > 0):
                rightPtr -= 1
            
            if not (((s[rightPtr].isalnum()) and (s[leftPtr].isalnum())) and (leftPtr < rightPtr)):
                return True

            leftElem = s[leftPtr]
            rightElem = s[rightPtr]

            if (leftElem != rightElem):
                print(f"Failed on comp {leftElem} and {rightElem}")
                return False
            
            leftPtr += 1
            rightPtr -= 1

        return True

        