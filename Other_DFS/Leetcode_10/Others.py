from collections import deque
'''
1.如果后面的东西和前面的东西有关系，先考虑从后往前循环再考虑栈操作
2.如果有很多种选择不能一次循环完，用dfs
3. dfs 和 dp 其实是一种转换，后面是根据长度来进行转换的，大家的复杂度都是O(mn)
'''
class Solution(object):
    def isMatch(self, s, p):

        m = len(s)
        n = len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for xi in range(m+1):
            for xj in range(n+1):
                i = xi-1
                j = xj-1
                if j>=0 :
                    if p[j] == '*'and j>=1:
                        if i<0 or (s[i] != p[j-1] and p[j-1]!= '.'):
                            ''' 这个地方要注意当s取长度为0的时候可能P是可以为 x*x*一类的
                            需要求s如果后面是 xxxxa* 说明s只和xxxx(前j-2位)匹配  '''
                            dp[xi][xj] = dp[xi][xj-2]
                        else:
                            '''s要么和xxxx匹配要么和xxxxa匹配/ 要么没有，要么有一个'''
                            dp[xi][xj] = dp[xi][xj-2] or dp[xi-1][xj]
                    if i >= 0 and (s[i] == p[j] or p[j]=='.'):
                        dp[xi][xj] = dp[xi-1][xj-1]
                        '''当相同的时候只要前面相同就可以移动'''
        return dp[m][n]

a = Solution()
s = ""
p = "."
print(a.isMatch(s,p))
print("Done")