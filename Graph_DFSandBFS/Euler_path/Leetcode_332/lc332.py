from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        def dfs(f):
            if len(res) == len(all_pos): return True
            for to in graph[f]:
                if to in hasVisited: continue
                hasVisited.add(to)
                res.append(to)
                if dfs(to):
                    return True
                hasVisited.remove(to)
                res.pop(to)
            return False

        if not tickets: return []
        hasVisited = set()
        graph = defaultdict(list)
        all_pos = set()
        for f in tickets:
            graph[f[0]].append(f[1])
            all_pos.add(f[1])
            all_pos.add(f[0])
        for key in graph.keys():
            graph[key].sort()
        res = ["JFK"]
        all_pos.add("JFK")
        hasVisited.add("JFK")
        for to in graph["JFK"]:
            res.append(to)
            hasVisited.add(to)
            if dfs(to):
                return res
            res.pop(to)
            hasVisited.remove(to)
        return []

'''
这题想错了, 原来是对边的dfs
'''
class Solution(object):
    def findItinerary(self, tickets):
        def dfs(start):
            if len(res) == len(tickets): return True
            for v in sorted(graph[start]):
                if v not in visited:
                    visited.add(v)
                    res.append(v)
                    if dfs(v):
                        return True
                    visited.remove(v)
                    res.pop()
            return False
        if not tickets: return []
        if len(tickets) <= 1: return tickets[0]
        tickets.sort(key=lambda t:t[0])
        graph = defaultdict(list)
        s = []
        visited = set()
        for i in range(len(tickets)):
            if tickets[i][0] == 'JFK':
                s.append(i)
            for j in range(len(tickets)):
                if tickets[i][1] == tickets[j][0]:
                    graph[i].append(j)
        s.sort(key=lambda t:tickets[t][1])
        res = []
        for start in s:
            visited.add(start)
            res.append(start)
            for v in graph[start]:
                visited.add(v)
                '''
                这里出错了， 我应该 visited add 边， 而且边会有重复所以不能用set()
                '''
                res.append(v)
                if dfs(v):
                    final_res=  [tickets[i][0] for i in res]
                    final_res.append(tickets[res[-1]][1])
                    return final_res
                visited.remove(v)
                res.pop()
            visited.remove(start)
            res.pop(start)


'''
边界： 只有一个点的要预先判断一下。
这一题不会做， 其实是求 欧拉路径 的题
'''

a = Solution()
ticket = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print(a.findItinerary(ticket))