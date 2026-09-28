class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        i = len(nums) - 2
        goal = i + 1
        while i > 0:
            if i + nums[i] >= goal:
                goal = i
                i = goal - 1
            else:
                i -= 1
        return i + nums[i] >= goal
