class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = nums[0]

        l = 0
        r = len(nums) - 1
        while l < r:
            mid = ((r - l) // 2) + l
            if minVal is None or nums[mid] < minVal:
                minVal = nums[mid]
            if nums[mid] < nums[r]:
                r = mid 
            elif nums[mid] > nums[r]:
                l = mid + 1
        return min(minVal, nums[l])


