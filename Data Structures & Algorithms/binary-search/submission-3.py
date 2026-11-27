class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # first, check the middle number of the array
        # if target < mid, search the left half 
            # if target < middle of that, search left half
            # if target > middle of that, search right half 
        # if target > mid, search the right half
            # if target < middle of that, search left half
            # if target > middle of that, search right half 

        l = 0
        r = len(nums) - 1

        if len(nums) == 1:
            return 0 if nums[0] == target else -1 
        if (len(nums) == 0):
            return -1

        while l < r:
            middle = ((r - l) // 2) + l
            print(f"left: {l}, middle: {middle}, right: {r}")
            val = nums[middle]
            if val == target:
                return middle
            elif target > val:
                l = middle + 1
            else: # target < val 
                r = middle

        return l if nums[l] == target else -1 

