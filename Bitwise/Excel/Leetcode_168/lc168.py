class Solution(object):
    def convertToTitle(self, n):
        if n <= 0: return ""
        n -= 1
        base = 1
        while n >= base*26: base *= 26
        res = ""
        while base > 1:
            key = n // base
            n = int(n % base)
            res += chr(key+ord("A")-1)
            base //= 26
        res += chr(n+ord("A"))
        return res
'''
easy 题， 我不会
'''

a = Solution()
print(a.convertToTitle(701))