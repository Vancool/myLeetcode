class Solution(object):
    def rob(self, nums):
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        prepre = 0
        pre = 0
        res = pre
        for i in range(len(nums)):
            cur = nums[i] + prepre
            res = max(res, cur)
            prepre = pre
            pre = cur
        return res



'''
这题我写错了， 还是要分买与不买的状态
'''
class Solution(object):
    def rob(self, nums):
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        buy = 0
        no_buy = 0
        for i in range(len(nums)):
            curbuy = no_buy + nums[i]
            cur_nobuy = max(buy, no_buy)
            buy = curbuy
            no_buy = cur_nobuy
        return max(buy, no_buy)

'''
还有另一种想法：
每个代表着到i为止获得的最大金额
因此 dp[i] = max(dp[i-1], dp[i-2] + num[i])
'''