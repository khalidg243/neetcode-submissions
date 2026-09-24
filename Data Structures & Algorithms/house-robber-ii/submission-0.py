class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            rob1 = 0  # Best result up to two houses ago
            rob2 = 0  # Best result up to the previous house

            for money in houses:
                current = max(
                    rob1 + money,  # Rob current house
                    rob2           # Skip current house
                )

                rob1 = rob2
                rob2 = current

            return rob2

        return max(
            rob_linear(nums[:-1]),  # Exclude last house
            rob_linear(nums[1:])    # Exclude first house
        )