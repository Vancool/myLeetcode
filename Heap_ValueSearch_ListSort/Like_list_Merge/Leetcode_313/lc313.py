class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        res = [1]
        r_p = [0] * len(primes)
        while n > 1:
            n -= 1
            temp = float("inf")
            min_p = -1
            for i, val in enumerate(primes):
                val *= res[r_p[i]]
                if val == res[-1]:
                    r_p[i] += 1
                    val = primes[i] * res[r_p[i]]
                if temp > val:
                    min_p = i
                    temp = val
            r_p[min_p] += 1
            res.append(temp)
        return res[-1]


a = Solution()
n = 12
primes = [2, 7, 13, 19]
print(a.nthSuperUglyNumber(n, primes))