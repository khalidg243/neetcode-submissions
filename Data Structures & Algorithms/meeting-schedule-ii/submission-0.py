"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        
        start.sort()
        end.sort()

        cnt = 0
        max_seen = 0

        t = b = 0

        while t < len(start):
            if start[t] < end[b]:
                cnt += 1
                t += 1
            else:
                cnt -= 1
                b += 1
            max_seen = max(max_seen, cnt)
        
        return max_seen
            
            