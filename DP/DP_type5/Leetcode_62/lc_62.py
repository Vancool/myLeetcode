class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

'''
https://leetcode-cn.com/problems/unique-paths/
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？


解法一、dp or 递归 
这个问题我本来用来练习dp

解法二、发现原来还可以用排列组合做
无论走哪条路都是 向右走 n-1 格，向下走 m-1 格， 区别在于在 m+n-2步中哪些步子是向下的哪些是向右的
因此 res = C(m+n-2, m-1)
'''
class Solution(object):
    def uniquePaths(self, m, n):
        if m > n:
            return self.uniquePaths(n, m)
        temp = 1
        for i in range(1,m):
            temp *= i
        res = 1
        for i in range(n, m+n-1):
            res *= i
        return res // temp

a = Solution()
print(a.uniquePaths(7,1))
print("Done")