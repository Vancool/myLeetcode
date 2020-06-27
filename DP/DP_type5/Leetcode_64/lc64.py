class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]
'''
dp的空间优化，用一维数组来代替二维
（因为其实是从左到右从上到下的，所以只用存着从左到右的顺便用之前的就好了）
'''
class Solution2(object):
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0] = grid[0][0]
                elif i == 0:
                    dp[j] = dp[j-1] + grid[i][j]
                elif j == 0:
                    dp[j] += grid[i][j]
                else:
                    dp[j] = grid[i][j] + min(dp[j], dp[j-1])
        return dp[n-1]

a = Solution2()
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(a.minPathSum(grid))
print("Done")

'''
这题用于练习dp的
但是也可以用DFS深搜来做
但是用DFS的话栈内存会爆掉，因为它是遍历了所有路径的方法 时间复杂度为O(2**(m+n))

'''
class Solution3(object):
    def minPathSum(self, grid):
        direction = {[1,0],[0,1]}
        m = len(grid)
        n = len(grid[0])
        self.res = float('inf')
        def dfs(i, j, preSum):
            if i == m-1 and j == n-1:
                self.res = min(preSum, self.res)
                return
            for step in direction:
                di = i + step[0]
                dj = j + step[1]
                if di <= m-1 and dj <= n-1:
                    dfs(di, dj, preSum + grid[di][dj])
        dfs(0,0, grid[0][0])
        return self.res


