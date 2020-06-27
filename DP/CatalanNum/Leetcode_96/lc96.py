class Solution1(object):
    def numTrees(self, n):
        if n < 1: return 0
        if n == 1: return 1
        memoMap = {}
        memoMap[1] = 1
        memoMap[0] = 1
        def Process(n):
            if n in memoMap:
                return memoMap[n]
            res = 0
            for i in range(n//2):
                res += 2 * Process(i) * Process(n-i-1)
            if n & 1 == 1:
                res += Process(n//2)**2

            memoMap[n] = res
            return res
        return Process(n)
'''
自己的解法一. 记忆递归
自己的解法二. dp
'''
class Solution(object):
    def numTrees(self, n):
        if n < 1: return 0
        if n == 1: return 1
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(0,i):
                dp[i] += dp[j] * dp[i-1-j]
        return dp[n]
a = Solution()
print(a.numTrees(5))
print("Done")