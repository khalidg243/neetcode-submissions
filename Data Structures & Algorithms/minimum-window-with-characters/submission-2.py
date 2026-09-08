class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        need = {}

        for char in t:
            need[char] = need.get(char, 0) + 1

        seen = {}
        satisfied = 0
        l = 0

        shortest_seen = float("inf")
        answer_start = 0

        for r, char in enumerate(s):
            if char in need:
                seen[char] = seen.get(char, 0) + 1

                # This character type has just become satisfied
                if seen[char] == need[char]:
                    satisfied += 1

            while satisfied == len(need):
                window_length = r - l + 1

                # Record the valid window before shrinking it
                if window_length < shortest_seen:
                    shortest_seen = window_length
                    answer_start = l

                left_char = s[l]

                if left_char in need:
                    seen[left_char] -= 1

                    if seen[left_char] < need[left_char]:
                        satisfied -= 1

                l += 1

        if shortest_seen == float("inf"):
            return ""

        return s[answer_start:answer_start + shortest_seen]