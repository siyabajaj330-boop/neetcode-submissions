class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # difference = target - nums[i]

        # hash tables have O(1) lookup
        # has at most n keys - O(n) space
        # we check at most n indexes - O(n) time

        diffDict = {} #maps elements to their indexes in nums
        for i in range (len(nums)):
            currElem = nums[i]
            difference = target - currElem

            if (difference in diffDict):
                return [diffDict[difference], i]
            else:
                diffDict[currElem] = i
        