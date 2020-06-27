class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]
            if diff > 0:
                res += diff
        return res
'''
解法一.贪心法 
其实是和121的差分 diff 有关
原理其实是把所有的差分求出来，把是正数的差分全部加起来就好
'''
'''
解法二. dp
和121的差分类似， 可以用动态规划来求解
区别是买入时候的状态改变
同样可以做空间优化（但是我太懒所以没写
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return -1
        dp = [[0] * len(prices) for _ in range(2)]
        dp[1][0] = -prices[0]
        for i in range(1, len(prices)):
            dp[0][i] = max(dp[0][i-1], dp[1][i-1] + prices[i])
            dp[1][i] = max(dp[1][i-1], dp[0][i-1] - prices[i])
            '''
            这个位置和121题不一样，121题是
          dp[1][i] = max(dp[1][i-1], -prices[i])
          不会加上 dp[0][i-1] 即买入之前所得
           '''
        return dp[0][len(prices)-1]