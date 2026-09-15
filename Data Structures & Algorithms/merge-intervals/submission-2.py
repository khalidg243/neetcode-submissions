class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        i = 1
        n = len(intervals)
        ans = [intervals[0]]
        while i < n:
            last_end = ans[-1][1]
            if intervals[i][0] <= last_end <= intervals[i][1]:
                ans[-1][1] = intervals[i][1]
            elif last_end > intervals[i][1]:
                i += 1
            else:
                ans.append(intervals[i])
            i += 1
        
        return ans
                
            
            
             