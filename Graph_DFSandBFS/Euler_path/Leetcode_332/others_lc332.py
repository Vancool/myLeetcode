from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        def dfs(start):
            for v in graph[start]:
                if visited[(start, v)] > 0:
                    visited[start, v] -= 1
                    dfs(v)
            self.res = [start] + self.res
            #ans.insert(0, f)
            # 也可以改成 self.res.append(start)
            # 最后搞个 return res[::-1] 就好


        if not tickets: return tickets
        tickets.sort(key=lambda t:t[0])
        graph = defaultdict(list)
        visited = {}
        self.res = []
        for x, y in tickets:
            graph[x].append(y)
            visited[(x,y)] = visited.get((x,y), 0) + 1
        dfs("JFK")
        return self.res

'''
要注意同一条边走两次的情况：
这个题不是一个简单图
[["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]

可以用 graph pop的方法去除边，这样就可以不用哈希表记录重复了
'''

# 暴力搜索， 同样是dfs只要要递归到底
from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        def dfs(start, path):
            if len(path) == len(tickets) + 1:
                self.res = path
            if self.res:
                return
            for v in graph[start]:
                if visited[(start, v)] > 0:
                    visited[start, v] -= 1
                    dfs(v, path + [v])
                    visited[(start, v)] += 1 # 搜索要状态还原

        if not tickets: return tickets
        graph = defaultdict(list)
        visited = {}
        self.res = []
        for x, y in tickets:
            graph[x].append(y)
            visited[(x,y)] = visited.get((x,y), 0) + 1
        for f in graph:
            graph[f].sort()
        dfs("JFK",["JFK"])
        return self.res


a = Solution()
ticket = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print(a.findItinerary(ticket))


