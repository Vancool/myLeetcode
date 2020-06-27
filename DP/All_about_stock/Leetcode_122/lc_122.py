class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0
        prices.append(-1) #哨兵
        buy_price = prices[0]
        res = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                res += prices[i-1] - buy_price
                buy_price = prices[i]
        return res
'''
我自己的做法一： 贪心 每次只计算递增组的插值，因为如果计算了递减的话就会加上负值
'''
a = Solution()
prices = [5,1]
print(a.maxProfit(prices))
print("Done")

