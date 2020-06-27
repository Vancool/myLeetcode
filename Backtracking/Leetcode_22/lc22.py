class Solution1(object):
    def generateParenthesis(self, n):
        if n == 0: return []
        preParenthesis = set("()")
        for i in range(2,n+1):
            cur = set()
            for pre in preParenthesis:
                cur.add("(" +  pre + ")")
                if pre[0:2] != "()":
                    cur.add(pre + "()")
                cur.add("()" + pre)
                for i in range(len(pre)):
                    if pre[i] == "(":
                        cur.add(pre[0:i+1] + "()" + pre[i+1: len(pre)])
            preParenthesis = set(cur)
        return list(preParenthesis)
'''
https://leetcode-cn.com/problems/generate-parentheses/
我自己使用的是dp , 用的是生成多一个括号放在哪里的想法， 但是每次都要用一个set 很麻烦

题解中另一种dp是这样的：
第i组的每个括号的形式是： (a)b   a是包含a个括号的形式， b是包含b个括号的形式，a+b = i-1 ， a 和 b可以是空
就变成了不是考虑多一个括号放哪里，而是考虑两个位置放什么
不会有重复，因为 左边是 a+1 个括号的形式 ， 右边是 b 个括号的形式， 是组合问题
'''
class Solution(object):
    def generateParenthesis(self, n):
        if n == 0: return []
        dp = [[] for _ in range(n+1)]
        dp[0] = [""]
        dp[1] = ["()"]
        for i in range(2, n+1):
            for j in range(i):
                for left in dp[j]:
                    for right in dp[i-1-j]:
                        dp[i].append("("+left+")"+right)
                        '''
                    官方题解这么写：
                    ans.append('({}){}'.format(left, right))
                        '''
        return dp[n]

'''
这题可以用 回溯来做
详情见 other
'''
a = Solution()
print(a.generateParenthesis(3))
print("Done")

