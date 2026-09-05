class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return len(nums)

        dictionary = {}

        for i,num in enumerate(nums):
            dictionary[num] = i
        
        sequence = []
        for num in nums:
            if num - 1 not in dictionary and num + 1 in dictionary:
                sequence.append(num)
            
        if not sequence:
            return 1

        max_seen = 0

        for num in sequence:
            x = num + 1
            cnt = 1
            while x in dictionary:
                cnt += 1
                x += 1
            max_seen = max(max_seen,cnt)
        
        return max_seen