class Solution(object):
    def isMatch(self, s, p):
        if not p: return not s
        dp = [[False]*(len(s)+1) for _ in range(len(p)+1)]
        for i in range(len(p)+1):
            for j in range(len(s)+1):
                if i== 0 and j == 0:
                    dp[i][j] = True
                if i > 0 and p[i-1] == '*':
                    dp[i][j] =  dp[i-1][j] or(j> 0 and (dp[i][j-1] or dp[i-1][j-1]))
                elif i > 0 and j > 0:
                    if p[i-1] == s[j-1] or p[i-1] == '?':
                        dp[i][j] = dp[i-1][j-1]
        return dp[len(p)][len(s)]


a = Solution()
s = "mississippi"
p = "m??*ss*?i*pi"
print(a.isMatch(s,p))
