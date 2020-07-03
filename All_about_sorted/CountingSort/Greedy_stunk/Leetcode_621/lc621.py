import heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        t = 0
        hashmap = {}
        for task in tasks:
            hashmap[task] = hashmap.get(task, 0)+1
        min_heap = []
        for key, value in hashmap.items():
            min_heap.append([0, key, value])
        while min_heap:
            heapq.heapify(min_heap)
            time, task, count = heapq.heappop(min_heap)
            t += time+1
            for i in range(len(min_heap)):
                min_heap[i][0] = 0 if min_heap[i][0] <= time+1 else min_heap[i][0] - time -1
            count -= 1
            if count > 0:
                heapq.heappush(min_heap, [n, task, count])
        return t
'''
这题我不会做， 原来是用贪心
'''
a = Solution()
tasks = ["A","A","A","B","B","B"]
n = 2
print(a.leastInterval(tasks, n))