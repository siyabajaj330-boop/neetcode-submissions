class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Brute force
        # for each elem
        # while you havent found a blockage, 
        # find elem + 1 within elems and increment the count
        # update elem to be elem + 1 and search continues 


        # Optimized:
        # each number can only be the start of a sequence if (num - 1) does not exist in nums 
        # remove duplicates - make nums set(nums)
        # then, for each num in nums:
        # if num is the start of a sequence, then while the sequence can continue, 
        # keep checking if (num + 1) is in nums and increment the count
        # else move onto the next num

        nums = set(nums)
        maxCount = 0
        for num in nums:
            if (num - 1) not in nums:
                count = 1
                broken = False
                while (not broken):
                    if (num + 1) in nums:
                        count += 1
                        num += 1
                    else:
                        broken = True
                if (count > maxCount):
                    maxCount = count

        return maxCount


                

        
        
        