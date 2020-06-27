class Solution(object):
    '''
    没写出来，我也很难过
    '''
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = n
        k = 0
        while n:
            k += 1
            n = n // 10
        count = [0 for _ in range(k)]
        if k == 1:
            return 1 if n<10 else 2
        count[0] = 1
        for i in range(1,k):
            count[i] = count[i-1]*10 + 10**i
        i = k-1
        res = 0
        while num:
            z = num //(10**i)
            num = int(num % 10)
            if i > 0:
                if z <= 1:
                    res += count[i-1]
                else:
                    res += count[i-1]+10**i
            else:
                if num == 0:
                    res += 2
                else:
                    res += 1
                return res
            i -= 1
a = Solution()
print(a.countDigitOne(12))
print("Done")
