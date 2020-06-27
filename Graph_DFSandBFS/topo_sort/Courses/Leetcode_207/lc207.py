class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        if numCourses < 2 or len(prerequisites) < 2:
            return True
        indegree =[0] * numCourses
        graph = [[] for i in range(numCourses)]
        for item in prerequisites:
            indegree[item[1]] += 1
            graph[item[0]].append(item[1])
        taken = set()
        flag = True
        while len(taken) < numCourses and flag:
            flag = False
            for i in range(numCourses):
                if i not in taken and indegree[i] == 0:
                    flag = True
                    taken.add(i)
                    for p in graph[i]:
                        indegree[p] -= 1
                    break
        return flag

'''
自己的这种写法不好，时间复杂度是 O(n^2), 因为每次都要遍历所有的

可以一开始遍历一遍，然后用一个队列存着入度为0的数组
'''



a = Solution()
n = 3
g = [[1,0],[2,0]]
print(a.canFinish(n,g))


