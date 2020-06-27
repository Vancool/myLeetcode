class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        dp = [0]*len(num)
        dp[-1] = 1
        for i in range(len(num)-2,-1,-1):
            val = int(num[i:i+2])
            if 10 <= val <= 25:
                if i == len(num)-2:
                    dp[i] = 2
                else:
                    dp[i] = dp[i+1] + dp[i+2]
            else:
                dp[i] = dp[i+1]
        return dp[0]

a = Solution()
num = 102
print(a.translateNum(num))