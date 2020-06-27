# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        def copyNode(node):
            return Node(node.val)
        if node == None: return node
        visited = {}
        def dfs(node):
            new_node = copyNode(node)
            visited[node] = new_node
            for v in node.neighbors:
                if v not in visited:
                    dfs(v)
        dfs(node)
        for n,new_node  in visited.items():
            for v in n.neighbors:
                new_node.neighbors.append(visited[v])
        return visited[node]

'''
我自己写的DFS 多了一个不必要的循环(?)
'''
class Solution(object):
    def cloneGraph(self, node):
        if not node: return node
        visited = {}
        def dfs(node):
            if node in visited: return visited[node]
            visited[node] = Node(node.val)
            for v in node.neighbors:
                if v not in visited:
                    dfs(v)
                visited[node].neighbors.append(visited[v])
        dfs(node)
        return visited[node]

'''
BFS
'''
from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        if not node: return node
        visited = {}
        visited[node] = Node(node.val)
        Q = deque()
        Q.append(node)
        while Q:
            cur =  Q.popleft()
            for v in cur.neigbors:
                if v not in visited:
                    visited[v] = Node(v.val)
                    Q.append(v)
                visited[cur].neigbors.append(visited[v])
        return visited[node]
