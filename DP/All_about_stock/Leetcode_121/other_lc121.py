class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0
        dp = [[0]*len(prices) for _ in range(2)]
        dp[1][0] = -prices[0]
        for i in range(1, len(prices)):
            dp[0][i] = max(dp[0][i-1], dp[1][i-1] + prices[i])
            dp[1][i] = max(dp[1][i-1], -prices[i])
        return dp[0][len(prices)-1]
'''
解法一： dp
状态： 天数 + 第n天是否买入卖出 [已经被买入1 / 未被买入（或者刚好卖出） 0]  
表示的值： 到第i天买入/未买入的最大的利润（如果买入就是负值）
状态转移方式：
 第i天卖出or未被买入 ： dp[0][i] = max( 前一天未被买入最大值，前一天被买入今天被卖出值 )
 第i天已经被买入：      dp[1][i] = max( 今天之前已经被买入最大值， 从今天开始买入)
 我们要的结果： dp[0][n] 第n天一定要卖出不能存着， dp[1][n] 可以不用管了
 参考：
 https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/bao-li-mei-ju-dong-tai-gui-hua-chai-fen-si-xiang-b/
 
 同样的dp思想更加省空间的解法是下面的，就是两个数组倒来倒去的，因为第i天只和第i-1天有关
 这个如何两个数组倒来倒去其实利用了奇偶数的性质 
'''
class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 0 or len(prices) == 1:
            return 0
        dp = [[0]*2 for _ in range(2)]
        dp[1][0] = -prices[0]
        for i in range(1, len(prices)):
            dp[0][i&1] = max(dp[0][i-1 & 1], dp[1][i-1 & 1] + prices[i])
            dp[1][i&1] = max(dp[1][i-1 & 1], -prices[i])
        return dp[0][len(prices)-1 & 1]

'''
但是其实最省空间的是只用0/1两个数组，然后可以转化为优化的暴力法，但是很难解释而且我一开始已经写出来了所以就不管了
'''

'''
解法二 差分法
diff[i] =  p[i+1] - p[i]
问题可以转化为那么实际上是求一组连续的differ使得它们的和最大，为什么可以这样转换？
因为如果在 i 买入在 i+3卖出， 价钱为 p[i+3] - p[i] = p[i+3] - p[i+2] + p[i+2] - p[i+1] + p[i+1] - p[i]
                                                = differ[i+2] + differ[i+1] + differ[i]                         
'''

class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 0 or len(prices) == 1:
            return 0
        differ = [0] * (len(prices)-1)
        for i in range(len(differ)):
            differ[i] = prices[i+1] - prices[i]
        res = 0
        cur = 0
        '''此处一定要从0开始， 因为differ可能都为负数不盈利'''
        for i in range(len(differ)):
            cur = max(cur+ differ[i], differ[i] )
            res = max(res, cur)
        return res


