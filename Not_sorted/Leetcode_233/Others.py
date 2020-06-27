
class Solution(object):
    def countDigitOne(self, n):
        base = 1
        before = 0
        cur = n
        res = 0
        while cur:
            key = int(cur % 10)
            if key == 1:
               res += before + (n - base*cur+1)
            if key > 1:
                res += before*key + base
            before = before*10 + base
            base *= 10
            cur = cur//10
        '''
        这个是自己写的方法，有点难理解，我自己写了题解。
        '''
        return res


a = Solution()
print(a.countDigitOne(10))
print("Done")