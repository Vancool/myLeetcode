class Solution(object):
    def findRedundantDirectedConnection(self, edges):
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

'''
上面那个是684的写法
这题和684求图的那题不同的是，它求的是一棵树，要保证最后出的是一棵树
与图不同的地方在于： 图是去掉一个边使得它没有圈
而这个不仅仅可能会 有圈， 也可能有 不含圈的有两个父亲的孩子，所以单单dfs或者并查集找圈肯定不行
对于有两个父亲的孩子，如果有圈，删除在圈里的那条边， 如果没有圈， 则随便删哪条都行（其实是删后面遇到的那条
注意这题不能用路径压缩
'''
class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        def find(p):
            while parent[p] > 0:p = parent[p]
            return p
        def union(set1, set2):
            if set1 == set2: return
            if -parent[set1] > -parent[set2]:
                parent[set2] = set1
            else:
                parent[set1] = set2
        hasParent = {}
        parent = [-1] * (len(edges)+1)
        hasCircle = None
        candidate = []
        for e in edges:
            if e[1] not in hasParent:
                hasParent[e[1]] = e[0]
                set1 = find(e[1])
                set2 = find(e[2])
                if set1 == set2:
                    hasCircle = e
                union(set1, set2)
            else:
                candidate.append((hasParent[e[1]], e[1]))
                candidate.append(e)
        if not candidate:
            return hasCircle
        return candidate[0] if hasCircle else candidate[1]




