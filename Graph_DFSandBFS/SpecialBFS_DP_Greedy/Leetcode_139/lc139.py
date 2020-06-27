class Solution(object):
    def wordBreak(self, s, wordDict):
        if len(s) * len(wordDict) == 0:
            return False
        dp = [-1] * (len(s) + 1)
        for i in range(1,len(dp)):
            cur = dp[i-1]
            while cur != -1:
                if s[cur: i] in wordDict:
                    dp[i] = i
                    break
                else:
                    cur = dp[cur-1]
            if cur == -1:
                if s[0:i] in wordDict:
                    dp[i] = i
                else:
                    dp[i] = dp[i-1]
        return dp[-1] == len(s)
'''
解法BFS写法
'''
from collections import deque
class Solution1(object):
    def wordBreak(self, s, wordDict):
        if len(s) * len(wordDict) == 0:
            return False
        visited = set()
        queue = deque()
        visited.add(0)
        queue.append(0)
        while queue:
            start = queue.popleft()
            '''广搜的两种策略. 如果字典小按字典搜，如果字符串长度小就按字符串长度搜'''
            if len(wordDict) < len(s):
                searchDict = [start + len(key) for key in wordDict]
            else:
                searchDict = [end for end in range(start+ 1,len(s)+1)]
            for end in searchDict:
                if end <= len(s) and s[start: end] in wordDict and end not in visited:
                    '''注意这边如果不写 end not in visited 算法就会退化为递归'''
                    if end == len(s): return True
                    queue.append(end)
                    visited.add(end)
        return False


'''
DFS -> DP 
false / true 写法
'''
class Solution(object):
    def wordBreak(self, s, wordDict):
        if len(s) * len(wordDict) == 0:
            return False
        dp = [False] * (len(s)+1)
        dp[-1] = True #哨兵
        for i in range(len(s)-2,-1,-1):
            for j in range(i+1, len(dp)):
                if s[i:j] in wordDict and s[j] == True:
                    s[i] = True
                    break
        return dp[0]

'''
在一维数组中，BFS的转化DP
BFS和DP的条件都是一步一步走，之前走过的路不会影响以后的决策的算法。
其实就是父亲不知道怎么处理多个儿子，那么从儿子找父亲来处理，儿子是确定的，只要看看它有没有父亲就好
BFS是数组从前往后儿子找父亲
DFS是数组从后往前儿子找父亲[这一题从前往后和从后往前都可]
到底什么时候用BFS什么时候用DP?
如果边界能够确定数组相邻两个元素是否可达，用DP
如果数组元素需要通过往前看或者继续往后找完整个数组，用BFS
'''
a = Solution1()
s = "a"
wordDict = ["a"]
print(a.wordBreak(s, wordDict))
print("Done")