class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = [] 
        max_profit = 0

        for price in prices:
            if not stack or stack[-1] <= price:
                stack.append(price)
            
            while stack and stack[-1] > price:
                stack.pop()

            stack.append(price)
            
            max_profit = max(max_profit,(stack[-1]-stack[0]))
        
        return max_profit
