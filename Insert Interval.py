class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        a, n = [], len(intervals)
        if n == 0:
            return [newInterval]
        for i in range(n):
            if intervals[i][0] > newInterval[0]:
                intervals.insert(i, newInterval)
                break
        # print(intervals)
        if len(intervals) == n:
            intervals.append(newInterval)
        start, end = intervals[0][0], intervals[0][1]
        for i in range(1, n+1):
            s1, e1 = intervals[i-1][0], intervals[i-1][1]
            s2, e2 = intervals[i][0], intervals[i][1]
            if end >= s2:
                end = max(e2, end)
            else:
                a.append([start, end])
                start = s2
                end = max(e2, end)
        a.append([start, end])
        return a
