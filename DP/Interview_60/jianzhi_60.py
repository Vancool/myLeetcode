class Solution(object):
    def twoSum(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        minVal = n
        maxVal = n*6
        prob = [0] * (n+1)
        prob[0] = 1
        for i in range(1,n+1):
            prob[i] = prob[i-1] * (n-i+1) / i
        res = []
        base = (1/6) ** n
        res.append(1)
        for i in range(1, maxVal + 1 - minVal):
            curRes = 0
            if ((i-1) % 5 == 0):
                left = (i-1) // 5 + 1
                right = n  if i > n else i
                for j in range(left, right + 1):
                    curRes += prob[j]
            else:
                if i < n:
                    curRes += prob[i]
                    curRes += res[-1]
                else:
                    curRes = res[-1]
            res.append(curRes)
        for i in range(len(res)):
            res[i] *= base
        return res
'''
一直想用概率的方法求出来
但是一直都不行，好难算
发现人家是用dp来做的
好气
'''
a = Solution()
print(a.twoSum(2))
print("Done")




