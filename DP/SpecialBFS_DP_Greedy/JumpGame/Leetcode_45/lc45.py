class Solution(object):
    def jump(self, nums):
        if len(nums) <= 1: return 0
        dp = [float('inf')] * len(nums)
        dp[-1] = 0
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= len(nums) - 1: dp[i] = 1
            else:
                dp[i] = min(dp[i+1: i+nums[i]+1]) + 1 if nums[i] > 0 else dp[i]
        return dp[0]
'''
复杂度 O(n^2) 超时
'''
class Solution(object):
    def jump(self, nums):
        if len(nums) <= 1: return 0
        pos = 0
        step = 1
        curLimit = 0
        preLimit = nums[0]
        while pos < len(nums) - 1:
            if pos >= preLimit:
                preLimit = curLimit
                step += 1
            pos += 1
            curLimit = max(pos + nums[pos], curLimit)
        return step

'''
试一下广度优先搜索,
写错了
但是我认为 greedy就是一种类型的广度优先，只是用遍历代替了visited
'''

a = Solution()
nums = [1,1]
print(a.jump(nums))