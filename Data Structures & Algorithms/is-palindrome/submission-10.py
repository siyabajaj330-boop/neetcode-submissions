class Solution:
    # Pseudocode:
    # Have a start pointer and an end pointer
    # If startElem != endElem, return False
    # else startPointer += 1 and endPointer -= 1
    def isPalindrome(self, s: str) -> bool:

        # newS = ""
        # # O(n)
        # for char in s:
        #     if (char.isalpha()) or (char.isdigit()):
        #         newS += (char.lower())
        s = s.strip()
        n = len(s)
        startPointer = 0
        endPointer = n - 1

        # O(n/2) ~ O(n)
        while (startPointer < endPointer):
            
            startElem = s[startPointer]
            while ((not (startElem.isalpha())) and (not (startElem.isdigit()))) and (startPointer < n - 1):
                startPointer += 1
                startElem = s[startPointer]
                
                
                
            
            endElem = s[endPointer]
            while ((not (endElem.isalpha())) and (not (endElem.isdigit()))) and (endPointer >= 0):
                endPointer -= 1
                endElem = s[endPointer]

                if (endPointer < startPointer):
                    
                    return True

            startElem, endElem = startElem.lower(), endElem.lower()


            if (startElem != endElem):
                print(f"Found startElem {startElem} and endElem {endElem}\n")
                return False
            startPointer += 1
            endPointer -= 1

        return True

        