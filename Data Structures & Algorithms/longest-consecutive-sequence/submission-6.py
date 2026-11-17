class Solution:
    from collections import defaultdict

    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Pseudocode:
        # What defines the start of a sequence?
        # A number is the "start" of a sequence if num - 1 doesnt exist. 
        # Thus, we can loop only for numbers which we know are the start of a sequence

        filteredNums = set(nums) # Remove repeats

        if (len(nums) == 0):
            return 0

        maxNum = max(nums)

        maxSeq = 1
        
        for num in filteredNums:
            

            if (num - 1) not in filteredNums:

                currSeq = 1
                broken = False
                currNum = num

                while (not broken):
                    if (currNum + 1) in filteredNums:
                        currSeq += 1
                
                    if ((currNum + 1) not in filteredNums) or (currNum == maxNum):
                        broken = True
                    
                    currNum += 1

                maxSeq = max(maxSeq, currSeq)

        return maxSeq


