class Solution(object):
    def longestValidParentheses(self, s):
        if s == None or len(s) == 0 or len(s) == 1:
            return 0
        stack = []
        res = 0
        s = "#" + s + "#" # 哨兵
        for i in range(len(s)):
            if s[i] == ")":
                if len(stack) > 0 and s[stack[-1]] == "(":
                    stack.pop()
                    continue
            stack.append(i)
        cur = stack.pop()
        while len(stack) > 0:
            before = stack.pop()
            res = max(res, cur - before - 1)
            cur = before
        return res
'''
我觉得自己的栈解法最好
不接受反驳。
其实还可以用dp 和 左右扫描(特殊解法) 来解
'''
'''
解法一.左右扫描
左右扫描其实是栈的特殊解法 其实就是两个局部最优解得出全局最优解，而与两边相关（or栈相关）的题目很适合这种解法，因为可以从两边扫描
为什么呢？ 是因为我们求有效括号要统计的是左右两边
比如
从左往右 可以统计类似于由过多右括号导致无效的有效括号长
从右往左 可以统计类似于由过多左括号导致无效的有效括号长
而这两个合起来就是 统计 最大有效括号长

注意这个 test case: "()(()" 因此我们只算刚刚好 left == right 的，不然只算left 或者right 中间被间隔了一个都不知道
'''
class Solution(object):
    def longestValidParentheses(self, s):
        if s == None or len(s) == 0 or len(s) == 1:
            return 0
        res = 0
        left = 0
        right = 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1
                if left == right:
                    res = max(res, right * 2)
                elif left < right:
                    left = 0
                    right = 0
        if res == len(s): return res
        left = 0
        right = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == ")":
                right += 1
            else:
                left += 1
                if left == right:
                    res = max(res, left * 2)
                elif left > right:
                    left = 0
                    right = 0
        return res


'''DP 解法
这个人讲得比较好:https://leetcode-cn.com/problems/longest-valid-parentheses/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-7/
'''
class Solution1(object):
    def longestValidParentheses(self, s):
        if s == None or len(s) == 0 or len(s) == 1:
            return 0
        dp = [0] * len(s)
        res = 0
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = dp[i-2] + 2 if i-2 >= 0  else 2
                elif s[i-1] == ")":
                    preleft = i - 1 - dp[i-1]
                    if preleft >= 0 and s[preleft] == "(":
                        dp[i] = 2 + dp[i-1]
                        if preleft - 1 >= 0:
                            dp[i] += dp[preleft-1]
                res = max(res, dp[i])
        return res


a = Solution1()
s = ")(()(()()(((()))"
print(a.longestValidParentheses(s))
print("Done")


