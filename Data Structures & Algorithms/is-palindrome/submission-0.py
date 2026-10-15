class Solution:
    # Pseudocode:
    # Have a start pointer and an end pointer
    # If startElem != endElem, return False
    # else startPointer += 1 and endPointer -= 1
    def isPalindrome(self, s: str) -> bool:

        newS = ""
        for char in s:
            if (char.isalpha()) or (char.isdigit()):
                newS += (char)

        newS = newS.lower()
        
        startPointer = 0
        endPointer = len(newS) - 1

        while (startPointer < endPointer):
            startElem = newS[startPointer]
            endElem = newS[endPointer]

            if (startElem != endElem):
                print(f"Found startElem {startElem} and endElem {endElem}\n")
                return False
            startPointer += 1
            endPointer -= 1

        return True

        