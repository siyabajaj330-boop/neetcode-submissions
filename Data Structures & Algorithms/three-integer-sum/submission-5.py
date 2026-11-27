class Solution:
    from collections import defaultdict

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort() # sort the nums, O(nlogn)
        triplets = []

        for i in range (len(nums)):

            val1 = nums[i]
            if (i > 0):
                if (nums[i] == nums[i - 1]):
                    continue
            
            l = i + 1
            r = len(nums) - 1
            diff = 0 - val1

            while (l < r):
                if nums[l] + nums[r] == diff:
                    triplets.append([val1, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < len(nums) and (nums[l] == nums[l-1]):
                        l += 1

                elif nums[l] + nums[r] < diff:
                    l += 1

                else:
                    r -= 1

        return triplets


            
