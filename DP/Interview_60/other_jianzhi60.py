class Solution(object):
    def twoSum(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        maxVal = 6 * n
        dp = [0] * (maxVal + 1)
        for i in range(1,7):
            dp[i] = 1
        for i  in range(2, n+1):
            for j in range(6*i,i-1,-1):
                dp[j] = 0
                '''一定要先清零，因为上一轮dp[j]里面可能有值'''
                for k in range(1,7):
                    if j - k >= i-1:
                        '''
                        这个判断注意一下， 一定是大于等于i-1,而不是0
                        因为上一轮的最小的数为i-1，在i-1之前的都是上上轮骰子出的数值和
                        '''
                        dp[j] += dp[j-k]
        all_count = 6**n
        for i in range(n, 6*n+1):
            dp[i] /= all_count
        return dp[n:6*n+1]

    '''
    这题我根本不会做，本来想用概率的方法，但是没做出来
    发现别人用dp，事实上自己不怎么会做dp的题目
    我是看这个人的题解的
    https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/solution/nge-tou-zi-de-dian-shu-dong-tai-gui-hua-ji-qi-yo-3/
    '''
a = Solution()
print(a.twoSum(2))
print("Done")
