from collections import defaultdict, deque
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n <= 2: return [i for i in range(n)]
        def BFS(start, graph):
            visited = set()
            q = deque()
            visited.add(start)
            q.append(start)
            level = 0
            while q:
                level += 1
                for _ in range(len(q)):
                    root = q.popleft()
                    for v in graph[root]:
                        if v not in visited:
                            q.append(v)
                            visited.add(v)
            return level
        in_count = [0] * n
        gragh = defaultdict(list)
        minRes = n
        res = []
        for e in edges:
            gragh[e[0]].append(e[1])
            gragh[e[1]].append(e[0])
            in_count[e[0]] += 1
            in_count[e[1]] += 1
        for i in range(n):
            if in_count[i] == 1: continue
            cur = BFS(i, gragh)
            if cur == minRes:
                res.append(i)
            elif cur < minRes:
                minRes = cur
                res = [i]
        return res

'''
有些 case 没考虑到
只有两个点和只有一个点的被我剪枝掉了
'''

'''
哈哈哈， 然而超时了。。。
'''


'''
原来这个是拓扑排序的思路， 我已经想到了BFS剪枝， 但是其实只要看所有的入度然后留下一个或两个点就好
'''
from collections import defaultdict, deque
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n <= 2: return [i for i in range(n)]
        graph = defaultdict(list)
        in_count = [0] * n
        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
            in_count[e[0]] += 1
            in_count[e[1]] += 1
        q = deque()
        for i,num in enumerate(in_count):
            if num == 1:
                q.append(i)
        while n > 2:
            n -= len(q)
            for _ in range(len(q)):
                p = q.popleft()
                # print(graph[p])
                for v in graph[p]:
                    if in_count[v] > 1:
                        in_count[v] -= 1
                        if in_count[v] == 1:
                            q.append(v)
        return list(q)



a = Solution()
e = [[1,0],[1,2],[1,3]]
print(a.findMinHeightTrees(4, e))
# print( ''.join(map(chr, range(10000))))
# print(''.join(map(chr, range(256))))

