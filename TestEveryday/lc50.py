class Solution(object):
    def myPow(self, x, n):
        if x == 0 or x == 1: return x
        if n == 0: return 1
        sign = False
        if n < 0:
            n = -n
            sign = True
        val = 1
        pre = x
        while n:
            if int(n%2) == 1:
               val *= pre
            pre *= pre
            n = n >> 1
        if sign:
            return 1/val
        return val
'''
还是用位运算简洁呀
https://leetcode-cn.com/problems/powx-n/solution/ji-bai-cbai-fen-bai-yong-hu-by-0x404/
'''
class Solution(object):
    def myPow(self, x, n):
        if x == 0 or x == 1: return x
        if n == 0: return 1
        sign = False
        if n < 0:
            n = -n
            sign = True
        res = 1
        while n:
            if n&1:
                res *= x
            n = n >> 1
            x *= x
        if sign: return 1/res
        return res

a = Solution()
print(a.myPow(2.0, 10))
