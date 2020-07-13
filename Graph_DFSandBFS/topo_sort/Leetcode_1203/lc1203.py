from collections import deque,defaultdict
class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        '''
        此处不能写：（写了虽然也可以过样例吧..)
        group = [m if i == -1 else i for i in group]
        '''
        in_degree = [0] * n
        group_indegree = [0]*m
        res = []
        zero_group = defaultdict(list)
        graph = defaultdict(list)
        group_graph = defaultdict(list)
        zero_queue = deque()
        for i in range(n):
            in_degree[i] += len(beforeItems[i])
            for p in beforeItems[i]:
                graph[p].append(i)
                if group[p] != group[i]:
                    group_graph[group[p]].append(group[i])
                    group_indegree[group[i]] += 1
            if in_degree[i] == 0:
                zero_queue.append(i)
        group_queue = deque([i for i in range(m) if group_indegree[i] == 0])
        while zero_queue:
            for _ in range(len(zero_queue)):
                task = zero_queue.popleft()
                n -= 1
                zero_group[group[task]].append(task)
                for next_task in graph[task]:
                    in_degree[next_task] -= 1
                    if in_degree[next_task] == 0:
                        zero_queue.append(next_task)
        if n != 0: return []
        while group_queue:
            g = group_queue.popleft()
            m -= 1
            res += zero_group[g]
            for other_g in group_graph[g]:
                group_indegree[other_g] -= 1
                if group_indegree[other_g] == 0:
                    group_queue.append(other_g)
        return res if m == 0 else []

'''
task case:
n = 5
m = 5
group = [2,0,-1,3,0]
beforeItems = [[2,1,3],[2,4],[],[],[]]

不仅要考虑任务之间的拓扑关系，也要考虑队伍之间的拓扑关系

队伍之间的拓扑关系要去掉自环，否则会跑不出来...


'''
a = Solution()
n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
print(a.sortItems(n, m, group, beforeItems))