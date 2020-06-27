class Solution(object):
    def findRedundantConnection(self, edges):
        n = len(edges)
        res = []
        hashmap = [0] * (n+1)
        for e in edges:
            if hashmap[e[0]] and hashmap[e[1]]:
                res = e
            hashmap[e[0]] = 1
            hashmap[e[1]] = 1
        return res

'''
这个解法不对， 没有考虑多个连通分支的情况
'''


'''
这题最好的方法是使用 union-find 并查集
'''

class Solution(object):
    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = [-1] * (n+1)
        def find(p):
            if parent[p] > 0:
                pre = find(parent[p])
                parent[p] = pre
                return pre
            return p
        def union(set1, set2):
            if -parent[set1] > -parent[set2]:
                parent[set2] = set1
            else:
                parent[set1] = set2

        for e in edges:
            set1 = find(e[0])
            set2 = find(e[1])
            if set1 != set2:
                union(set1, set2)
            else:
                return e






a = Solution()
e = [[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]

print(a.findRedundantConnection(e))