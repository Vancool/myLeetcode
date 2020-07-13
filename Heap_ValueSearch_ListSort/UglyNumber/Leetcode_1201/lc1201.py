class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        res = 1
        key = [a,b,c]
        point = [1] * 3
        while n:
            res = min(point[i]*key[i] for i in range(3))
            for i in range(3):
                if not res % key[i]:
                    point[i] += 1
            n -= 1
        return res

'''
超时
'''
s = Solution()
n = 4
a = 2
b = 3
c = 4
print(s.nthUglyNumber(n,a,b,c))