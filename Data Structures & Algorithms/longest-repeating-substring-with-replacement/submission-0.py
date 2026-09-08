class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        l = 0 
        longest_seen = 0
        for r, char in enumerate(s):
            seen[char] = seen.get(char,0) + 1

            while (r - l + 1) - (max(seen.values())) > k:
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    del seen[s[l]]
                l += 1
            
            longest_seen = max(longest_seen,(r-l+1))
        
        return longest_seen