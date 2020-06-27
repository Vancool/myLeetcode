class Solution1(object):

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 1 or x == 1:
            return x
        if n == 0:
            return 1
        if n<0:
            n = -n
            x = 1/x
        res = 1
        while n:
            if n&1: res = res*x
            x = x*x
            n = n>>1
        return res
'''
Solution 1: 二分法解法： 把 x^n 看成 (x^2)^(n//2) 或者是 x* (x^2)^(n//2) 
先把多出来的x用乘法结合律全部提取出来然后最后和乘方做运算

Solution2: 利用二进制编码把n的每一位对应的x的乘方全部算出来之后再一起乘
 
但是实际上两者的代码是相同的， 唯一不同的是对二分的理解吧
 也就是说用位来表示运算也是一种二分，如果不是搜索而是迭代可以考虑直接把数字转化为二进制
'''
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 1 or x == 1:
            return x
        if n == 0:
            return 1
        if n<0:
            n = -n
            x = 1/x
        res = 1
        base = x
        while n:
            if n&1 == 1:
                res = res*base
            base = base*base #(x, x^2, x^4, ...)
            n = n>>1
        return res