class Solution(object):
    def leastInterval(self, tasks, n):
        max_val = 0
        max_num = set()
        hashmap = {}
        for task in tasks:
            hashmap[task] = hashmap.get(task, 0) + 1
            if max_val == hashmap[task]: max_num.add(task)
            if max_val < hashmap[task]:
                max_val = hashmap[task]
                max_num = set(task)
        interval_num = max_val-1
        available_time = interval_num * (n-len(max_num)+1)
        rest_task_count = len(tasks) - max_val*len(max_num)
        idle_time = max(0, available_time - rest_task_count)
        return len(tasks) + idle_time

'''
https://leetcode.com/problems/task-scheduler/discuss/104500/Java-O(n)-time-O(1)-space-1-pass-no-sorting-solution-with-detailed-explanation
时间复杂度 O(n)
'''

import heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        hashmap = [0] * 26
        for task in tasks:
            hashmap[ord(task)-ord('A')] += 1
        hashmap.sort()
        i = 25
        while i > 0 and hashmap[i] == hashmap[i-1]:
            i -= 1
        return max(len(tasks), (hashmap[25]-1)*(n+1)+ (25-i+1))

a = Solution()
tasks = ["A","A","A","B","B","B"]
n = 2
print(a.leastInterval(tasks, n))