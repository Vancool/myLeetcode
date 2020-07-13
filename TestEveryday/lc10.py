class Solution(object):
    def isMatch(self, s, p):
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]

        for i in range(len(s)+1):
            for j in range(len(p)+1):
                if i == 0:
                    if i == 0 and j == 0:
                        dp[i][j] = True
                    elif p[j-1] == "*":
                        dp[i][j] = dp[i][j-2]
                else:
                    if j == 0: continue
                    if s[i-1] == p[j-1] or p[j-1]=="." :
                        dp[i][j] = dp[i-1][j-1]
                    elif p[j-1] == "*":
                        if p[j-2] == "." or p[j-2] == s[i-1]:
                            dp[i][j] = (dp[i][j-2] or dp[i-1][j-2] or dp[i-1][j-1] or dp[i][j-1])
                        else:
                            dp[i][j] = dp[i][j-2]
        return dp[len(s)][len(p)]
s = "aaa"
p = ".*"
a = Solution()
print(a.isMatch(s,p))