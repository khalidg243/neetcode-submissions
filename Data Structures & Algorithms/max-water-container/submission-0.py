class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0 , len(heights) - 1
        max_seen = 0

        while l < r:
            max_seen = max(max_seen,(r - l) * min(heights[r],heights[l])) 
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max_seen
