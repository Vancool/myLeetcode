class Solution(object):
    def minCut(self, s):
        if len(s) <= 1: return 0
        hashmap = {}
        dp = [[False] * len(s) for _ in range(len(s))]
        for right in range(len(s)):
            for left in range(right+1):
                dp[left][right] = (s[left] == s[right]) and (right - left <= 2 or dp[left+1][right-1])
        def process(left, right):
            if dp[left][right]: return 0
            if s[left: right+1] in hashmap:
                return hashmap[s[left:right+1]]
            count = float("inf")
            for i in range(right+1):
                if dp[left][i]:
                    cur = process(i+1, right) + 1
                    count = min(cur, count)
                    if count == 1: break
            hashmap[s[left:right + 1]] = count
            return count
        res = process(0, len(s)-1)
        return res

'''
尝试1： 超时
'''
from collections import defaultdict
class Solution(object):
    def minCut(self, s):
        if len(s) <= 1: return 0
        dp = [ set() for _ in range(len(s))]
        for right in range(len(s)):
            for left in range(right+1):
                if (s[left] == s[right]) and (right - left <= 2 or right-1 in dp[left+1]):
                    dp[left].add(right)
        def process(left, right):
            if right in dp[left]: return 0

            count = float("inf")
            for i in dp[left]:
                cur = process(i+1, right) + 1
                count = min(count, cur)
                if count == 1: break
            return count
        res = process(0, len(s)-1)
        return res

'''
尝试2： 过了一个样例， 还是超时
'''
'''
原来是要用dp，详情请见others
两种写dp的方式
'''
a = Solution()
print(a.minCut("fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"))