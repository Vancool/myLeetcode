class Solution(object):
    def isPalindrome(self, x):
        if x < 0: return False
        if 0<= x <= 9: return True
        if x % 10 == 0: return False
        val = 0
        tmp = x
        while tmp:
            val *= 10
            val += int(tmp % 10)
            tmp = tmp // 10
        return val == x
'''
转字符串解法：
1. 双指针
2. a[::-1] = a

不转字符串：
1. 我的解法， 转换成一个翻过来的 这样的话复杂度为O(n)
但是我的解法要处理溢出
2. 只翻转一半然后就判断  复杂度变为 O(n//2)

'''
class Solution(object):
    def isPalindrome(self, x):
        if x < 0: return False
        if 0<= x <= 9: return True
        if x % 10 == 0: return False
        rx = 0
        while x > rx:
            rx *= 10
            rx += int(x % 10)
            x = x // 10
        return rx == x or rx // 10 == x
a = Solution()
print(a.isPalindrome(10))