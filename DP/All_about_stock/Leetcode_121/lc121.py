class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        curMin = prices[0]
        res = 0
        for i in range(1,len(prices)):
            if prices[i] < curMin:
                curMin = prices[i]
            else:
                res = max(res, prices[i] - curMin)
        return res
a = Solution()
num = [7,1,5,3,6,4]
print(a.maxProfit(num))
print("Done")