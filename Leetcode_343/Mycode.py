class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        s = [0]*(n+1)
        s[1] = 0
        s[2] = 1
        s[3] = 2
        for i in range(4,n+1):
            val = 0
            mid = i//2
            for j in range(mid, i):
                val = max(val, max(s[j],j)*max(s[i-j],i-j))
            s[i] = val
        return s[i]
a = Solution()
print(a.cuttingRope(10))
print("Done")