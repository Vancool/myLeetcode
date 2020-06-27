class Solution(object):
    def lengthOfLIS(self, nums):
        if len(nums) == 0: return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]: dp[i] = max(dp[j]+1, dp[i])
        return max(dp)