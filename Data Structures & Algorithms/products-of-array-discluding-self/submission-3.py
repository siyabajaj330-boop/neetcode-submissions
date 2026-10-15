

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        leftProd = 1
        res = [1] * len(nums) # placeholder for products to be accumulated into
        for i in range (len(nums)):
            res[i] = leftProd
            leftProd *= nums[i]
        # now res[i] will hold the product of all elements to the left of i, for each i

        rightProd = 1
        for i in range (len(nums) - 1, -1, -1): #loop from right -> left
            res[i] *= rightProd
            rightProd *= nums[i]
        return res


            
        
        