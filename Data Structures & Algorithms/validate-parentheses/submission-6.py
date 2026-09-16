class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }
        for par in s:
            if par in match:
                if not stack or stack[-1] != match[par]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(par)
            
        return False if stack else True
