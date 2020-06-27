'''
自己写的，写错的
'''
'''
class Solution(object):
    def bfs(selfs,graph, visited, queue, res):
        v = queue[0]
        temp = graph[v].next
        while temp is not None:
            if visited[temp.data]==0:
                visited[temp.data] = 1
                res.append(temp.data)
                queue.append(temp.data)

            temp = temp.next
        queue.pop(0)


    def dfs(self, v,graph, visited, stack, res):
        if(len(stack) == 0):
            return
        else:
            temp = graph[v].next
            while temp is not None:
                if(visited[temp.data]==0):
                    visited[temp.data] = 1
                    res.append(temp.data)
                    stack.append(temp.data)
                    self.dfs(temp.data, graph, visited, stack, res)
                temp = temp.next
            stack.pop()

    def backOrder(self, v, graph, visited, res):
        temp = graph[v].next
        while temp is not None:
            if visited[temp.data] == 0:
                visited[temp.data] = 1
                self.backOrder(temp.data, graph, visited, res)
            temp = temp.next
        res.append(v)


    def findOrder(self, numCourses, prerequisites): #2, [[1,0]]
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if numCourses==0:
            return []
        if numCourses <= 2:
            return sorted(prerequisites[0])
        graph =[]
        count_in = [0]*numCourses
        visited = [0]*numCourses
        res = []
        queue = []
        for i in range(numCourses):
            graph.append(Node(i))
        for i in range(len(prerequisites)):
            inV = prerequisites[i][1]
            outV = prerequisites[i][0]
            if graph[inV].next is None:
                graph[inV].next = Node(outV)
            else:
                temp = graph[inV].next
                graph[inV].next = Node(outV, temp)
            count_in[outV] += 1
        for i in range(numCourses):
            if count_in[i] == 0 and visited[i] == 0:
                visited[i] = 1
                self.backOrder(i,graph, visited, res)
        res.reverse()
        print(res)

'''

from collections import defaultdict
class Solution(object):
    def dfs(self,v, graph,  color, res):
        color[v] = 1
        if v in graph:
            for neibor in graph[v]:
                if color[neibor] == 2:
                    continue
                elif color[neibor] == 0 and self.dfs(neibor, graph, color, res):
                    continue
                else:
                    return False
        res.append(v)
        color[v] = 2
        return True
    def findOrder(self, numCourses, prerequisites):  # 2, [[1,0]]
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if numCourses == 0 :
            return []
        if len(prerequisites) == 0:
            return range(numCourses)
        if len(prerequisites) == 1:
            if prerequisites[0][0] > prerequisites[0][1]:
                return [i for i in range(numCourses)]
            else:
                res = [i for i in range(numCourses)]
                res[prerequisites[0][0]] =  prerequisites[0][1]
                res[prerequisites[0][1]] =  prerequisites[0][0]
                return res
        #create graph using dict
        graph = defaultdict(list)
        res = []
        color = [0] * numCourses
        for outV, inV in prerequisites:
            graph[inV].append(outV)
        for i in range(numCourses):
            if color[i] == 0:
                if not self.dfs(i,graph, color,res):
                    return []
        return res[::-1]

if __name__ == "__main__":
    a = Solution()
    res = a.findOrder(2, [[0,1],[1,0]])
    print(res)



