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
                if stack:
                    last = stack.pop()
                    if match[par] != last:
                        return False
                else:
                    return False
            else:
                stack.append(par)
            
        return False if stack else True
