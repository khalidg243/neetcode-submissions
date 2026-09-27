class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = 0 
        ans = float('-inf')
        for r in nums:
            temp += r
            if temp < 0:
                temp = 0
            ans = max(ans, temp)
        
        return max(nums) if ans == 0 else ans