class Solution(object):
    def xorOperation(self, n, start):
        if n == 1: return start
        end = start + 2*(n-1)
        count = 1
        res = 0
        cur_start = start
        pre = 0
        while end:
            if count == 1:
                if start & 2 and n & 2 :
                    res += 1
                    cur_start = cur_start>> 1
            elif count == 2 and cur_start&1 and n&1:
                res += 1
                pre = 1
            else:
                pre = pre^1
                res += ((pre^1) << count)
            count += 1
            end = end >> 1

        return res
class Solution(object):
    def xorOperation(self, n, start):
        if n == 1: return start
        res = 0
        for i in range(n):
            res ^= (start + 2*i)
        return res

a = Solution()
print(a.xorOperation(1,7))
