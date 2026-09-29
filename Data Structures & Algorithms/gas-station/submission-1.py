class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
       
        prefix = 0
        ans = 0

        for i in range(len(gas)):
            prefix += (gas[i] - cost[i])
            if prefix < 0:
                prefix = 0
                ans = i + 1 
        return ans

        
