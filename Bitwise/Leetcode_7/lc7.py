class Solution(object):
    def reverse(self, x):
        minInt = - 2**31
        maxInt = -minInt - 1
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        s = str(x)
        s = s[::-1]
        x = int(s)
        if minInt <= sign * x <= maxInt:
            return sign * x
        return 0
'''
解法一
int 转 str

解法二
运算
注意一下判断溢出的方法：
if res > maxInt // 10 or (res == maxInt // 10 and ((sign == -1 and lastone > 7) or (sign == 1 and lastone >= 7)))
'''
class Solution(object):
    def reverse(self, x):
        maxInt = (1 << 31) - 1
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        res = 0
        while x:
            key = int(x % 10)
            if res > maxInt // 10 or (res == maxInt // 10 and ((sign == -1 and key > 7) or (sign == 1 and key >= 7)) ):
                return 0
            res = res * 10 + key
            x = x // 10
        return res * sign