from collections import deque
class Solution1(object):
    def findOrder(self, numCourses, prerequisites):
        if numCourses < 2 or len(prerequisites) == 0: return [i for i in range(numCourses)]
        if numCourses*(numCourses-1)//2 < len(prerequisites): return []
        inDegree = [0] * numCourses
        zeroqueue = deque()
        graph = [set() for _ in range(numCourses)]
        for item in prerequisites:
            graph[item[1]].add(item[0])
            inDegree[item[0]] += 1
        res = []
        for i in range(numCourses):
            if inDegree[i] == 0:
                zeroqueue.append(i)
        while zeroqueue:
            start = zeroqueue.popleft()
            res.append(start)
            for end in graph[start]:
                inDegree[end] -= 1
                if inDegree[end] == 0:
                    zeroqueue.append(end)
        if len(res) == numCourses: return res
        return []

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        def dfs(start):
            if status[start] == 2:
                return True
            if status[start] == 1:
                return False
            status[start] = 1
            for end in graph[start]:
                if not dfs(end): return False
            status[start] = 2
            res.append(start)
            return True
        if numCourses < 2 or len(prerequisites) == 0: return [i for i in range(numCourses)]
        if numCourses*(numCourses-1)//2 < len(prerequisites): return []
        graph = [set() for _ in range(numCourses)]
        status = [0] * numCourses
        res = []
        for item in prerequisites:
            graph[item[1]].add(item[0])
        for i in range(numCourses):
            if not dfs(i): return []
        '''
        这边也可以用逆邻接链表， 就不用最后反序输出了
        '''
        return res[::-1]



a = Solution()
n = 4
course = [[1,0],[2,0],[3,1],[3,2]]
print(a.findOrder(n, course))
print("Done")

