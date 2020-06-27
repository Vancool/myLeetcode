from queue import PriorityQueue
class Solution(object):
    def merge(self, intervals):
        if len(intervals) == 0 or len(intervals) == 1:
            return intervals
        q = PriorityQueue()
        res = []
        for item in intervals:
            q.put(item)
        res.append(q.get())
        while not q.empty():
            cur = q.get()
            if res[-1][1] >= cur[0]:
                res[-1][1] = cur[1] if cur[1] >= res[-1][1] else res[-1][1]
            else:
                res.append(cur)
        return res
'''
test case:
1. [[1,3]]
2.[[1,4],[2,3]]可能前面那个区间比较大
'''