class Solution(object):
    def mySqrt(self, x):
        left = 0
        right = x
        while left  <= right:
            mid = left + (right - left) // 2
            val = mid ** 2
            if val ==x :
                return mid
            elif val > x:
                right = mid - 1
            elif val < x:
                left = mid + 1
        return right
'''
解法一. 二分

解法二. 牛顿迭代
要注意 cur = 0 的情况
https://leetcode-cn.com/problems/sqrtx/solution/er-fen-cha-zhao-niu-dun-fa-python-dai-ma-by-liweiw/
'''
class Solution1(object):
    def mySqrt(self, x):
        if x == 0: return 0
        cur = x//2
        while True:
            pre = cur
            cur = (cur + x/cur) / 2
            if abs(cur - pre) < 1e-7:
                return int(cur)
            '''
            while abs(x0 - x1) < 1:
                return int(x1)
            '''
a = Solution1()
print(a.mySqrt(8))
print("Done")
