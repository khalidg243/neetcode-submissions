class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r-l)//2)
            if nums[mid] < nums[r]:
                r = mid 
            else:
                l = mid + 1 
        
        offset = l

        l , r = 0 + offset , len(nums) - 1 + offset

        while l <= r:
            mid = l + ((r-l) // 2)
            if nums[mid % len(nums)] == target:
                return mid % len(nums)
            elif nums[mid % len(nums)] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
