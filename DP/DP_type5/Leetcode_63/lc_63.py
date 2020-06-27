class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j-1] if obstacleGrid[i][j-1] == 0 else 0
                elif j == 0:
                    dp[i][j] = dp[i-1][j] if obstacleGrid[i-1][j] == 0 else 0
                else:
                    dp[i][j] += dp[i][j - 1] if obstacleGrid[i][j - 1] == 0 else 0
                    dp[i][j] += dp[i - 1][j] if obstacleGrid[i - 1][j] == 0 else 0
        return dp[m-1][n-1]


a = Solution()
graph = [[0,0,0],
         [0,1,0],
         [0,0,0]]
print(a.uniquePathsWithObstacles(graph))
print("Done")