class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        need = {}
        for char in t:
            need[char] = need.get(char,0) + 1
        
        shortest_seen = float('inf')
        l = 0
        satisfied = 0
        have = {}
        ans = []
        for r, char in enumerate(s):
            if char in need:                
                have[char] = have.get(char,0) + 1
                if have[char] == need[char]:
                    satisfied += 1
            while satisfied == len(need):

                if r-l+1 < shortest_seen:
                    shortest_seen = r-l+1
                    ans = [l,r] 

                if s[l] in have:
                    have[s[l]] -= 1
                    if have[s[l]] < need[s[l]]:
                        satisfied -=1
                    if have[s[l]] == 0:
                        del have[s[l]]
                
                l += 1
        
        return s[ans[0]:ans[1] +1] if shortest_seen != float('inf') else ""
            
                
