class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # difference = target - nums[i]

        diffDict = {}
        for i in range (len(nums)):
            #print(f"currElem: {nums[i]}\n")
            difference = target - nums[i]
            #print(f"looking for difference: {difference}\n")
            #print(f"dict: {diffDict}\n")
            if (difference in diffDict):
                return [diffDict[difference], i]
            else:
                diffDict[nums[i]] = i
        