class Solution(object):
    def nextGreaterElement(self, n):
        n = list(str(n))
        MAXINT = 1<<32 - 1
        MAXINT = list(str(MAXINT))
        if len(n) == 1: return -1
        for i in range(len(n)-1,0,-1):
            if n[i] > n[i-1]:
                j = len(n)-1
                while n[j] <= n[i-1]: j -= 1
                n[j], n[i-1] = n[i-1], n[j]
                left, right = i, len(n) - 1
                while left < right:
                    n[left], n[right] = n[right], n[left]
                    left += 1
                    right -= 1
                if len(n) == len(MAXINT):
                    i = len(n) - 1
                    while i >= 0 and n[i] == MAXINT[i]: i -= 1
                    if i >= 0: return -1
                return int("".join(n))
        return -1
'''
test case: 
230241
1999999999
注意已经说了32位了
'''
a = Solution()
print(a.nextGreaterElement(1999999999))

