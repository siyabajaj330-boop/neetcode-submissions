class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        # start with the leftmost and rightmost bar, since this is the largest width
        # save this area 
        # if the left bars height is > the right bars height,
        # move the right pointer to the left
        # if the right bars height is > the left bars height,
        # move the left pointer to the right
        # since this is the only way the area can potentially increase 
        # compute the area on each step, updating the max seen along the way
        # do this until r < l 

        l, r = 0, len(heights) - 1
        maxArea = 0
        while (l < r):
            lHeight = heights[l]
            rHeight = heights[r]
            currArea = (r - l) * min(lHeight, rHeight)
            maxArea = max(maxArea, currArea)
            if lHeight < rHeight:
                l += 1
            else:
                r -= 1

        return maxArea

