class Solution(object):
    def titleToNumber(self, s):
        res = 0
        base = 1
        for i in range(len(s)):
            key = s[len(s)-1-i]
            res += base * (ord(key)-ord('A')+1)
            base *= 26
        return res

a = Solution()
print(a.titleToNumber("ZY"))
