import math


class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        def getValue(a, x ):
            val = 1
            while a > 0:
                if a%2 : val = x*val
                val = ()
            return val
        k = n % 3
        r = int((1e9 + 7) // 3)
        index = n // 3
        res = 1
        while n > r:
            res = res * math.pow(3, r)
            val
            if k == 0:
                val = math.pow(3, r)
            if k == 1:
                val = math.pow(3, n // 3 - 1) * 4
            if k == 2:
                val = math.pow(3, n // 3) * 2

        return int(val % (1e9 + 7))