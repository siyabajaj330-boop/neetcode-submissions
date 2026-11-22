class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1

        maxArea = 0

        while l < r:
            lHeight = heights[l]
            rHeight = heights[r]
            area = min(lHeight, rHeight) * (r - l)
            maxArea = max(maxArea, area)
            if lHeight < rHeight:
                l += 1
            else:
                r -= 1

        return maxArea
        