class Solution(object):
    def coinChange(self, coins, amount):
        if amount < 0: return -1
        if len(coins) == 0: return -1
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        coins.sort()
        for i in range(1,amount+1):
            for key in coins:
                if i - key <0:
                    break
                dp[i] = min(dp[i], dp[i-key] + 1)
        return dp[amount] if dp[amount] < float('inf') else -1

a = Solution()
coins= [2]
print(a.coinChange(coins,3))