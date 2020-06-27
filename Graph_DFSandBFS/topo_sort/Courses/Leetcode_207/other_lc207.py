from collections import deque
'''
解法一： BFS 用队列存入度为0的点， 这样就不用每次都遍历一次了
'''
class Solution1(object):
    def canFinish(self, numCourses, prerequisites):
        if len(prerequisites) < 2 or numCourses < 2: return True
        if numCourses*(numCourses-1)//2 < len(prerequisites): return False
        '''此处为了防止重复输入边用set, 其实如果有说明用list也可以'''
        graph = [set() for _ in range(numCourses)]
        zeroqueue = deque()
        inDegree = [0] * numCourses
        for item in prerequisites:
            graph[item[0]].add(item[1])
            inDegree[item[1]] += 1
        for i in range(numCourses):
            if inDegree[i] == 0:
                zeroqueue.append(i)
        while zeroqueue:
            start = zeroqueue.popleft()
            numCourses -= 1
            for end in graph[start]:
                inDegree[end] -= 1
                if inDegree[end] == 0:
                    zeroqueue.append(end)
        return numCourses == 0

'''
解法二. DFS 如果碰到了正在访问，就向上回溯return False, 说明当前有圈
'''

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        def dfs(start):
            if status[start] == 2: return True
            if status[start] == 1: return False
            status[start] = 1
            for end in graph[start]:
                if not dfs(end):
                    return False
            status[start] = 2
            return True

        if len(prerequisites) < 2 or numCourses < 2: return True
        if numCourses*(numCourses-1)//2 < len(prerequisites): return False
        '''此处为了防止重复输入边用set, 其实如果有说明用list也可以'''
        graph = [set() for _ in range(numCourses)]
        status = [0] * numCourses
        for item in prerequisites:
            graph[item[0]].add(item[1])
        for i in range(numCourses):
            if not dfs(i): return False
        return True

a = Solution()
n = 3
g = [[1,0],[2,0]]
print(a.canFinish(n,g))