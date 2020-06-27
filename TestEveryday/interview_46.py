class Solution(object):
    def translateNum(self, num):
        num = str(num)
        dp = [0] * (len(num) + 1)
        dp[-1] = 1
        dp[-2] = 1
        for i in range(len(num) - 2,-1,-1):
            if "10" <= num[i]+num[i+1] <= "25":
                dp[i] = dp[i+1] + dp[i+2]
            else:
                dp[i] = dp[i+1]
        return dp[0]

class Solution(object):
    def translateNum(self, num):
        num = str(num)
        pre, cur = 1, 1
        for i in range(len(num)-2, -1, -1):
            if "10" <= num[i]+num[i+1] <= "25":
                tmp = cur
                cur = pre + cur
                pre = tmp
            else:
                cur = pre
        return cur

'''
不用构造字符串的解法
'''

class Solution(object):
    def translateNum(self, num):
        pre, cur = 1,1
        x = num % 10
        while num:
            num = num // 10
            y = num % 10
            if 10 <= x + y * 10 <= 25:
                tmp = pre + cur
                pre = cur
                cur = tmp
            else:
                pre = cur
            x = y
        return cur


