class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0 
        longest = 0
        for r,char in enumerate(s):
            seen[char] = seen.get(char,0) + 1
            while seen[char] > 1:
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    del seen[s[l]]
                l += 1
            longest = max(longest, r-l + 1)
        return longest


            