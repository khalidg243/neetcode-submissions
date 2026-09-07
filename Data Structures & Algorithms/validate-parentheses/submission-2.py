class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        matching = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for par in s:
            if par in '[{(':
                stack.append(par)
            else:
                if not stack or stack[-1] != matching[par]:
                    return False
                stack.pop()
        
        return not stack 