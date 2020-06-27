class Solution(object):
    def numDecodings(self, s):
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(s)+1):
            if i >= 2 and '10' <= s[i-2: i] < '27':
                if s[i-1] == '0':
                    dp[i] = dp[i-2]
                else:
                    dp[i] = dp[i-1] + dp[i-2]
            elif '0' < s[i-1] <= '9':
                dp[i] = dp[i-1]
            else:
                return 0
        return dp[len(s)]
'''
注意： 这个题目没有说编码的字符串到底规不规范
因此可能会出现 0 

如果从前往后写可能会碰到这个test case 要注意：
test case: 10 20 只能两个一起
字符串题： 如果0 和 10 要分成两种情况，10又可以拆开，要注意10这个分支的写法
'''

'''
可以空间优化
从后往前走的解法：
把0那条路单拎出来也算一条路
'''
class Solution(object):
    def numDecodings(self, s):
        if len(s) == 0: return 1
        pre = 1
        cur = 0 if s[-1] == '0' else 1
        for i in range(len(s)-2, -1,-1):
            if s[i] == '0':
                pre = cur
                cur = 0
            else:
                one_digit_count = cur
                two_digit_count = 0
                twodigit = (ord(s[i])- ord('0')) * 10 + (ord(s[i+1]) - ord('0'))
                if 10 <= twodigit <= 26:
                    two_digit_count = pre
                pre = cur
                cur = one_digit_count + two_digit_count
        return cur
a = Solution()
s = "226"
print(a.numDecodings(s))
