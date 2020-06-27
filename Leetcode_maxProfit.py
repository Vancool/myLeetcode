class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if(n == 0 or n ==1):
            return 0
        if(n == 2):
            if(prices[0] >= prices[1]):
                return 0
            else:
                return prices[1] - prices[0]
        buyVal = min(prices)
        buyIndex = prices.index(buyVal)
        if buyIndex == n-1:
            return self.maxProfit(prices[0:n-1])
        else:
            sellSec = prices[buyIndex+1:]
            sellVal = max(sellSec)
            output1 = sellVal - buyVal
            output2 = self.maxProfit(prices[0:buyIndex])
            return max(output1, output2)

if __name__ == "__main__":
    a = Solution()
    print(a.maxProfit([7,1,5,3,6,4]))