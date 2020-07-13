class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n
        key = [1,2,3,5]
        n = n-3
        res = [1,2,3]
        start = 4
        count = 0
        while count < n:
            num = start
            for k in key:
                if k!= 1:
                    while start % k == 0:
                        start = start // k
                        if start in res:
                            start = 1
                            break
                    if start == 1:
                        res.append(num)
                        count += 1
                        break
            start = num + 1
        return res[-1]

a = Solution()
print(a.nthUglyNumber(10))
print("Done")