class Solution:
    def isHappy(self, n: int) -> bool:
        x = n
        seen = {}
        while x not in seen:
            seen[x] = True
            temp = 0
            while x > 0 :
                temp += pow((x%10),2)
                x //= 10
            x = temp
            
        if x == 1:
            return True
        else:
            return False