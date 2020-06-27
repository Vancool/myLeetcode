class Solution(object):
    def partition(self, s):
        if len(s) <= 1: return [[s]]
        memohash = {}
        for key in s:
            memohash[key] = [[key]]
        def isValid(s, left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        def process(s):
            if s in memohash:
                return memohash[s]
            res = []
            left = 0
            right = len(s)
            for i in range(left, right):
                if isValid(s, left, i):
                    if i == right - 1:
                        res.append([s[left: i + 1]])
                        break
                    subreslist = process(s[i + 1: right])
                    for subres in subreslist:
                        res.append([s[left: i + 1]] + subres)
            memohash[s] = res
            return res

        return process(s)
'''
我自己的话是使用记忆递归来做的
比较多人使用的是dp + dfs 来做
但是我认为没差，因为大家的时间复杂度都是 O(n^2)
'''

class Solution(object):
    def partition(self, s):
        if len(s) <= 1: return [[s]]
        dp = [[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i+1):
                if s[i] == s[j] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True #这个地方要注意是 dp[j][i]
        res = []
        def dfs(start, path):
            if start == len(s):
                res.append(path[:])
                return
            for i in range(start, len(s)):
                if dp[start][i]:
                    dfs(i+1, path + [s[start:i+1]])
        dfs(0, [])
        return res


class Solution(object):
    def partition(self, s):
        if len(s) <= 1: return [[s]]
        memohash = {}
        if len(s) <= 1: return [[s]]
        dp = [[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i+1):
                if s[i] == s[j] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True #这个地方要注意是 dp[j][i]
        for key in s:
            memohash[key] = [[key]]
        def process(left, right):
            if s[left:right+1] in memohash:
                return memohash[s[left:right+1]]
            res = []
            for i in range(left, right+1):
                if dp[left][i]:
                    if i == right:
                        res.append([s[left: i + 1]])
                        break
                    subreslist = process(i+1, right)
                    for subres in subreslist:
                        res.append([s[left: i + 1]] + subres)
            memohash[s[left:right+1]] = res
            return res

        return process(0, len(s)-1)

a = Solution()
s = "aa"
print(a.partition(s))
