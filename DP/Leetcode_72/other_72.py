class Solution(object):
    def minDistance(self, word1, word2):
        memohash = {}
        def Process(i, j):
            if (i,j) in memohash:
                return memohash[(i,j)]
            if i < 0:
                memohash[(i,j)] = j+1
                return j+1
            if j < 0:
                memohash[(i,j)] = i+1
                return i+1
            if word1[i] == word2[j]:
                res = Process(i-1, j-1)
            else:
                res = min(Process(i-1,j-1), Process(i, j-1), Process(i-1, j)) + 1
            memohash[(i,j)] = res
            return res
        return Process(len(word1)-1, len(word2)-1)

'''
从后往前走的递归 [从前往后其实也可以， 只是要用len(word) - index]
而且这样方便推dp
dp 解法：
'''
class Solution(object):
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        dp = [[float('inf')] * (n+1) for  _ in range(m+1) ]
        dp[0][0] = 0
        for i in range(1,m+1):
            dp[i][0] = i
        for j in range(1,n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
        return dp[m][n]




