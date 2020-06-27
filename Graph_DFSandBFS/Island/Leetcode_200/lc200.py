class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(i, j, grid):
            m, n = len(grid), len(grid[0])
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                grid[i][j]  = self.flag
                for step in direction:
                    di = i + step[0]
                    dj = j + step[1]
                    dfs(di, dj, grid)


        if len(grid) == 0:
            return 0
        self.flag = 1
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.flag += 1
                    dfs(i,j, grid)
        return self.flag - 1

'''
岛屿系列一，求连通分支个数
https://leetcode-cn.com/problems/number-of-islands/submissions/

'''

def getGrid(s):
    s = s.split()
    grid = []
    for i in range(len(s)):
        subArray = []
        for j in range(len(s[0])):
            subArray.append(int(s[i][j]))
        grid.append(subArray)
    return grid


a = Solution()
nums = '11000 11000 00100 00011'
grid = getGrid(nums)
print(grid)
print(a.numIslands(grid))
print("Done")
