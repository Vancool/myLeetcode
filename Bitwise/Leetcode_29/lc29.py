class Solution(object):
    def divide(self, dividend, divisor):
        MAXINT = (1<<31) - 1
        if divisor == -1: return MAXINT if dividend == -(1<<31) else -dividend
        sign = 1 if not (dividend > 0)^(divisor > 0) else -1
        dividend =  abs(dividend)
        divisor = abs(divisor)
        tmp = divisor
        count = 0
        while tmp <= dividend:
            if dividend // 2 < tmp: break #此处防止越界
            tmp = tmp << 1
            count += 1
        res = 0
        while count >= 0:
            if dividend >= tmp:
                res |= (1<<count)
                dividend -= tmp
            tmp = tmp >> 1
            count -= 1
        return sign * res
'''
这题我不会
原来无论哪个进制的除法都是一样的，可以从大到小去除之后得到余数再继续除的
所以十进制除法可以转化为二进制除法
'''

'''
另一种解法：
从底到上加上二进制值
'''

class Solution(object):
    def divide(self, dividend, divisor):
        MAXINT = (1<<31) - 1
        if divisor == -1: return MAXINT if dividend == -(1<<31) else -dividend
        res = 0
        sign = 1 if not (dividend > 0)^(divisor > 0) else -1
        if dividend > 0: dividend *= -1
        if divisor > 0: divisor *= -1
        while dividend <= divisor:
            tmp_res = 1
            tmp_divisor = divisor
            while dividend <= tmp_divisor:
                if (tmp_divisor<<1 < (-(1<<31)>>1)) or ((tmp_divisor<<1)< dividend): break
                tmp_divisor <<= 1
                tmp_res <<= 1
            dividend -= tmp_divisor
            res += tmp_res
        return sign * res
'''
另一款从高位到低位
但是题目要求不能用 * 和 /
'''
class Solution(object):
    def divide(self, dividend, divisor):
        MAXINT = (1<<31) - 1
        if divisor == -1: return MAXINT if dividend == -(1<<31) else -dividend
        res = 0
        sign = 1 if not (dividend > 0)^(divisor > 0) else -1
        if dividend > 0: dividend *= -1
        if divisor > 0: divisor *= -1
        tmp_res = 1
        while dividend <= divisor:
            if dividend <= tmp_res * divisor:
                dividend -= tmp_res * divisor
                res += tmp_res
                tmp_res += tmp_res
            else:
                tmp_res //= 2
        return sign * res




a = Solution()
print(a.divide(10,3))