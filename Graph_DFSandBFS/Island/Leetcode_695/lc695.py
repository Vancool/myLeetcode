class Solution(object):
    def maxAreaOfIsland(self, grid):
        m,n = len(grid), len(grid[0])
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        self.res = 0
        def dfs( i, j, grid):
            tmp = 0
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                tmp += 1
                grid[i][j] = -1
                for step in direction:
                    di = i + step[0]
                    dj = j + step[1]
                    tmp += dfs(di, dj, grid)
            return tmp

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    tmp_res = dfs(i,j,grid)
                    self.res = max(self.res, tmp_res)
        return self.res
'''
岛屿系列二.依旧训练dfs
https://leetcode-cn.com/problems/max-area-of-island/

如何不用递归来做面积搜索：
用栈 or 队列 代替递归 
'''

class Solution(object):
    def maxAreaOfIsland(self, grid):
        m,n = len(grid), len(grid[0])
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        stack = []
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cur = 0
                    stack.append((i,j))
                    while stack:
                        start = stack.pop()
                        grid[start[0]][start[1]] = 0
                        cur += 1
                        for step in direction:
                            dx = start[0] + step[0]
                            dy = start[1] + step[1]
                            if 0 <= dx < m and 0<= dy < n and grid[dx][dy] == 1:
                                stack.append((dx, dy))
                    res = max(res, cur)
        return res




a = Solution()
area = [[0,0,0,0,0,0,0,0]]

print(a.maxAreaOfIsland(area))
print("Done")