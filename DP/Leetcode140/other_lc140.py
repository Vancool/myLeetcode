from collections import defaultdict
class Solution(object):
    def wordBreak(self, s, wordDict):
        dict  = set(wordDict)
        dp = [[] for _ in range(len(s) + 1)]
        dp[0].append("")
        for i in range(1,len(dp)):
            for j in range(i+1):
                if len(dp[j]) > 0 and s[j:i] in dict:
                    for str in dp[j]:
                        if str == "":
                            dp[i].append(s[j:i])
                        else:
                            dp[i].append(str + " " + s[j: i])
        return dp[-1]
'''
解法一. 记忆递归
解法二. dp
dp[i] 表示在下标i之前s[0:i] 所能产生的所有分割
'''
a = Solution()
s = "catsanddog"
d = ["cat","cats","and","sand","dog"]
print(a.wordBreak(s, d))
print("Done")