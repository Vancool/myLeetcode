class Solution(object):
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        if m*n == 0:
            return 0
        # getIndex 的方法是和 UnionFind 一起用的，因为它定义了一个一维数组来表示parent
        def getIndex(i,j):
            return i * n + j
        class UnionFind():
            self.num = 0
            def __init__(self, n):
                self.num = n
                self.parent = [ i for i in range(n)]
                self.rank = [1 for _ in range(n)]
                # rank 数组是用来标识大树还是小树的，为了并查集的效率尽可能的把小树并到大树上面
            def find(self, p):
                while p!= self.parent[p]:
                    self.parent[p] = self.parent[self.parent[p]] #把查找的层数减小
                    p = self.parent[p]
                return p
            def is_connected(self,p,q):
                return self.find(p) == self.find(q)
            def union(self, p,q):
                p_root = self.find(p)
                q_root = self.find(q)
                if p_root == q_root:
                    return
                if self.rank[p_root] > self.rank[q_root]:
                    self.parent[q_root] = p_root
                    self.rank[p_root] += self.rank[q_root]
                else:
                    self.parent[p_root] = q_root
                    self.rank[q_root] += self.rank[p_root]
                self.num -= 1
                #只要union了就会减少一个独立的连通分支
        num = n*m + 1
        #为社么加一？ 因为有一个集合是表示水域，我们这边设置矩形之外还有一个格子是水域
        # 因此碰到'0'表示水域的时候总是会与这个虚假的水域 n*m+1这个格子合并成集合
        uf = UnionFind(num)
        direction = [(1,0),(0,1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    uf.union(getIndex(i,j), n*m)
                if grid[i][j] == '1':
                    for step in direction:
                        di = i + step[0]
                        dj = j + step[1]
                        if di < m and dj < n and grid[di][dj] == '1':
                            #因为不会往回找，按顺序来找所以不会出现循环无法退出的情况
                            uf.union(getIndex(i,j), getIndex(di,dj))
        return uf.num - 1

if __name__ == '__main__':
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    solution = Solution()
    result = solution.numIslands(grid)
    print(result)


'''
share from:
https://leetcode-cn.com/problems/number-of-islands/solution/dfs-bfs-bing-cha-ji-python-dai-ma-java-dai-ma-by-l/
实际上岛屿问题用dfs做是刚刚好的
只是也可以用并查集来做【求连通分支】
所以写一下防止自己以后被问到不会写，其实还是用DFS做吧2333
'''